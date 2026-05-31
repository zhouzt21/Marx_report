---
stage: deck_build
stage_status: confirmed
requires_confirmed:
  - ppt_production_brief
  - fact_ledger
  - defense_narrative
  - storyboard
  - speaker_notes_rehearsal
  - defense_qa_backup
  - asset_layout_plan
  - academic_figure_prompt_when_required
  - content_fidelity_qa
allowed_next_stage: ppt-render-qa-loop
confirmed_by: user/2026-05-31
created_at: 2026-05-31
---

# PPT Deck Build Manifest v1 Image2

## Outputs

- PPTX：`generated_pptx_test/marx_report_7_8_section_v1_image2.pptx`
- Base PPTX：`generated_pptx_test/marx_report_7_8_section_v0.pptx`
- Generated Slide 3 image：`assets/generated/slide3_image2_v0.png`
- Prompt artifact：`align/academic_figure_prompt_v0.md`
- Prompt fidelity check：`align/ppt_content_fidelity_qa_image2_slide3_v0.md`
- Apply script：`exp/apply_slide3_image2_v0.py`

## Change From v0

只替换 Slide 3 中部五维框架图区域。Slide 1、Slide 2、Slide 4 未改动；Slide 3 的标题、行动标题、页码、页脚来源、speaker notes 均保留。

## Counts

- Slide count：4
- Main slide count：4
- Backup slide count：0
- Notes slides：4

## Visual Route Outcomes

| Slide | Asset | Route outcome | Evidence status | Editability |
|---:|---|---|---|---|
| 1 | 方法闭环流程图 | unchanged from v0; editable PPT objects | source_derived_explanation | yes |
| 2 | 走访入口-公开资料-分析用途矩阵 | unchanged from v0; editable PPT objects | source_derived_explanation | yes |
| 3 | 五维技术突围系统协同示意图 | image2 generated academic framework diagram | source_derived_explanation, not evidence image | raster image; slide text remains editable |
| 4 | 参考文献与资料来源表 | unchanged from v0; editable PPT table | source_evidence | yes |

## Generated Image Provenance

- Generation tool route：OpenRouter ICU Image / `gpt-image-2`
- Prompt：`align/academic_figure_prompt_v0.md`
- Prompt status：confirmed by user/2026-05-31
- Image output：`assets/generated/slide3_image2_v0.png`
- Event log：`assets/generated/slide3_image2_v0.events.jsonl`
- Boundary：解释性框架图，不作为企业事实截图、数据图或证据图。

## Structural Validation

- opened_by_python_pptx：True
- slide_count：4
- aspect_ratio_16_9：True
- slide_3_picture_count：1
- notes_text_present：True, 4/4 slides readable by `python-pptx`
- forbidden_wording_absent：True
- placeholder_text_absent：True

## Known Render QA Focus

- Slide 3 生成图中文字较 v0 更密，需要 render QA 检查单页可读性。
- Slide 3 图内自带一行小来源，与 PPT 页脚来源形成双重标注；这是保守来源策略，不应遮挡主体。
- Slide 3 由 raster image 承载中部框架，后续若需要逐元素编辑，应回退到 v0 editable diagram 或重新用 PPT 形状重绘。
