# Progression Resources

Unofficial tools for ferny's Progression RimWorld collections: a searchable catalog of every mod and the whole pack's research tree, linked both ways. The catalog covers:

- [The Progression Modpack [1.6]](https://steamcommunity.com/workshop/filedetails/?id=3521297585) (1/3 Core)
- [The Progression Content (2/3)](https://steamcommunity.com/workshop/filedetails/?id=3521319712)
- [The Progression Cosmetics (3/3)](https://steamcommunity.com/sharedfiles/filedetails/?id=3637541646)

[Site patch notes](CHANGELOG.md)

**Steam snapshot date: 15 November 2026**

**packageId from RimSort steamDB: 1012 of 1523**

**Known packageIds (RimSort + previous overlay): 1428 of 1523**

**Unique mods: 1523** — Core 893 · Content 435 · Cosmetics 195 (3 collection pages omitted from the item list)

This is an unofficial helper, not an official Progression site. Categories are inferred from titles and which collection an item sits in.

## This snapshot vs previous catalog

### Added (27)
- [LFS] UI Rethemed - Wildlife — 3828731834
- Player Multicolor Ideology Icon — 3839041756
- Visual Progression: Chemfuel — 3837997724
- These Are Our Lands — 3828062951
- Vehicles at Work — 3835520732
- CAI 5000 Performance Fix (1.7) — 3827953715
- I Can Sit On This Throne — 3836624677
- [LFS] UI Rethemed - Main Bar — 3826865706
- Visual Progression: Van's Organ Jars — 3838085030
- Never Home Area — 3839235856
- Chemfuel Retextured : For Medieval and Tribal — 3454176238
- Ambience Core — 3835975372
- Baby Birds Can't Fly — 3836369455
- [DG]More Door Variants — 3832293718
- Automatic Foraging — 3687750532
- [LFS] UI Rethemed - Quests — 3829391880
- Chemfuel Retexture — 3730861087
- Visual Progression: Van's Hemogen Vials — 3836592165
- Van's Retexture : Organ jars — 3541295970
- Panning For Gold Ore Patch — 3836445267
- Linkable Descriptions — 3837322529
- [LFS] UI Rethemed - Animals — 3831602102
- [LFS] UI Rethemed - Notifications — 3827650605
- Injector Implant — 3837632462
- Mech Group Rename & Caravan List — 3837808142
- Dynamic Spacefarer Policy — 3829638797
- Visual Progression Framework — 3834891951

### Removed (8)
- Animal Tab — 712141500
- Declutter UI — 3649094165
- Modern Notifications — 3752932665
- Ponpeco Pajamas — 3482959515
- Ponpeco Furnitures : Kids' Room — 3367310887
- Ponpeco Furnitures : Sci-Fi — 3610234567
- Faction Territories FPS Fix — 3768849805
- Faction Territories and Vassalage — 3626725895

### Renamed (4)
- HALO: Rimworld Psychic Pulse Armory (Continued) → [1.6] HALO: Rimworld Psychic Pulse Armory (Continued) — 3507626861
- Noble and Psycaster Styles Morbid → Noble and Psycaster Furniture Styles Morbid — 3828495663
- Van's Retexture : Hemogen Vials → Van's Retexture : Hemogen Vials  — 3453224032
- Gravship Pilot Console Retexture → Pilot Console Retexture — 3528477422

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

- Steam Web API snapshot 2026-09-13
- packageId from RimSort steamDB.json; existing overlay/catalog packageIds kept when RimSort has no row
- New workshop IDs without a RimSort row are left blank (packageId unknown)
- Did not download workshop mods via SteamCMD
