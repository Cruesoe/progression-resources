# Progression Resources

Unofficial tools for ferny's Progression RimWorld collections: a searchable catalog of every mod and the whole pack's research tree, linked both ways. The catalog covers:

- [The Progression Modpack [1.6]](https://steamcommunity.com/workshop/filedetails/?id=3521297585) (1/3 Core)
- [The Progression Content (2/3)](https://steamcommunity.com/workshop/filedetails/?id=3521319712)
- [The Progression Cosmetics (3/3)](https://steamcommunity.com/sharedfiles/filedetails/?id=3637541646)

[Site patch notes](CHANGELOG.md)

**Steam snapshot date: 22 November 2026**

**packageId coverage: 1540 of 1543**

**packageId from RimSort steamDB: 1012 of 1545**

**Known packageIds (RimSort + previous overlay): 1540 of 1545**

**Unique mods: 1545** — Core 900 · Content 445 · Cosmetics 200 (3 collection pages omitted from the item list)

This is an unofficial helper, not an official Progression site. Categories are inferred from titles and which collection an item sits in.

## This snapshot vs previous catalog

### Added (2)
- Time Since Save — 3842457773
- Map Vehicles – Ocean Expansion — 3842174841

### Removed (0)
- None

### Renamed (0)
- None

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
| `research.html` | Research tree of the whole pack, with ferny's mods or the ProgressionLESS mods |
| `research/tree.json`, `research/summary.json` | Research tree data, rebuilt from the mods' files when the pack changes |
| `research/experimental-layout.js` | Standalone, dependency-based experimental layout used by Progression New and ProgressionLESS New |
| `backup/progression_collections_categorized.xlsx` | Spreadsheet backup |
| `backup/progression_collections_categorized.txt` | Plain-text grouped list |
| `backup/progression_modpack_mods.txt` | Core pack numbered list |
| `backup/progression_packageids.csv` | Title / workshop ID / packageId table |

## Experimental research layouts

On `research.html`, select **Progression New** or **ProgressionLESS New** to
compare the experimental graph-derived layouts with the original editions.
Both versions use the same underlying project data. The original editions
and their stored positions are unchanged.

The experimental algorithm is kept separately in
`research/experimental-layout.js` so its era-aware, prerequisite-first
scheduling and crossing-reduction approach can be translated into the
Research Organized mod later. It uses no hand-assigned research categories.
The experimental view hides unrelated dependency lines unless
**Show all links** is enabled.

## Enable GitHub Pages (if the live URL 404s)

Repo **Settings → Pages → Build and deployment**

- Source: **Deploy from a branch**
- Branch: `main` / `/ (root)`

## Snapshot notes

- packageIds filled 2026-11-18
- Steam Web API snapshot 2026-09-13
- packageId from RimSort steamDB.json; existing overlay/catalog packageIds kept when RimSort has no row
- New workshop IDs without a RimSort row are left blank (packageId unknown)
- Did not download workshop mods via SteamCMD
