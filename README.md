# Awesome GPT Image 2.5

Official stills, reconstruction prompts, and reusable templates for **ChatGPT Images 2.5** / **GPT-Image-2.5 Flare** / **GPT-Image-2.5 Sunburst**.

[English](README.md) | [Simplified Chinese](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Cases](https://img.shields.io/badge/cases-16-111111)](docs/gallery.md)
[![Released](https://img.shields.io/badge/released-2026--09--08-blue)](https://openai.com/index/introducing-chatgpt-images-2-5/)

## Quick links

| Resource | Path |
| --- | --- |
| Case album | [docs/gallery.md](docs/gallery.md) |
| Templates | [docs/templates.md](docs/templates.md) |
| Models | [docs/models.md](docs/models.md) |
| Case index JSON | [data/cases.json](data/cases.json) |
| Agent skill | [agents/skills/gpt-image-2.5-style-library/SKILL.md](agents/skills/gpt-image-2.5-style-library/SKILL.md) |
| Disclaimer | [docs/disclaimer.md](docs/disclaimer.md) |

## Layout of this repository

```
docs/gallery.md          album index
docs/cases/01-....md     one still + metadata + prompt
docs/templates.md        reusable templates by job
docs/models.md           Flare / Sunburst / ChatGPT
data/cases.json          machine-readable catalog
agents/skills/           operator skill for agents
```

Each case page has the same shape: preview image, field table, official phrase when known, reconstruction prompt in a `prompt` fence.

## Category overview

| Category | Cases | Open |
| --- | --- | --- |
| Fidelity and edits | 02-05 | [gallery](docs/gallery.md#fidelity-and-edits) |
| Layout and type | 01, 06-08 | [gallery](docs/gallery.md#layout-and-type) |
| Documents / product / character | 09, 10, 15 | [gallery](docs/gallery.md#documents--product--character) |
| Style lock | 11-14, 16 | [gallery](docs/gallery.md#style-lock) |

## Featured cases

| Case | What to steal |
| --- | --- |
| [03 Make the Bed](docs/cases/03-making-bed-after.md) | Short edit. Freeze the room. |
| [05 Tuxedo Restyle](docs/cases/05-baby-portrait-after.md) | Change only X. |
| [06 Poster Grid](docs/cases/06-mid-century-modern-posters.md) | Shared palette plus nine specified posters. |
| [09 Science Deck](docs/cases/09-presentation-image.md) | UI chrome plus sidebar continuity. |
| [15 1980s Headshot](docs/cases/15-80s-headshot.md) | Official phrase is one sentence; reconstruction locks the print. |

## How to use

1. Find a neighbor still in [docs/gallery.md](docs/gallery.md).
2. Open its case page and copy the reconstruction prompt.
3. If the job is new, start from [docs/templates.md](docs/templates.md) and fill the slots.
4. One change per edit turn. List the locks.

## Sources

Stills are linked from the [Images 2.5 launch post](https://openai.com/index/introducing-chatgpt-images-2-5/) CDN. Reconstruction prompts are reverse-engineered for replication. See [docs/disclaimer.md](docs/disclaimer.md).

## License

MIT. See [LICENSE](LICENSE).
