---
stage: academic_figure_prompt
stage_status: confirmed
requires_confirmed:
  - ppt_production_brief
  - fact_ledger
  - storyboard
  - asset_layout_plan
allowed_next_stage: ppt-content-fidelity-qa-stage
confirmed_by: user/2026-05-31
source_skill: https://github.com/LigphiDonk/academic-figure-generator/tree/main/academic-figure-prompt
created_at: 2026-05-31
target_slide: 3
generation_tool_intent: image2
---

# Slide 3 Academic Figure Prompt v0

## Alignment

- Figure purpose：overall framework diagram.
- Slide anchor：Slide 3, `初步观察：技术突围的五个维度`.
- Visualized claim：技术突围不是单点发明，而是研发设计、工程转化、产业链协同、人才组织、全球布局五个维度的系统协同。
- Source anchors：F7, F8, F9, F10, F13, F14, F15.
- Audience：课程小组成员、组长、开题报告展示听众。
- Aspect ratio：16:9, designed for a PowerPoint slide body area below the action title.
- Generation boundary：只生成解释性框架示意图，不作为企业事实截图、数据图或证据图；不得添加具体数值、客户名称、未确认产品照片、真实 logo、工厂实拍、地图坐标或未确认技术细节。
- Editability expectation：image2 输出为 raster image，插入 PPT 后不可逐元素编辑；保留 slide title、action title、footer citation and speaker notes as editable PPT text.
- Palette：custom template-derived academic palette, deep violet `#3C3652`, violet `#7561D6`, blue `#5199EA`, muted cyan `#68A4C6`, near-white `#F7F8FB`, soft grey `#D9DDE8`.

## Prompt

```text
A highly detailed, information-dense academic paper framework diagram about "Five-dimensional mechanism of technological breakthrough in a high-tech enterprise", designed for a Chinese Marxism course opening-report PowerPoint slide. Create a clean 16:9 white-background diagram that visually explains a system-synergy framework, not a decorative poster and not a factual evidence image. The diagram should fit in the body area of a slide, leaving empty margin at the top for an existing slide title and action title.

=== CENTRAL SYSTEM CORE ===
Place a central rounded hexagonal module with white fill, thin deep-violet border, and a small two-line Chinese label: "高科技企业" / "技术突围". Inside the module, add a subtle monochrome mini-thumbnail of interlocking gears and a rising capability curve, using only thin grey and violet lines. Around the core, show a faint circular coordination ring labelled in small Chinese text: "系统协同".

=== FIVE DIMENSION MODULES ===
Arrange five white rounded modules evenly around the central core, connected by thin curved arrows. Each module must include a Chinese title and 2-3 tiny sub-elements, not empty boxes:
1. "研发设计": small icons/thumbnails of a chip outline, optical/acoustic wave lines, and a product prototype sketch.
2. "工程转化": miniature process path from prototype to manufacturable module, with a tool mark and a small factory-line schematic.
3. "产业链协同": vertical chain of components, modules, smart hardware, and an integration node, with dashed supplier-to-manufacturing links.
4. "人才组织": small team-network thumbnail, two young researcher silhouettes in line-art style, and a knowledge-sharing node.
5. "全球布局": simplified abstract globe grid with connected R&D nodes, no real map labels, no country names.

=== SYSTEM LINKS AND ANNOTATIONS ===
Use thin arrows from each dimension to the central core and a subtle clockwise feedback loop connecting the five dimensions. Add short Chinese semantic labels on selected arrows: "技术积累", "制造落地", "链条整合", "组织支撑", "外部连接". Add one bottom annotation ribbon in Chinese: "初步观察：技术突围不是单点发明，而是系统能力提升。"

=== EVIDENCE BOUNDARY ===
Include a very small unobtrusive note in the lower-left corner of the diagram area: "来源：实践推文、公开资料、相关文献整理". Do not include company logos, real product photos, patent numbers, revenue figures, customer names, exact geographic labels, or claims of final proof.

=== STYLE SPECIFICATIONS ===
Use a restrained academic PowerPoint style with at least 70% white or near-white area. Palette: deep violet #3C3652 for key text and central border, violet #7561D6 for one accent path, blue #5199EA for engineering and R&D accents, muted cyan #68A4C6 for supply-chain/global accents, near-white #F7F8FB for very light panels, soft grey #D9DDE8 for dividers and secondary lines. Module fills must remain white or near-white; avoid saturated colored fills. Typography should imitate clean Chinese presentation fonts such as Microsoft YaHei or DengXian, with legible Chinese labels, no negative letter spacing. Line weights should be thin and consistent, with soft shadows only if extremely subtle. Keep all text horizontal and readable at slide scale. Avoid clutter, 3D realism, stock-photo style, glossy gradients, dark backgrounds, decorative bokeh, unrelated icons, exaggerated innovation slogans, and any invented numerical data.
```

## Self-check

- [x] information density: five modules each include subcontent.
- [x] source-fact constraints: only visualizes F7-F10 and theory links F13-F15 at framework level.
- [x] restrained palette: template-derived violet/blue/cyan palette with mostly white space.
- [x] grayscale readability: white modules, outlines, line-art thumbnails, and semantic arrows remain distinguishable.
- [x] no API/path/model parameters mixed into the prompt.

## Required Confirmation

用户已确认按此 prompt 调用 image2 生成 Slide 3 示意图。后续生成图只能作为解释性框架示意，不得作为企业事实证据图。
