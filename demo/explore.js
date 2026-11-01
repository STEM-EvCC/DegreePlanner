function renderExplore(){
  const P=id=>D.programs.find(p=>p.id===id);
  const careersIn=(area,ids)=>(D.careers||[]).filter(c=>c.area===area&&(!ids||ids.includes(c.id))).map(c=>c.id);
  const cards=[
   {k:"life",t:"Biology",c:"--l-bio",what:"Living things from cells to ecosystems. Lab-heavy, with a full year each of general and organic chemistry.",
    math:"Calculus I to Calculus 3 (MATH& 151, 152, 163) for the Biology AS-T.",
    leads:"A BS or BA in biology after transfer, and the usual route toward medical, dental, pharmacy or veterinary school.",
    degrees:["bio-ast"], start:["STEM 101","BIOL& 221","CHEM& 161","MATH& 151"],
    acts:[["transfer",["biology"],"See biology transfer paths"]]},
   {k:"physical",t:"Chemistry, Physics & Astronomy",c:"--l-chem",what:"Matter, energy and the universe. Problem-solving with math at the center.",
    math:"Calculus I to Calculus 3. Physics uses calculus-based physics (PHYS& 241, 242, 243).",
    leads:"A BS in chemistry, biochemistry, physics or astronomy after transfer, then lab, industry or graduate work.",
    degrees:["chem-ast","phys-ast"], start:["STEM 101","CHEM& 161","PHYS& 241","MATH& 151"],
    acts:[["transfer",["chemistry","biochemistry"],"See chemistry transfer paths"],["transfer",["physics","astronomy"],"See physics and astronomy transfer paths"]]},
   {k:"earth",t:"Geology & Earth Science",c:"--l-geo",what:"Rocks, landforms, water and hazards like earthquakes and volcanoes. Fieldwork plus chemistry and physics.",
    math:"Calculus I and II (MATH& 151, 152).",
    leads:"A BS in geology or earth and space sciences after transfer, toward environmental, engineering-geology and resource jobs.",
    degrees:["geol-ast"], start:["STEM 101","GEOL 102","GEOL& 103","CHEM& 161"],
    acts:[["transfer",["geology","environmental-science"],"See geology transfer paths"]]},
   {k:"nursing",t:"Nursing",c:"--l-hlth",what:"Patient care, from EvCC's own RN program to a BSN. Science-heavy: chemistry, anatomy and physiology, and microbiology.",
    math:"Statistics (MATH& 146), after MATH 86. MATH 96 eligibility before CHEM& 121.",
    leads:"The Nursing DTA/MRP is EvCC's RN program (selective admission), with an RN-to-BSN later. The Pre-Nursing DTA/MRP prepares you to apply to a university BSN.",
    degrees:["nursing-dta","prenursing-dta"], start:["HP 101","ENGL& 101","CHEM& 121","MATH& 146"],
    acts:[["transfer",["nursing"],"See nursing transfer paths"]]},
   {k:"health",t:"Health Careers",c:"--l-hlth",what:"Patient care and the business side of health care: medical assisting, phlebotomy, nursing assistant, EMT, billing and coding, and interpreting.",
    math:"MATH or TS 76 level (or BUS 130) for the Medical Assistant and Billing and Coding degrees. Short certificates need no college math. The Allied Health DTA needs one college-level math course.",
    leads:"Jobs right after EvCC with a certificate or an ATA, and BAS programs later. The Allied Health DTA prepares you to transfer toward programs like dental hygiene, sonography and health sciences.",
    degrees:["allied-health-dta","ma-ata","ma-aast","mbc-ata","phleb-cert","na-cert","emt-cert","med-interp-cert","hrm-cert"], start:["HP 101","HLTH 100","HLTH 109","HCM 101"],
    acts:[["work",careersIn("health"),"See health career paths"],["transfer",((P("allied-health-dta")||{}).majors||[]),"See allied health transfer paths"]]},
   {k:"amtec",t:"Advanced Manufacturing",c:"--l-mfg",what:"Welding, precision machining, composites, mechatronics and CAD design at AMTEC. Hands-on, shop-based and job-ready.",
    math:"MATH 86 level, or ENG T 101 (Technical Problem Solving), for the ATA degrees. Most certificates need no college math.",
    leads:"Jobs right after EvCC with a certificate or an ATA. The ATA degrees also connect to BAS programs at CWU and Clover Park Technical College.",
    degrees:["amt-weld-ata","amt-machining-ata","amt-composites-ata","amt-mechatronics-ata","amt-cad-ata"], start:["MFG T 100","ENG T 111","WELD 101","MECH 119"],
    acts:[["work",careersIn("amtec"),"See advanced manufacturing career paths"]]}];
  $("#app").innerHTML=`<h2 class="sr-only">Explore</h2><div class="xgrid">${cards.filter(x=>x.degrees.some(P)).map(x=>`<section class="xcard" style="--xc:var(${x.c})" aria-labelledby="x-${x.k}"><h3 id="x-${x.k}">${x.t}</h3><p>${esc(x.what)}</p>
     <dl><dt>Math</dt><dd>${esc(x.math)}</dd><dt>Leads to</dt><dd>${esc(x.leads)}</dd>
     <dt>At EvCC</dt><dd>${x.degrees.map(P).filter(Boolean).map(p=>`${esc(p.name)} ${esc(p.credential)} <span class="rowt">(${p.total} cr)</span>`).join("<br>")}</dd>
     <dt>Start with</dt><dd><div class="chiprow">${x.start.filter(c=>D.courses[c]).map(chip).join("")}</div></dd></dl>
     <div class="acts">${x.acts.filter(a=>a[1].some(m=>D.majors[m])).map(([g,ms,l],i)=>`<button class="btn${i?" ghost":""}" data-go="${g}" data-ms="${ms.join(",")}">${esc(l)} →</button>`).join("")}</div></section>`).join("")}</div>
   <section class="tips" aria-labelledby="tips-h"><h3 id="tips-h">Torn between two?</h3><ul>
    <li><b>RN now, or BSN first?</b> The Nursing DTA/MRP is EvCC's RN program, with a selective application. The Pre-Nursing DTA/MRP is for going straight to a university BSN. They share most of the science prerequisites (CHEM& 121, BIOL& 211, anatomy and physiology, microbiology), so you can start either way.</li>
    <li><b>Biology or chemistry?</b> Both AS-T degrees include a full year of general chemistry, a year of organic chemistry and Calculus I to 3. Biology adds the BIOL& 221-223 majors sequence; chemistry adds a physics or biology sequence.</li>
    <li><b>Pre-med, pre-dental or pre-vet?</b> These aren't majors. Most students choose Biology or Chemistry and add what each professional school asks for. Check each school's list early.</li>
    <li><b>Science sequences:</b> start CHEM& 161 as early as your math allows. Organic chemistry (CHEM& 261-263) starts in fall and runs fall, winter, spring. Don't split a sequence between colleges.</li>
    <li><b>Medical Assistant certificate, ATA or AAS-T?</b> They share the core coursework. The ATA is built for work; the AAS-T is built to continue to a BAS.</li>
    <li><b>Not sure which trade?</b> The AMT degrees all start with MFG T 100 and ENG T 111, and include one course each from composites, machining, mechatronics and welding, so you try them all.</li>
   </ul><p class="rowt">From the EvCC 2026-27 catalog program pages. Talk with a program advisor before you register.</p></section>`;
  $$("[data-go]").forEach(b=>b.onclick=()=>{ const g=b.dataset.go, ms=b.dataset.ms.split(",").filter(m=>D.majors[m]); S.byGoal[g]=Object.assign({},S.byGoal[g]||{}, {majors:ms,major:ms[0],track:null,schools:[]}); setGoal(g) });
  $$("[data-goto]",$("#app")).forEach(b=>b.onclick=()=>selectCourse(b.dataset.goto));
}
