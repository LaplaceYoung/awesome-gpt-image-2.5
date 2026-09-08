# Awesome GPT Image 2.5

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Cases](https://img.shields.io/badge/cases-16-111111)](docs/gallery.md)
[![Templates](https://img.shields.io/badge/prompt%20templates-16-111111)](docs/templates.md)
[![Updated](https://img.shields.io/badge/updated-2026--09--08-blue)](docs/models.md)

An open-source reference library for **ChatGPT Images 2.5** and the **GPT-Image-2.5 Flare / Sunburst** image models. It brings together official launch stills, image-generation and image-editing case studies, reconstruction prompts, reusable prompt templates, and model notes in one searchable repository.

See the [official ChatGPT Images 2.5 announcement](https://openai.com/index/introducing-chatgpt-images-2-5/) for product context; this repository focuses on practical examples and reusable prompt patterns.

[简体中文](README.zh-CN.md) · [Case gallery](docs/gallery.md) · [Prompt templates](docs/templates.md) · [Model guide](docs/models.md)

> **What is this repository?** A practical prompt and visual-reference library for learning, evaluating, and prototyping with GPT Image 2.5. It is documentation and sample data, not an API SDK, model checkpoint, or promise of identical outputs.

## Contents

- [Start here](#start-here)
- [Explore by task](#explore-by-task)
- [What is included](#what-is-included)
- [A repeatable prompt workflow](#a-repeatable-prompt-workflow)
- [Choose a model surface](#choose-a-model-surface)
- [Repository map](#repository-map)
- [For agents and search systems](#for-agents-and-search-systems)
- [Contributing](#contributing)
- [License and attribution](#license-and-attribution)

## Start here

1. **Browse a visual example.** Start with the [16-case gallery](docs/gallery.md), or jump to a category below.
2. **Read the case page.** Each page records the task type, visual constraints, source image or official reference, and a reconstruction prompt when available.
3. **Adapt a template.** Copy a [prompt template](docs/templates.md), replace its `{subject}`, `{change}`, `{lock}`, `{style}`, `{copy}`, or `{format}` slots, and keep the requested change separate from what must remain unchanged.
4. **Check the model notes.** Use [models.md](docs/models.md) for the Flare / Sunburst split, image parameters, and the dated pricing snapshot.

## Explore by task

| Goal | Recommended cases and reference |
| --- | --- |
| Preserve an input image while changing one detail | [Make the Bed](docs/cases/03-making-bed-after.md), [Tuxedo Restyle](docs/cases/05-baby-portrait-after.md), [TPL-01 / TPL-03](docs/templates.md) |
| Render readable type and layout | [Launch Wordmark](docs/cases/01-images2point5_16-9.md), [Poster Grid](docs/cases/06-mid-century-modern-posters.md), [Wedding Invitation](docs/cases/08-wedding-invitation.md) |
| Generate documents or branded graphics | [Science Deck](docs/cases/09-presentation-image.md), [Sticker Poster](docs/cases/10-stickers.md), [TPL-07 / TPL-09](docs/templates.md) |
| Lock a visual style across a scene | [Impressionist Cityscape](docs/cases/11-impressionist-cityscape.md), [Cyberpunk](docs/cases/12-cyberpunk.md), [Retrofuturism](docs/cases/13-retrofuturism.md) |
| Explore identity-preserving edits | [1980s Studio Headshot](docs/cases/15-80s-headshot.md), [TPL-02 / TPL-14](docs/templates.md) |

The complete index is available in [docs/gallery.md](docs/gallery.md), with categories for fidelity and edits, layout and typography, documents, product and brand, character, and style lock.

## What is included

- **16 documented cases** covering text-to-image, image reconstruction, and targeted image edits.
- **Official reference stills** linked to the public launch CDN, paired with local reconstruction slots where generated files are available.
- **16 reusable prompt templates** for local edits, identity-preserving restyles, multi-turn comments, posters, stamps, invitations, decks, pack shots, stickers, and style studies.
- **Model and parameter notes** for ChatGPT Images 2.5, `gpt-image-2.5-flare`, and `gpt-image-2.5-sunburst`.
- **Machine-readable catalogs** in [`data/cases.json`](data/cases.json) and [`data/style-library.json`](data/style-library.json), useful for scripts, evaluation harnesses, and AI agents.

## A repeatable prompt workflow

The case studies use a simple pattern that transfers well between image generation and image editing:

1. **State the source of truth.** Name the attached image, sketch, or previous frame that controls composition, identity, camera, or materials.
2. **Name one change.** Describe the edit or visual objective in a separate sentence.
3. **Declare the locks.** List the regions, text, identity, aspect ratio, and other details that must stay fixed.
4. **Specify output constraints.** Add exact copy, dimensions, style, background, and the intended use when they affect the result.

This separation makes prompts easier to compare, revise, and evaluate across models. The [template library](docs/templates.md) provides ready-to-fill examples.

## Choose a model surface

| Surface | Best fit |
| --- | --- |
| **ChatGPT Images 2.5** | Sketches, format templates, comments, and shareable conversational prompts. |
| **GPT-Image-2.5 Flare** | Fast previews, social crops, higher-volume text-to-image generation, and iterative exploration. |
| **GPT-Image-2.5 Sunburst** | Precision edits, campaign stills, and edit chains where surrounding pixels should remain stable. |

For API names, quality and size options, background handling, snapshots, and the pricing snapshot, see [docs/models.md](docs/models.md). Confirm current model IDs, limits, and prices in the live OpenAI documentation before production or billing decisions.

## Repository map

```text
docs/gallery.md          searchable case index and categories
docs/cases/              one page per still, with metadata and prompts
docs/compare.md          official references and reconstruction files
docs/templates.md        reusable prompt patterns (TPL-01 to TPL-16)
docs/models.md           model surfaces, parameters, and pricing snapshot
data/cases.json          machine-readable case catalog
data/style-library.json  style-to-case and style-to-template mappings
assets/official/         compressed official reference stills
assets/generated/        reconstruction outputs when checked in
```

## For agents and search systems

Use the Markdown pages for human-readable context and the JSON files for deterministic indexing. Each case has a stable numeric ID, slug, title, task kind, category, and documentation path. The style catalog maps named styles to gallery cases and prompt templates. This makes the repository suitable for retrieval-augmented generation, prompt evaluation, dataset bootstrapping, and internal image-generation experiments.

When citing an example, link to its case page so readers can see the source, constraints, and prompt together. Official images and product names remain the property of their respective owners; see the [disclaimer](docs/disclaimer.md) for usage and rights guidance.

## Contributing

Issues and pull requests are welcome. To add a case or template, follow [CONTRIBUTING.md](CONTRIBUTING.md): keep the case metadata complete, register new cases in both the gallery and `data/cases.json`, and preserve the existing prompt format so entries stay comparable.

## License and attribution

The repository's original documentation and prompt text are available under the [MIT License](LICENSE). Official stills are linked from the public launch post and Contentful CDN and are not relicensed by this project. Prompts are starting points; outputs, policy eligibility, and commercial clearance are not guaranteed. Follow the current OpenAI policies and applicable law when generating or editing images.
