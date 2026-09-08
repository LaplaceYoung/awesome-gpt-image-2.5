# Awesome GPT Image 2.5

Curated official samples, structured prompts, and model notes for **ChatGPT Images 2.5** and the API models **GPT-Image-2.5 Flare** and **GPT-Image-2.5 Sunburst**.

[English](README.md) | [Simplified Chinese](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Models](https://img.shields.io/badge/models-Flare%20%7C%20Sunburst-111111)](docs/models.md)
[![Released](https://img.shields.io/badge/released-2026--09--08-blue)](https://openai.com/index/introducing-chatgpt-images-2-5/)

## Official launch

On 8 September 2026 OpenAI shipped ChatGPT Images 2.5: sharper detail, more reliable multi-turn edits, up to 50% lower latency versus Images 2.0, plus Sketch, Templates, inline comments, and shareable prompts.

- Blog: [Introducing ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/)
- System card: [ChatGPT Images 2.5 System Card](https://deploymentsafety.openai.com/chatgpt-images-2-5)
- API guide: [Image generation](https://developers.openai.com/api/docs/guides/image-generation)
- Help: [Images in ChatGPT](https://help.openai.com/articles/11084440)

## Quick links

| Resource | Path |
| --- | --- |
| Official stills | [docs/gallery.md](docs/gallery.md) |
| Prompt templates | [docs/templates.md](docs/templates.md) |
| Flare vs Sunburst | [docs/models.md](docs/models.md) |
| Agent skill | [agents/skills/gpt-image-2.5-style-library/SKILL.md](agents/skills/gpt-image-2.5-style-library/SKILL.md) |
| Style library JSON | [data/style-library.json](data/style-library.json) |
| Disclaimer | [docs/disclaimer.md](docs/disclaimer.md) |

## Category overview

### Case album

Official stills published with the 2.5 launch. Preview pages live in the gallery.

| Category | Cases | Entry |
| --- | --- | --- |
| Hero / cover | 1 | [Gallery](docs/gallery.md#hero) |
| Reference-led edits | 2 pairs | [Gallery](docs/gallery.md#reference-edits) |
| Layout + text | 4 | [Gallery](docs/gallery.md#layout-text) |
| Style studies | 5 | [Gallery](docs/gallery.md#style-studies) |
| Character look | 1 | [Gallery](docs/gallery.md#character) |
| Mosaic / mixed | 1 | [Gallery](docs/gallery.md#mosaic) |

### Prompt template categories

| Category | Templates | Core capability |
| --- | --- | --- |
| Fidelity and edits | TPL-01 to TPL-03 | Keep identity, change only the requested region |
| Layout and type | TPL-04 to TPL-07 | Posters, stamps, invitations, decks |
| Product and brand | TPL-08 to TPL-09 | Pack shots, merch, stickers |
| Style lock | TPL-10 to TPL-14 | Impressionist, cyberpunk, retrofuturism, surreal sci-fi, 1980s portrait |
| Product features | TPL-15 to TPL-17 | Sketch-to-image, templates, comment edits |

## Models at a glance

| Model | Role | When to use |
| --- | --- | --- |
| ChatGPT Images 2.5 | Consumer surface | Sketch, Templates, comments, shared prompts |
| `gpt-image-2.5-flare` | Fast API default | High volume, social, iteration, about 50% lower latency vs GPT-Image-2 |
| `gpt-image-2.5-sunburst` | Precision API | Campaign stills, tight multi-step edits, longer generation |

Token rates (API, per 1M): text in $5 / cached text $1.25 / image in $8 / cached image $2 / image out $30.

Quality knobs: `low`, `medium`, `high`, `xhigh`, `max`, `auto`. Transparent backgrounds on PNG/WebP.

## How to use this repository

1. Open [docs/gallery.md](docs/gallery.md) and pick a still that matches the job.
2. Copy the nearest template from [docs/templates.md](docs/templates.md).
3. Choose Flare for speed or Sunburst for lock-tight edits ([docs/models.md](docs/models.md)).
4. Keep identity, layout, and brand constraints in separate sentences so the model can hold them across turns.
5. For agents, load [data/style-library.json](data/style-library.json) or the skill file.

## Project vision

Treat prompts as versioned assets: one schema, reusable slots, explicit do-not-change clauses. Images 2.5 is strong at preserving subjects and following local edits; the templates in this repo are written to exploit that instead of rewriting the whole frame every turn.

## Notes

Official stills are hosted on OpenAI Contentful CDN and linked from the launch post. This repo does not claim ownership of those images. See [docs/disclaimer.md](docs/disclaimer.md).

## License

MIT. See [LICENSE](LICENSE).
