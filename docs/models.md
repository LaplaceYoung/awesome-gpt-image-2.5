# Models

## Surfaces

| Surface | ID | Notes |
| --- | --- | --- |
| ChatGPT / Work / Codex | ChatGPT Images 2.5 | Sketch, Templates, comments, shareable prompts. Rolling out to all tiers on 2026-09-08. |
| Image API / Responses tool | `gpt-image-2.5-flare` | Default for most apps. Higher quality than GPT-Image-2 at about 50% lower latency. |
| Image API / Responses tool | `gpt-image-2.5-sunburst` | Extra precision, longer generation. Campaign stills and tight edit chains. |
| Snapshots | `gpt-image-2.5-flare-2026-09-08`, `gpt-image-2.5-sunburst-2026-09-08` | Pinned launch snapshots. |

## Choose a model

Use Flare when you need volume, previews, social crops, or conversational iteration.

Use Sunburst when a single element must change and everything else must stay put.

Use ChatGPT Images 2.5 when the operator wants Sketch, a format template, or comment pins on the canvas.

## API parameters that matter

- quality: low | medium | high | xhigh | max | auto
- size: arbitrary WIDTHxHEIGHT on 2.5 models (example 1536x864)
- background: opaque | transparent | auto (transparent requires png or webp)
- Inputs: text + image. Output: image only.

## Pricing snapshot

Per 1M tokens, same schedule for Flare and Sunburst:

| Token type | Price |
| --- | --- |
| Text input | $5.00 |
| Cached text input | $1.25 |
| Image input | $8.00 |
| Cached image input | $2.00 |
| Image output | $30.00 |

Confirm live numbers on OpenAI pricing.
