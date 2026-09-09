---
name: gpt-image-25-archive
description: Organize, inspect, and cite the archived GPT Image 2.5 prompt and image batch in this repository.
---

# GPT Image 2.5 Archive Skill

Use this skill when adding, reviewing, or exporting the uncurated GPT Image 2.5 batch archive.

## Scope

- Prompt records: `docs/cases/` (imported cases 019–138)
- Generated assets: `assets/generated/`
- Case index: `docs/gallery.md`
- Source notes: `docs/twitter-showcases.md`

## Workflow

1. Read the case page from `docs/cases/`; preserve its numeric ID, title, and prompt.
2. Match an image by zero-padded filename (`001.png` through `107.png`) when the result exists.
3. Keep every case page under `docs/cases/` and every generated image under `assets/generated/`; use the `Imported showcase` category for provenance.
4. Add attribution and source URLs when a prompt or image came from a public collection.
5. Mark any visual reconstruction as `reverse-engineered`; never label inferred wording as an author's original prompt.
6. Update `docs/gallery.md` and `data/cases.json` when records or filenames change.

## Validation

```bash
python3 - <<'PY'
import json
from pathlib import Path
p=Path('docs/archive/gpt-image-25-run/prompts.json')
d=json.loads(p.read_text())
assert len(d) > 0
print(f'{len(d)} prompt records')
print(f'{len(list(Path("assets/archive/gpt-image-25-run").glob("*.png")))} image files')
PY
git diff --check
```

Do not copy the full archive into the curated gallery automatically. Promote individual items only after checking the prompt, image, attribution, and intended use.
