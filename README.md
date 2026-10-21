# EvCC Degree Planner

Engineering, Computer Science and Information Technology pathways at Everett Community College: course prerequisite maps, transfer requirements for Washington universities and applied bachelor's programs, a checklist export, and an optional quarter-by-quarter route planner.

A static site: `index.html` (the app) and `data.json` (all courses, degrees and transfer requirements). There is no server code and no database. Students' "completed" checkmarks are saved only in their own browser.

## Publish on GitHub Pages
1. Create a repository (ideally under a department or college GitHub organization rather than a personal account), for example `degree-planner`.
2. Upload `index.html`, `data.json`, `.nojekyll` and this README to the repository root.
3. Settings → Pages → Source: "Deploy from a branch", branch `main`, folder `/ (root)`. Save.
4. After about a minute the site is live at `https://<org>.github.io/degree-planner/`.
5. Optional: add a custom domain (e.g. a subdomain EvCC IT gives you) under Settings → Pages.

## Publish on any other web server
Copy the same files to any folder a web server serves. The page loads `data.json` from the same folder, so it must be served over http(s). Opening the file directly from disk will not load the data.

## Updating requirements
- Edit `data.json` (GitHub's web editor works fine). Each university program has `requirements`, `admission`, `sources` and `verified`.
- Update `meta.checked` when you re-verify.
- The "Data & sources" link in the footer lists every program's status and sources, which works as a yearly review checklist.

## External services the page uses
- Google Fonts (typefaces)
- cdnjs.cloudflare.com (the PDF library, loaded only when someone downloads a PDF)
