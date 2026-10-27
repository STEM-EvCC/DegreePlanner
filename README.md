# EvCC Degree Planner

Engineering, Computer Science and Information Technology pathways at Everett Community College: course prerequisite maps, transfer requirements for Washington universities and applied degree programs, a checklist export, and an optional quarter-by-quarter route planner.

A static site: `index.html` is the whole app. There is no server code and no database. Students' "completed" checkmarks are saved only in their own browser.

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
- cdnjs.cloudflare.com (the PDF library, loaded only when someone downloads a PDF)
- cdn.jsdelivr.net (the QR code library, loaded on the checklist to draw a QR code for each university's requirements page)
