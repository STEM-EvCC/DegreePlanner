# EvCC Degree Planner

Engineering, Computer Science and Information Technology pathways at Everett Community College: course prerequisite maps, transfer requirements for Washington universities and applied degree programs, a checklist export, and an optional quarter-by-quarter route planner.

A static site: `index.html` is the whole app. There is no server code and no database. Students' "completed" checkmarks are saved only in their own browser.

## Building a schedule ("Plan my route")
- **Add classes I've completed** opens a picker. Students tap the classes they've passed (marking MATH& 152 also checks MATH& 151, and so on up required single-path chains), mark finished gen ed and elective spots, or use their unofficial transcript: they choose the PDF or paste the text, and the page finds the EvCC course numbers. Lines that show a W, NC, F or 0.0 come back unchecked for the student to review.
- **Drag and drop**: drag any class (or gen ed spot) to another quarter, to the "Later" column, or onto Completed. On a phone, press and hold, then drag. The planner fills everything else around the moved classes and flags a class placed before its prerequisites, in a quarter it isn't usually offered, or a quarter over the credit limit. The course panel has a "Quarter" menu that does the same thing from the keyboard.
- **Start over** either undoes the moves or starts a new schedule (clears completed classes, moves, and the quarter, placement and credit settings; majors and universities stay).

## Transfer map
The **Transfer map** tab shows every school in the data that offers the student's selected majors, on a map of Washington with a list beside it (grouped by distance from EvCC). Clicking a pin or a list row shows that school's program, admission model, deadline and links, and adds it to the student's list. In "go to work" mode the tab is called **Next steps map** and shows the BAS and BS options listed for the chosen career paths.

Campus locations are in the `CAMPUS` table in `index.html`, keyed by school id. A school in the data can override its point with `lat` and `lng` fields. A school with no point still appears in the list. Distances are straight-line miles from EvCC's Everett campus.

## Student data
Nothing a student enters leaves their browser. A transcript is read in the page with pdf.js and is never uploaded or saved; only the course numbers the student confirms are kept, in that browser's local storage, the same as the completed checkmarks. Start over clears them. Scanned or photographed transcripts can't be read (there's no text in them), so those students use the pick list.

## Where the data lives

All courses, degrees and transfer requirements come from the shared data repo, **[STEM-EvCC/PathwaysData](https://github.com/STEM-EvCC/PathwaysData)**. This site loads it when it opens:

```
https://stem-evcc.github.io/PathwaysData/data.json
```

The [Pathways](https://github.com/STEM-EvCC/Pathways) site reads the same file, so a fix in PathwaysData updates both sites. That repo checks every change automatically before it goes live; its README explains how to edit.

The address is set once, near the bottom of `index.html`:

```js
const DATA_URL="https://stem-evcc.github.io/PathwaysData/data.json";
```

## Publish on GitHub Pages
Settings → Pages → Source: "Deploy from a branch", branch `main`, folder `/ (root)`. The site is live at `https://stem-evcc.github.io/DegreePlanner/`. PathwaysData must be published too.

## Publish on any other web server
Copy `index.html` and `.nojekyll` to any folder a web server serves, and copy PathwaysData's files to a web server as well. If the data moves, change `DATA_URL` to its new address. The page must be served over http(s); opening the file directly from disk will not load the data.

## Updating requirements
Edit `data.json` in [PathwaysData](https://github.com/STEM-EvCC/PathwaysData), not here. The "Data & sources" link in this site's footer lists every program's status and sources, which works as a yearly review checklist.

## External services the page uses
- stem-evcc.github.io/PathwaysData (the shared data)
- Google Fonts (typefaces)
- cdnjs.cloudflare.com (the PDF libraries: jsPDF, loaded only when someone downloads a PDF, and pdf.js, loaded only when someone reads a transcript PDF)
- cdnjs.cloudflare.com (Leaflet and Leaflet.markercluster, loaded only when someone opens the Transfer map)
- tile.openstreetmap.org (the map background on the Transfer map; no student data is sent)
- cdn.jsdelivr.net (the QR code library, loaded on the checklist to draw a QR code for each university's requirements page)
