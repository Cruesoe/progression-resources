# Progression Resources

Unofficial tools for Progression, ProgressionLESS, and Genesis: offline research snapshots and a searchable Progression catalog, linked both ways. The catalog covers:

- [The Progression Modpack [1.6]](https://steamcommunity.com/workshop/filedetails/?id=3521297585) (1/3 Core)
- [The Progression Content (2/3)](https://steamcommunity.com/workshop/filedetails/?id=3521319712)
- [The Progression Cosmetics (3/3)](https://steamcommunity.com/sharedfiles/filedetails/?id=3637541646)

[Site patch notes](CHANGELOG.md)

**Steam snapshot date: 24 November 2026**

**Known packageIds: 1548 of 1551**

**Unique mods: 1551** — Core 901 · Content 448 · Cosmetics 202 (3 collection pages omitted from the item list)

This is an unofficial helper, not an official Progression site. Categories are inferred from titles and which collection an item sits in.

## This snapshot vs previous catalog

### Added (7)
- [LFS] UI Rethemed - Work — 3835296643
- Nurgle Slug Herald — 3840648231
- Hemophage Warcasket — 3844425399
- Soviet Ideology Style — 3843473937
- Resource Readout+ — 3844147232
- Styles Pack for VFE Classical (Fan Mod) — 3840619132
- HYRAX — 3844020959

### Removed (1)
- Sleek Work Priorities — 3764537806

### Renamed (1)
- Fog Color Changer → Dynamic Fog Color — 3492647454

### Newly unavailable (0)
- None

## Open the site

- Live site (GitHub Pages): https://cruesoe.github.io/progression-resources/
- Or open `index.html` from this repo.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Home page |
| `catalog.html` | Searchable catalog, refreshed from Steam every Sunday |
| `research.html` | Research viewer for Progression, ProgressionLESS, and the published Genesis pack |
| `research/tree.json`, `research/summary.json` | Research tree data, rebuilt from the mods' files when the pack changes |
| `backup/progression_collections_categorized.xlsx` | Spreadsheet backup |
| `backup/progression_collections_categorized.txt` | Plain-text grouped list |
| `backup/progression_modpack_mods.txt` | Core pack numbered list |
| `backup/progression_packageids.csv` | Title / workshop ID / packageId table |

## Research editions

- **Progression:** the three published Progression collections.
- **ProgressionLESS:** those collections with published ProgressionLESS replacements; incompatible items declared by the replacements are excluded.
- **Genesis:** the published [Genesis Steam collection](https://steamcommunity.com/sharedfiles/filedetails/?id=3798004429), not the current active game list or Genesis: Core development work.

The viewer reads RimWorld 1.7 XML and applies Research: Organized's offline layout, adapted to 24 projects per column. Runtime-generated research and unsupported custom patch operations may differ from the game. Unreadable collection items are reported in each edition; they are not silently treated as verified. Combined and tabbed layouts support search, mod highlighting, project links, and the optional coordinate grid.

Run `python .github/scripts/check_research.py` to check edition data, layout coordinates, and cross-page counts. The catalog refreshes weekly; research snapshots have a separate build date.

## Enable GitHub Pages (if the live URL 404s)

Repo **Settings → Pages → Build and deployment**

- Source: **Deploy from a branch**
- Branch: `main` / `/ (root)`

## Snapshot notes

- packageIds filled 2026-11-24
- Steam Web API snapshot 2026-11-24
- packageId from RimSort steamDB.json; existing overlay/catalog packageIds kept when RimSort has no row
- packageIds are supplemented from the synced mods' About.xml metadata.
- Research sources are synced from Steam Workshop. Unavailable downloads and unsupported operations remain explicit in the research metadata.
