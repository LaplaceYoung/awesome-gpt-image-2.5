# Case 112 — 英文社论报纸排版

| Field | Value |
| --- | --- |
| Kind | t2i |
| Category | Imported showcase |
| Model | GPT Image 2.5 batch |
| Source record | `prompts.json` id 94, source `ym-43` |
| Output | [`assets/generated/112-imported-.png`](../../assets/generated/112-imported-.png) |

## Prompt

```prompt
主题：{argument name="subject" default="文化评论"} / 英语等级：{argument name="English level" default="B2"} / 字数：{argument name="word count" default="400"}

生成一份高端黑白社论风格的英文文章排版，类似于高级文学杂志、文化期刊或报纸专题页面。

文章语言必须为英语，写作必须严格遵循第一行指定的 CEFR 英语等级。英语等级可选 A1、A2、B1、B2、C1 或 C2；“主题”为文章话题；“字数”为目标英文单词数。

英语难度要求：
- A1：非常基础，使用高频词汇和简单的短句。
- A2：常用生活词汇，简单的连接词和基础复合句。
- B1：更丰富的日常和抽象词汇，包含原因、示例和观点。
- B2：成熟的论证表达，词汇丰富，句式结构复杂且逻辑层次分明。
- C1：高级、准确且自然的英语，具备文学品质。
- C2：近乎母语者的文化评论或文学社论水平，运用细腻的修辞和抽象概念。

文章必须围绕指定主题展开，字数控制在目标字数的 ±10% 以内。排版应包含顶部的简洁报头（例如“THE LITERARY REVIEW”）、主标题使用优雅的高对比度衬线字体、作者署名以及三栏式社论网格。左侧包含一段醒目的粗体斜体引语，中心配有一张大型黑白纪实照片及说明文字。整体美学应克制、理性且具有学术感，使用带有轻微油墨晕染和颗粒感的米白色新闻纸纹理。仅限使用黑色、深灰色和米白色。底部应设有一个包含大型斜体行动号召（Call to Action）的信息框。
```
