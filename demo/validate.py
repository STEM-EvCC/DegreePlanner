#!/usr/bin/env python3
"""Check demo/data.json (copy of PathwaysData's scripts/validate.py).

Two passes:
  1. Shape: data.json must match schema/data.schema.json.
  2. Links: ids and course codes that refer to each other must line up.

Errors fail the check (and block the change on GitHub). Warnings are printed
but do not fail, e.g. a prerequisite that names a course outside this catalog
such as ENGL 97.

Run locally:  pip install jsonschema && python3 demo/validate.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: {path.name} is not valid JSON (line {e.lineno}, column {e.colno}): {e.msg}")
        sys.exit(1)


data = load(ROOT / "data.json")
schema = load(ROOT / "data.schema.json")

# 1. Shape
try:
    import jsonschema
except ImportError:
    print("ERROR: install jsonschema first: pip install jsonschema")
    sys.exit(1)

validator = jsonschema.Draft202012Validator(schema)
for e in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
    where = "/".join(str(p) for p in e.absolute_path) or "(top level)"
    err(f"shape: {where}: {e.message[:300]}")

if errors:
    # Link checks assume the shape is right, so stop here.
    for m in errors:
        print("ERROR:", m)
    print(f"\n{len(errors)} error(s). data.json was not accepted.")
    sys.exit(1)

# 2. Links
courses = data["courses"]
majors = data["majors"]
program_ids = [p["id"] for p in data["programs"]]
school_ids = [s["id"] for s in data["schools"]]


def dupes(ids, what):
    seen = set()
    for i in ids:
        if i in seen:
            err(f"{what} id '{i}' is used more than once")
        seen.add(i)


dupes(program_ids, "program")
dupes(school_ids, "school")

for p in data["programs"]:
    for m in p["majors"]:
        if m not in majors:
            err(f"program {p['id']}: major '{m}' is not in majors")
    for g in p["groups"]:
        for item in g["items"]:
            for code in [item["course"]] if "course" in item else item.get("one_of", []):
                if code not in courses:
                    err(f"program {p['id']} group '{g['id']}': course '{code}' is not in courses")

for s in data["schools"] + data["meta"]["statewide"]:
    for sp in s["programs"]:
        if sp["major"] not in majors:
            err(f"school {s['id']}: major '{sp['major']}' is not in majors")
        for r in sp["requirements"]:
            for code in r["courses"]:
                if code not in courses:
                    warn(f"school {s['id']} ({sp['major']}): requirement names '{code}', which is not in courses")

for c in data["careers"]:
    for cred in c["credentials"]:
        if cred not in program_ids:
            err(f"career {c['id']}: credential '{cred}' is not a program id")
    for cert in c["certs"]:
        for code in cert.get("courses", []):
            if code not in courses:
                err(f"career {c['id']}: cert '{cert['name']}' names course '{code}', which is not in courses")


def walk(node, code):
    if "course" in node and node["course"] not in courses:
        warn(f"course {code}: prerequisite '{node['course']}' is not in courses")
    for key in ("all", "any"):
        for child in node.get(key, []):
            walk(child, code)


for code, c in courses.items():
    walk(c["prereq"], code)

for code, o in data["layout_overrides"].items():
    if code not in courses:
        err(f"layout_overrides: '{code}' is not in courses")
    if o.get("same_as") and o["same_as"] not in courses:
        err(f"layout_overrides: '{code}' same_as '{o['same_as']}', which is not in courses")

for i, n in enumerate(data["advisor_notes"]):
    for code in n.get("courses", []):
        if code not in courses:
            err(f"advisor_notes[{i}]: course '{code}' is not in courses")
    for m in n.get("majors", []):
        if m not in majors:
            warn(f"advisor_notes[{i}]: major '{m}' is not in majors")
    for sid in n.get("schools", []):
        if sid not in school_ids:
            warn(f"advisor_notes[{i}]: school '{sid}' is not a school id (fine if it means a group of campuses)")

for m in warnings:
    print("warning:", m)
for m in errors:
    print("ERROR:", m)

print(
    f"\n{len(courses)} courses, {len(program_ids)} EvCC programs, {len(school_ids)} schools, "
    f"{sum(len(s['programs']) for s in data['schools'])} school programs checked."
)
if errors:
    print(f"{len(errors)} error(s). data.json was not accepted.")
    sys.exit(1)
print(f"OK ({len(warnings)} warning(s)).")
