# GPT Image 2.5 style library

Pick a still, a lock list, and a model before writing a prompt for ChatGPT Images 2.5, gpt-image-2.5-flare, or gpt-image-2.5-sunburst.

1. Load data/style-library.json.
2. Resolve style_id to a gallery still and template id.
3. Copy the template from docs/templates.md.
4. Fill slots only. Do not delete lock sentences.
5. If the user attached a photo, treat it as source of truth.
6. For turn two onward, use TPL-03.

Guardrails: one change per turn; quote exact copy; transparent backgrounds only with PNG or WebP.
