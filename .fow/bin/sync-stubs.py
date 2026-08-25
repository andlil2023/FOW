#!/usr/bin/env python3
"""Regenerate .claude/skills/ pointer stubs from the canonical skills in .fow/skills/.

FOW keeps one copy of every skill in .fow/skills/ (tool-neutral, Law 6). Claude Code only
auto-discovers project skills under .claude/skills/, so each canonical skill gets a stub
there carrying its name and description verbatim. The duplicated description is the one
thing that drifts: edit a canonical description and the stub silently keeps the old one,
so Claude Code triggers on stale text. This script is the fix.

Usage:
    python .fow/bin/sync-stubs.py           regenerate stubs, report what changed
    python .fow/bin/sync-stubs.py --check   report drift only, write nothing, exit 1 if any

--check is what you want in CI or a pre-commit hook.

Stdlib only, no dependencies. Run from the repo root.
"""

import re
import shutil
import sys
from pathlib import Path

CANONICAL = Path(".fow/skills")
STUBS = Path(".claude/skills")
MARKER = "Pointer only. Canonical skill:"

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)


def field(frontmatter, key, path):
    m = re.search(rf"^{key}:[ \t]*(.+?)[ \t]*$", frontmatter, re.M)
    if not m:
        sys.exit(f"error: {path} frontmatter has no '{key}:'")
    return m.group(1)


def read_skill(path):
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER.match(text)
    if not m:
        sys.exit(f"error: {path} does not start with a YAML frontmatter block")
    fm = m.group(1)
    return field(fm, "name", path), field(fm, "description", path)


def stub_text(name, description, slug):
    # Always LF, on every platform: .gitattributes pins the whole kit to LF, so writing
    # anything else just produces a file git normalizes on the next commit.
    return (
        f"---\nname: {name}\ndescription: {description}\n---\n\n"
        f"{MARKER} `{CANONICAL.as_posix()}/{slug}/SKILL.md`\n\n"
        "Read that file now and follow it exactly. Do not act before reading it.\n"
        "Never edit this stub to change behaviour — edit the canonical file.\n"
    )


def main():
    check = "--check" in sys.argv[1:]
    if unknown := [a for a in sys.argv[1:] if a != "--check"]:
        sys.exit(f"error: unknown argument(s): {' '.join(unknown)}\n{__doc__.splitlines()[0]}")

    if not CANONICAL.is_dir():
        sys.exit(f"error: {CANONICAL} not found — run this from the repo root")

    written, stale, removed, kept = [], [], [], 0

    slugs = sorted(d.name for d in CANONICAL.iterdir() if (d / "SKILL.md").is_file())
    if not slugs:
        sys.exit(f"error: no SKILL.md files under {CANONICAL}")

    for slug in slugs:
        source = CANONICAL / slug / "SKILL.md"
        name, description = read_skill(source)
        want = stub_text(name, description, slug)

        target = STUBS / slug / "SKILL.md"
        current = None
        if target.is_file():
            # newline="" so line endings compare literally; Path.read_text grew the kwarg in 3.13.
            with open(target, encoding="utf-8", newline="") as fh:
                current = fh.read()

        if current == want:
            kept += 1
            continue
        (stale if check else written).append(slug)
        if not check:
            target.parent.mkdir(parents=True, exist_ok=True)
            with open(target, "w", encoding="utf-8", newline="") as fh:
                fh.write(want)

    # Stubs whose canonical skill is gone. Only touch files that are actually stubs.
    if STUBS.is_dir():
        for d in sorted(STUBS.iterdir()):
            if not d.is_dir() or d.name in slugs:
                continue
            f = d / "SKILL.md"
            if f.is_file() and MARKER not in f.read_text(encoding="utf-8"):
                print(f"  ! {d.name}: not a generated stub, leaving alone")
                continue
            removed.append(d.name)
            if not check:
                shutil.rmtree(d)

    if check:
        for s in stale:
            print(f"  drift: {s}")
        for s in removed:
            print(f"  orphan: {s}")
        if stale or removed:
            print(f"\n{len(stale)} drifted, {len(removed)} orphaned, {kept} in sync")
            print("run: python .fow/bin/sync-stubs.py")
            return 1
        print(f"all {kept} stubs in sync")
        return 0

    for s in written:
        print(f"  wrote: {s}")
    for s in removed:
        print(f"  removed: {s}")
    print(f"{len(written)} written, {len(removed)} removed, {kept} already current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
