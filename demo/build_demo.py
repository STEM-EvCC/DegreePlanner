#!/usr/bin/env python3
"""Build demo/index.html from the live index.html.

The demo is the same planner pointed at demo/data.json (sciences, health
sciences and Advanced Manufacturing), with the few spots that assume
Engineering/CS/IT made general. Run this again after changing the live
index.html so the demo picks up the change:

    python3 demo/build_demo.py

Each replacement must match exactly once, so a change to the live page that
breaks one stops the build with a message instead of producing a bad demo.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = (ROOT / "index.html").read_text(encoding="utf-8")
EXPLORE = (ROOT / "demo" / "explore.js").read_text(encoding="utf-8").strip()

R = []  # (old, new, why)

# Course prefixes drawn in the "Health" lane of the map.
HEALTH_PREFIXES = ["NURS", "HLTH", "HCM", "MC", "HP", "EMS"]


def rep(old, new, why):
    R.append((old, new, why))


# ---- page identity -------------------------------------------------------
rep('<meta name="description" content="EvCC engineering, computer science and IT courses, prerequisites and transfer requirements.">',
    '<meta name="description" content="Demo: EvCC science, health sciences and advanced manufacturing courses, prerequisites and transfer requirements.">',
    "description")
rep("<title>EvCC Degree Planner</title>", "<title>Degree Planner Demo</title>", "title")
rep('<h1>Degree Planner <span class="proto">Prototype</span></h1>',
    '<h1>Degree Planner <span class="proto">Demo</span></h1>', "badge")
rep('<div class="sub">Everett Community College · Engineering, Computer Science &amp; IT courses, prerequisites and transfer requirements</div>',
    '<div class="sub">Everett Community College · Sciences, Health Sciences &amp; Advanced Manufacturing courses, prerequisites and transfer requirements</div>',
    "subtitle")
rep('<section class="trip" id="trip" aria-label="Your goal"></section>',
    '<div class="demobar" role="note"><b>Demo for review.</b> This page is separate from the live Degree Planner (Engineering, Computer Science and IT) and uses its own data. Facts here are still being checked, so don\'t use it for advising yet. <a href="../">Open the live planner</a></div>\n  <section class="trip" id="trip" aria-label="Your goal"></section>',
    "demo banner")
rep(".toast{position:fixed;",
    ".demobar{margin:2px 0 12px;padding:10px 14px;border:1px dashed var(--warn);border-radius:var(--r);background:color-mix(in srgb,var(--warn) 9%,var(--surface));font-size:.88rem;color:var(--ink-2)}.demobar b{color:var(--ink)}\n.toast{position:fixed;",
    "demo banner style")

# ---- separate saved state from the live planner (same github.io origin) ---
rep('localStorage.getItem("evccpath:"+k)', 'localStorage.getItem("evccdemo:"+k)', "storage read")
rep('localStorage.setItem("evccpath:"+k', 'localStorage.setItem("evccdemo:"+k', "storage write")

# ---- lanes: add earth science and health ---------------------------------
for theme in ("--l-it:#B23A6E; --l-mfg:#3E6A8A;",):
    rep(theme, theme + " --l-geo:#8A5A2B; --l-hlth:#C0396B;", "light lane colors")
src_dark = "--l-it:#E57FA8; --l-mfg:#86B0CF;"
# two identical dark blocks: handled after the loop below
rep('{id:"bio",label:"Biology",v:"--l-bio"},{id:"engr",label:"Engineering",v:"--l-engr"},{id:"cs",label:"Comp Sci",v:"--l-cs"},{id:"it",label:"Info Tech",v:"--l-it"},{id:"mfg",label:"Advanced Manufacturing",v:"--l-mfg"},',
    '{id:"bio",label:"Biology",v:"--l-bio"},{id:"geo",label:"Earth Science",v:"--l-geo"},{id:"hlth",label:"Health",v:"--l-hlth"},{id:"engr",label:"Engineering",v:"--l-engr"},{id:"cs",label:"Comp Sci",v:"--l-cs"},{id:"it",label:"Info Tech",v:"--l-it"},{id:"mfg",label:"Advanced Manufacturing",v:"--l-mfg"},',
    "lanes")
rep('const laneOf=c=>{const p=c.split(" ")[0];',
    'const HLTH=new Set(__HEALTH_PREFIXES__); const GEO=new Set(["GEOL","GEOL&","OCEA","OCEA&","ATM","ENVS","ENVS&","GEOG"]);\nconst laneOf=c=>{const p=c.split(" ")[0]; if(HLTH.has(p)||HLTH.has(c.replace(/\\s\\d.*$/,"")))return"hlth"; if(GEO.has(p))return"geo"; if(p.startsWith("ASTR"))return"phys"; if(p.startsWith("NUTR"))return"bio";',
    "laneOf")

# ---- areas ------------------------------------------------------------------
rep('if(!a.size)a.add("engineering"); return a }',
    'if(!a.size)a.add(D.programs[0].area); return a }', "default area")
rep("const menuOk=c=>/^(IT|CS|CL|STEM|WELD|MFG|ENG T|CT|MECH)\\b/.test(c);",
    "const menuOk=c=>/^(IT|CS|CL|STEM|WELD|MFG|ENG T|CT|MECH)\\b/.test(c)||laneOf(c)===\"hlth\";", "menuOk")
rep('const t=D.programs.filter(p=>p.majors.includes(m)); return t.length?t:D.programs.filter(p=>p.id==="general") }',
    'const t=D.programs.filter(p=>p.majors.includes(m)); return t.length?t:[FALLBACK_PROG(m)] }\nfunction FALLBACK_PROG(m){ return D.programs.find(p=>p.kind==="transfer") }',
    "tracksFor fallback")
rep('if(n.length<=3)return n.slice(0,-1).join(", ")+" & "+n[n.length-1]+" Engineering";',
    'if(n.length<=3)return n.slice(0,-1).join(", ")+" & "+n[n.length-1];', "majPhrase")

# ---- goal sentence ----------------------------------------------------------
rep('const GL={"civil-mech":"Engineering · Civil & Mechanical MRP","comp-ee":"Engineering · Computer & Electrical MRP","bio-chem":"Engineering · Bioengineering & Chemical MRP","general":"Engineering · General AS-T","cs-dta":"Computer Science · CS DTA/MRP","it-aast":"Information Technology · IT AAS-T / ATA"};',
    'const AREAL={science:"Sciences",health:"Health Sciences",amtec:"Advanced Manufacturing"}; const GL={}; D.programs.forEach(p=>GL[p.id]=(AREAL[p.area]||p.area)+" · "+p.name+" "+p.credential);',
    "group labels")
rep('const groups=S.goal==="work"?[["IT career paths",majorsAll().filter(m=>CAREER(m).area==="it")],["Advanced Manufacturing career paths",majorsAll().filter(m=>CAREER(m).area==="amtec")]].filter(g=>g[1].length):',
    'const groups=S.goal==="work"?[["Health career paths",majorsAll().filter(m=>CAREER(m).area==="health")],["Advanced Manufacturing career paths",majorsAll().filter(m=>CAREER(m).area==="amtec")],["Other career paths",majorsAll().filter(m=>!["health","amtec"].includes(CAREER(m).area))]].filter(g=>g[1].length):',
    "work groups")
rep("Most engineering and computer science jobs need a BS, which means transferring. Choose \"transfer and study\" for those.",
    "Science careers, and nursing beyond the RN, usually need a four-year degree, which means transferring. Choose \"transfer and study\" for those.",
    "work note")
rep("Not sure yet? Compare Engineering, Computer Science and IT below, then pick a goal.",
    "Not sure yet? Compare the sciences, health programs and Advanced Manufacturing below, then pick a goal.",
    "explore note")

# ---- labels that said BS ------------------------------------------------------
rep('degree:{s:"BS",l:"Counts toward BS"}', 'degree:{s:"DEG",l:"Counts toward the degree"}', "category label")
rep('<span class="stag c-degree">${esc(sl[0].abbr)}</span>Counts toward BS</span>',
    '<span class="stag c-degree">${esc(sl[0].abbr)}</span>Counts toward the degree</span>', "route legend label")
rep('${LANES.filter(l=>l.id!=="bio"||S.major==="bioengineering"||S.major==="chemical").map(',
    '${LANES.filter(l=>[...r.quarters.flatMap(q=>q.items.filter(i=>i.c).map(i=>i.c)),...doneList].some(c=>laneOf(c)===l.id)).map(',
    "route legend lanes")

# ---- explore page -------------------------------------------------------------
start = src.index("function renderExplore(){")
end = src.index("/* ---------- careers ---------- */")
rep(src[start:end], EXPLORE + "\n", "explore page")

# ---- spec note: only programs that have specialization lists ----------------------
rep('note:"EvCC\'s catalog doesn\'t list specialization courses for this school, so the site uses the school\'s own transfer requirements. Confirm your picks with an advisor."};',
    'note:Object.keys(p.spec.by||{}).length?"EvCC\'s catalog doesn\'t list specialization courses for this school, so the site uses the school\'s own transfer requirements. Confirm your picks with an advisor.":""};',
    "spec note")

# ---- careers ------------------------------------------------------------------
rep('<p class="rowt" style="margin-top:6px">Certificates stack into the ATA. Pick a step to see its courses on the map, route and checklist.</p>',
    '<p class="rowt" style="margin-top:6px">${car.area==="amtec"||car.area==="it"?"Certificates stack into the ATA. ":""}Pick a step to see its courses on the map, route and checklist.</p>',
    "stack note")

# ---- data & sources -------------------------------------------------------------
rep('Everything the site shows comes from one shared file, <code>data.json</code> in <a href="https://github.com/STEM-EvCC/PathwaysData" target="_blank" rel="noopener">STEM-EvCC/PathwaysData</a>. The Pathways site reads the same file, so a fix there updates both.',
    'This demo reads its own file, <code>demo/data.json</code> in <a href="https://github.com/STEM-EvCC/DegreePlanner/tree/main/demo" target="_blank" rel="noopener">STEM-EvCC/DegreePlanner</a>, so nothing here changes the live planner or the Pathways site. When a program is approved, its entries move into the shared file in STEM-EvCC/PathwaysData.',
    "data intro")
rep("<dt>Offerings</dt><dd>Department course list (2021), updated with Winter 2024 advising notes. Confirm against the class schedule each year.</dd>",
    "<dt>Offerings</dt><dd>Quarters offered are shown only for courses carried over from the live data. Confirm against the class schedule.</dd>",
    "offerings")
rep("const sw=D.meta.statewide&&D.meta.statewide[0];", "const sws=D.meta.statewide||[];", "statewide all")
rep('${sw?`<div class="card"><h4>Statewide agreements</h4><ul>${sw.general_notes.map(n=>`<li>${esc(n)}</li>`).join("")}</ul></div>`:""}',
    '${sws.map(sw=>`<div class="card"><h4>${esc(sw.name)}</h4><ul>${sw.general_notes.map(n=>`<li>${esc(n)}</li>`).join("")}</ul>${(sw.programs||[]).flatMap(p=>p.sources||[]).length?`<p class="rowt">${[...new Set((sw.programs||[]).flatMap(p=>p.sources||[]))].map(u=>`<a href="${esc(u)}" target="_blank" rel="noopener">${esc(u.replace(/^https?:\\/\\//,"").slice(0,50))}</a>`).join("<br>")}</p>`:""}</div>`).join("")}',
    "statewide cards")
rep('<th style="text-align:left">Changed since 2021 advising sheet</th>', '<th style="text-align:left">Notes</th>', "notes col")
rep("${(p.changes_from_2021_sheet||[]).map(esc).join(\"<br>\")}", "${(p.notes||[]).map(esc).join(\"<br>\")}", "notes col body")

# ---- defaults and data address ----------------------------------------------------
rep('const b=S.byGoal[g]||(g==="work"?{majors:["it-support"],major:"it-support",schools:[],track:null}:{majors:["mechanical"],major:"mechanical",schools:["uw-seattle"],track:null});',
    'const b=S.byGoal[g]||(g==="work"?{majors:[DEF_CAREER()],major:DEF_CAREER(),schools:[],track:null}:{majors:[DEF_MAJOR],major:DEF_MAJOR,schools:[],track:null});',
    "setGoal defaults")
rep('const DATA_URL="https://stem-evcc.github.io/PathwaysData/data.json";',
    'const DATA_URL="data.json"; // demo/data.json, next to this page\nconst DEF_MAJOR="biology"; const DEF_CAREER=()=>(D.careers&&D.careers[0]&&D.careers[0].id)||"";',
    "data url")
rep('S.schools=["uw-seattle"]; S.majors=["mechanical"];', 'S.schools=[]; S.majors=[DEF_MAJOR]; S.major=DEF_MAJOR;', "boot defaults")
rep('if(S.goal==="work"&&!sel){S.majors=["it-support"];S.major="it-support";S.schools=[]}',
    'if(S.goal==="work"&&!sel){S.majors=[DEF_CAREER()];S.major=DEF_CAREER();S.schools=[]}', "boot work default")
rep('if(!S.majors.length)S.majors=[g==="work"?"it-support":"mechanical"];',
    'if(!S.majors.length)S.majors=[g==="work"?DEF_CAREER():DEF_MAJOR];', "setGoal fallback")
rep('if(!S.majors.length)S.majors=[S.goal==="work"?"it-support":"mechanical"];',
    'if(!S.majors.length)S.majors=[S.goal==="work"?DEF_CAREER():DEF_MAJOR];', "boot fallback")
rep("$(\"#footMeta\").innerHTML=`Prototype built from",
    "$(\"#footMeta\").innerHTML=`Demo built from", "footer")
rep('program:"civil-mech",major:"mechanical",school:"uw-seattle"', 'program:"",major:"biology",school:""', "initial state")
rep('math:"MATH& 151",chem:"CHEM& 161"', 'math:"MATH& 141",chem:"CHEM& 161"', "plan math default")

out = src
for old, new, why in R:
    n = out.count(old)
    if n != 1:
        raise SystemExit(f"build_demo: '{why}' matched {n} times, expected 1. Update demo/build_demo.py.")
    out = out.replace(old, new)
n = out.count(src_dark)
if n != 2:
    raise SystemExit(f"build_demo: dark lane colors matched {n} times, expected 2.")
out = out.replace(src_dark, src_dark + " --l-geo:#C79A6B; --l-hlth:#EE7FA6;")

import json
out = out.replace("__HEALTH_PREFIXES__", json.dumps(HEALTH_PREFIXES))

(ROOT / "demo" / "index.html").write_text(out, encoding="utf-8")
print(f"demo/index.html written ({len(R)} replacements).")
