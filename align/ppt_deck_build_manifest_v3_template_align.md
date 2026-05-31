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
confirmed_by: user-requested-slide2-align/2026-06-01
created_at: 2026-06-01
---

# PPT Deck Build Manifest v3 Template Align

## Outputs

- PPTX：`generated_pptx_test/marx_report_7_8_section_v3_template_align.pptx`
- Base PPTX：`generated_pptx_test/marx_report_7_8_section_v2_template.pptx`
- Apply script：`exp/apply_slide2_center_align_v3.py`

## Change From v2

只调整 Slide 2 三个白色内容框中的正文对齐：

- 水平居中。
- 垂直居中。
- 稍微收紧行距与框内边距。

其余页面、内容、参考文献、image2 图和 speaker notes 未改动。

## Structural Validation

- Slide count：4
- Notes slides：4
- Speaker notes：preserved
- Render QA：`qa/template_v3_align/ppt_render_qa_v3_template_align.md`
