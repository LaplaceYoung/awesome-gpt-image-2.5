# Case 132 — 奢华腕表产品广告模板

| Field | Value |
| --- | --- |
| Kind | t2i |
| Category | Imported showcase |
| Model | GPT Image 2.5 batch |
| Source record | `prompts.json` id 114, source `ym-103` |
| Output | No generated image in source batch |

## Prompt

```prompt
{
  "type": "产品广告",
  "objective": "{argument name="objective" default="为奢华腕表创建电商广告"}",
  "inputs": {
    "subject": "{argument name="subject" default="黑金机械腕表"}",
    "scene": "{argument name="scene" default="黑色石质底座"}",
    "style": "奢华产品摄影",
    "palette": "黑色、金色、深灰色"
  },
  "quality_constraints": {
    "aspect_ratio": "4:5",
    "composition": "居中放置，顶部留有文案空间" 
  },
  "output_requirements": {
    "usage": "电商广告",
    "focus": "表盘与金属质感"
  }
}
```
