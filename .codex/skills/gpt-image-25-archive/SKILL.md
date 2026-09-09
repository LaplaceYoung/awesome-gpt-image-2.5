---
name: gpt-image-25-archive
description: Organize, inspect, and cite the archived GPT Image 2.5 prompt and image batch in this repository.
---

# GPT Image 2.5 Archive Skill

Use this skill when adding, reviewing, or exporting the uncurated GPT Image 2.5 batch archive.

## Scope

- Prompt catalog: `docs/archive/gpt-image-25-run/prompts.json`
- Generated assets: `assets/archive/gpt-image-25-run/`
- Archive index: `docs/archive/gpt-image-25-run/README.md`
- Source notes: `docs/archive/gpt-image-25-run/sources/`

## Workflow

1. Read the prompt record from `prompts.json`; preserve its numeric `id`, `title`, and `prompt`.
2. Match an image by zero-padded filename (`001.png` through `107.png`) when the result exists.
3. Keep imported material under `assets/archive/` and `docs/archive/`; curated examples belong under `assets/generated/` and `docs/cases/`.
4. Add attribution and source URLs when a prompt or image came from a public collection.
5. Mark any visual reconstruction as `reverse-engineered`; never label inferred wording as an author's original prompt.
6. Update the archive README when records or filenames change.

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
