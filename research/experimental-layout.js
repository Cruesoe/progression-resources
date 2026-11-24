/* Experimental Progression tree layout.
 * Graph-only layered layout: no manually classified categories or new data.
 * This is a standalone algorithm so its behaviour can later be ported to
 * Research Organized without coupling the mod to the website UI.
 *
 * Pipeline:
 *  1. Preserve technological era order.
 *  2. Topologically schedule each era into capacity-limited columns,
 *     prioritising critical dependency chains and branch hubs.
 *  3. Reorder each column by repeated forward/backward weighted-barycentre
 *     sweeps to align dependent research and reduce visual crossings.
 *  4. Retain a small bias towards original vertical positions for stability.
 *
 * This is Sugiyama-inspired, not a copy or direct port of YART's C# code.
 */
(function (root) {
  'use strict';

  const ERAS = ['Undefined', 'Animal', 'Neolithic', 'Medieval',
    'Industrial', 'Spacer', 'Ultra', 'Archotech'];
  const ROW_STEP = 0.63; // matches the existing card height and separation
  const COLUMN_CAPACITY = 24;
  const SWEEPS = 8;
  const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
  const number = value => Number.isFinite(+value) ? +value : 0;

  function compute(projects, mode) {
    const combined = mode !== 'tabs';
    const getX = p => number(combined ? p.cx : p.ox);
    const getY = p => number(combined ? p.cy : p.oy);
    const nodes = projects.map((p, index) => ({
      id: p.d, p, index, oldX: getX(p), oldY: getY(p),
      era: Math.max(0, ERAS.indexOf(p.rt)),
      parents: [], children: [], internalParents: [], internalChildren: [],
      column: -1, row: 0, critical: -1
    }));
    const byId = new Map(nodes.map(n => [n.id, n]));
    const groups = new Map();
    for (const n of nodes) {
      if (!groups.has(n.era)) groups.set(n.era, []);
      groups.get(n.era).push(n);
    }
    for (const n of nodes) {
      for (const id of n.p.p || []) {
        if ((n.p.hp || []).includes(id)) continue;
        const parent = byId.get(id);
        if (!parent || parent === n) continue;
        n.parents.push(parent);
        parent.children.push(n);
        if (parent.era === n.era) {
          n.internalParents.push(parent);
          parent.internalChildren.push(n);
        }
      }
    }

    // A longer remaining dependency path should be positioned early, so a
    // large collection of independent projects cannot block progression.
    function critical(n, visiting) {
      if (n.critical >= 0) return n.critical;
      if (visiting.has(n)) return 0; // safe fallback for a modded cycle
      visiting.add(n);
      let depth = 0;
      for (const child of n.internalChildren)
        depth = Math.max(depth, 1 + critical(child, visiting));
      visiting.delete(n);
      n.critical = depth;
      return depth;
    }
    for (const n of nodes) critical(n, new Set());

    const columns = [];
    for (const era of [...groups.keys()].sort((a, b) => a - b)) {
      const group = groups.get(era);
      const indegree = new Map(group.map(n => [n, n.internalParents.length]));
      const placed = new Set();
      let ready = group.filter(n => indegree.get(n) === 0);
      let previous = new Set();
      while (placed.size < group.length) {
        if (!ready.length) {
          // A prerequisite cycle can occur in modded XML. Make progress
          // deterministically, without altering the underlying dependency.
          const fallback = group.filter(n => !placed.has(n))
            .sort((a, b) => a.oldX - b.oldX || a.oldY - b.oldY || a.index - b.index)[0];
          ready.push(fallback);
        }
        const score = n => {
          const inherited = n.internalParents.filter(p => previous.has(p)).length;
          return n.critical * 12
            + Math.min(n.internalChildren.length, 20) * 1.5
            + inherited * 9 - n.oldX * 0.12;
        };
        ready.sort((a, b) => score(b) - score(a)
          || a.oldX - b.oldX || a.oldY - b.oldY || a.index - b.index);
        const chosen = ready.splice(0, COLUMN_CAPACITY);
        const index = columns.length;
        for (const n of chosen) {
          n.column = index;
          placed.add(n);
        }
        columns.push(chosen);
        previous = new Set(chosen);
        const newReady = [];
        for (const n of chosen) {
          for (const child of n.internalChildren) {
            if (placed.has(child)) continue;
            const next = indegree.get(child) - 1;
            indegree.set(child, next);
            if (next === 0) newReady.push(child);
          }
        }
        const eligible = new Set([...ready, ...newReady].filter(n => !placed.has(n)));
        ready = [...eligible];
      }
    }

    // Original positions are useful as a stable seed but do not constrain
    // the resulting graph: the dependency graph controls horizontal order.
    for (const col of columns) {
      col.sort((a, b) => a.oldY - b.oldY || a.oldX - b.oldX || a.index - b.index);
      const centre = col.reduce((sum, n) => sum + n.oldY / ROW_STEP, 0) / col.length;
      const offset = clamp(Math.round(centre - (col.length - 1) / 2),
        0, COLUMN_CAPACITY - col.length);
      col.forEach((n, i) => { n.row = i + offset; });
    }

    function reorder(col, forward) {
      if (col.length < 2) return;
      const weight = n => {
        const relevant = forward ? n.parents : n.children;
        let sum = n.row * 0.25 + n.oldY / ROW_STEP * 0.35;
        let total = 0.60;
        for (const other of relevant) {
          const distance = Math.abs(n.column - other.column);
          if (!distance || (forward ? other.column > n.column : other.column < n.column)) continue;
          const w = 2 / Math.sqrt(distance);
          sum += other.row * w;
          total += w;
        }
        return sum / total;
      };
      const desired = new Map(col.map(n => [n, weight(n)]));
      const originalIndex = new Map(col.map((n, i) => [n, i]));
      col.sort((a, b) => desired.get(a) - desired.get(b)
        || originalIndex.get(a) - originalIndex.get(b));
      const centre = col.reduce((sum, n) => sum + desired.get(n), 0) / col.length;
      const offset = clamp(Math.round(centre - (col.length - 1) / 2),
        0, COLUMN_CAPACITY - col.length);
      col.forEach((n, i) => { n.row = i + offset; });
    }
    for (let pass = 0; pass < SWEEPS; pass++) {
      if (pass % 2 === 0) {
        for (let i = 1; i < columns.length; i++) reorder(columns[i], true);
      } else {
        for (let i = columns.length - 2; i >= 0; i--) reorder(columns[i], false);
      }
    }

    return {
      positions: new Map(nodes.map(n => [n.id, { x: n.column, y: +(n.row * ROW_STEP).toFixed(2) }])),
      columns: columns.length,
      projectCount: nodes.length,
      algorithm: 'era-aware topological layers + barycentre ordering'
    };
  }

  root.ProgressionExperimentalLayout = { compute };
})(window);
