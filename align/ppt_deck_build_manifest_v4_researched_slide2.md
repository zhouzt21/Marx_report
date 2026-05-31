---
stage: deck_build
stage_status: draft
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
confirmed_by:
created_at: 2026-06-01
---

# PPT Deck Build Manifest v4 Researched Slide 2

## Outputs

- PPTX：`generated_pptx_test/marx_report_7_8_section_v4_researched_slide2.pptx`
- Base PPTX：`generated_pptx_test/marx_report_7_8_section_v3_template_align.pptx`
- Revised text：`align/section_7_8_revised_text_v1.md`
- Apply script：`exp/apply_slide2_researched_content_v4.py`

## Change From v3

根据重新调研和第 7-8 部分改写文本，重做 Slide 2 内容口径：

- 标题由“以深圳歌尔泰克走访材料为入口”调整为“方法与材料如何进入第八部分”。
- 三栏由泛化的“走访入口 / 公开资料 / 分析用途”调整为“材料入口 / 公开补强 / 分析产出”。
- 增加底部口径说明：以深圳歌尔泰克走访材料为入口，结合歌尔股份公开资料补充背景；集团公开数据不直接等同于单一走访主体。
- 更新 Slide 2 notes，强调第二页如何支撑第八部分正文改写。

其余页面、image2 图、参考文献页和整体模板背景未改动。

## Structural Validation

- Slide count：4
- Notes slides：4
- Speaker notes：preserved and Slide 2 updated
- Render QA：`qa/template_v4_researched_slide2/ppt_render_qa_v4_researched_slide2.md`

## Known Pre-Acceptance Status

- v4 已完成 PowerPoint COM 渲染。
- 当前为 draft，等待用户确认是否接受新版 Slide 2。

