# Progression Resources

Unofficial tools for ferny's Progression RimWorld collections: a searchable catalog of every mod and the whole pack's research tree, linked both ways. The catalog covers:

- [The Progression Modpack [1.6]](https://steamcommunity.com/workshop/filedetails/?id=3521297585) (1/3 Core)
- [The Progression Content (2/3)](https://steamcommunity.com/workshop/filedetails/?id=3521319712)
- [The Progression Cosmetics (3/3)](https://steamcommunity.com/sharedfiles/filedetails/?id=3637541646)

[Site patch notes](CHANGELOG.md)

**Steam snapshot date: 18 November 2026**

**packageId coverage: 1518 of 1523**

**packageId from RimSort steamDB: 1012 of 1543**

**Known packageIds (RimSort + previous overlay): 1513 of 1543**

**Unique mods: 1543** — Core 899 · Content 444 · Cosmetics 200 (3 collection pages omitted from the item list)

This is an unofficial helper, not an official Progression site. Categories are inferred from titles and which collection an item sits in.

## This snapshot vs previous catalog

### Added (27)
- Rustic Meal Retexture — 3453364177
- Cherokee Sling - Vehicle and Container Airlift — 3836765380
- Milky Way — 3773448562
- Utility Vehicle — 3627439568
- [LFS] UI Rethemed - Architect — 3830054994
- Visual Progression: Meals — 3834892583
- HE-Chevrolet Tahoe '07 — 3430904230
- NANAME Floors — 3293767181
- Engine Industries — 3009527756
- UI Rethemed - Era Looks — 3840498215
- Body Hair Framework — 3823805934
- HE-Ford B700 Bus '87 — 3281446276
- Wayward Biomes: Core — 3710302618
- Sling Framework — 3840130852
- Progression: Power — 3841675689
- Fog Color Changer — 3492647454
- [LFS] UI Rethemed - Relationships — 3840876824
- Morton's Body Hair (Not Tattoos) — 3825963278
- Progression: Water — 3841674396
- Progression: Waste — 3841676471
- SQUISHY Ranged — 3833016652
- Wayward Biomes: Tangled Hollows — 3837906824
- Progression: Vehicles — 3841677765
- Smooth Terrain — 3502765685
- Overlord Warcasket — 3841078351
- GTek's Vehicles - 1998 Subaru Forester — 3367924127
- [LFS] UI Rethemed - Colonist Card — 3828206639

### Removed (7)
- CAI 5000 Performance Fix (1.7) — 3827953715
- Better Inspect Pane — 3788686557
- RimHUD — 1508850027
- Chest Hair Tattoos — 3549854404
- Cybranian - Social Interface — 2854221326
- [LYN] VVE Renamed — 3014810352
- RimHUD Passion Icons — 3829500081

### Renamed (1)
- Won hair_women → Won hair_women  — 1886150617

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
| `backup/progression_collections_categorized.xlsx` | Spreadsheet backup |
| `backup/progression_collections_categorized.txt` | Plain-text grouped list |
| `backup/progression_modpack_mods.txt` | Core pack numbered list |
| `backup/progression_packageids.csv` | Title / workshop ID / packageId table |

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
