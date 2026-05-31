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
confirmed_by: user-requested-template-repair/2026-06-01
---

# PPT Deck Build Manifest v2 Template

Generated at: `2026-06-01 00:17:01`

## Outputs

- PPTX: `generated_pptx_test/marx_report_7_8_section_v2_template.pptx`
- Build script: `exp/build_marx_report_deck_v2_template.py`
- Manifest: `align/ppt_deck_build_manifest_v2_template.md`
- Source template: `2025nianduyanshiwengaomoban2-tongyongzhuti.pptx`

## Template Background Selection

| Deck slide | Template slide used | Reason |
|---:|---:|---|
| 1 | 11 | 清华模板正文页，适合方法闭环内容重排 |
| 2 | 13 | 图文/双区块模板页，适合案例材料矩阵 |
| 3 | 23 | 中心图+四周说明模板页，适合五维框架图 |
| 4 | 26 | 时间线/总结类模板页，适合参考文献表格改造 |

## Change From v1 Image2

- 直接基于用户提供模板的候选页生成新 PPT，不再只手工套用配色。
- 保留模板的顶部 logo、紫色标题线、淡灰背景纹理和正文页风格。
- 删除模板占位文本和图片占位内容，重排本项目实际内容。
- Slide 3 继续使用已确认的 image2 五维框架图。

## Counts

- Slide count: 4
- Main slide count: 4
- Backup slide count: 0
- Notes slides: 4

## Generated Image Provenance

- Slide 3 image: `assets/generated/slide3_image2_v0_crop_source.png`
- Prompt artifact: `align/academic_figure_prompt_v0.md`, status confirmed.
- Boundary: explanatory framework image, not evidence image.

## Structural Validation

- aspect_ratio_16_9: True
- file_exists: True
- forbidden_wording_absent: True
- notes_chars: [805, 859, 913, 609]
- notes_slides_present: True
- opened_by_python_pptx: True
- placeholder_text_absent: True
- slide_2_entity_boundary: True
- slide_3_initial_observation: True
- slide_count: 4
- template_header_logo_present: True

## Known Pre-render Risks

- 使用模板页后整体风格更统一，但仍需 PowerPoint COM render QA 检查是否有占位文本残留、字体替换、表格可读性和图片压边。
- Slide 3 中部图为 raster image，不可逐元素编辑；标题、行动标题、页脚与备注仍为可编辑文本。

## Required Handoff

- Render QA completed in `qa/template_v2/ppt_render_qa_v2_template.md`; final user acceptance is still required.
