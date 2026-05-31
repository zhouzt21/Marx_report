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
---

# PPT Deck Build Manifest v0

Generated at: `2026-05-31 23:18:35`

## Outputs

- PPTX: `generated_pptx_test/marx_report_7_8_section_v0.pptx`
- Build script: `exp/build_marx_report_deck_v0.py`
- Manifest: `align/ppt_deck_build_manifest_v0.md`

## Counts

- Slide count: 4
- Main slide count: 4
- Backup slide count: 0
- Backup policy: B1-B5 remain planned optional in `align/ppt_defense_qa_backup_v0.md` and `align/ppt_layout_plan_v0.json`; not inserted into this main draft because the user requested a 4-slide clean deck.

## Notes Insertion

- Status: inserted into PowerPoint notes pane via `python-pptx` notes slide API.
- Notes source: `align/ppt_speaker_notes_rehearsal_v0.md`
- Limitation: notes were inserted structurally but not render-verified in PowerPoint, because render QA/COM was explicitly out of scope for this lane.

## Confirmed Source Paths

- `align/ppt_production_brief_v0.md`
- `align/fact_ledger_v0.md`
- `align/ppt_defense_narrative_v0.md`
- `align/PPT_storyboard_v0.md`
- `align/ppt_speaker_notes_rehearsal_v0.md`
- `align/ppt_defense_qa_backup_v0.md`
- `align/template_inventory_v0.md`
- `align/template_design_rules_v0.md`
- `align/PPT_asset_audit_v0.md`
- `align/visual_enrichment_plan_v0.md`
- `align/ppt_layout_plan_v0.json`
- `align/PPT_asset_manifest_v0.csv`
- `align/ppt_content_fidelity_qa_v0.md`

## Content Fidelity QA

- Source: `align/ppt_content_fidelity_qa_v0.md`
- Status: confirmed; `qa_result: draft-pass-ready`.
- Applied constraints: Slide 2 keeps entity-boundary wording; Slide 3 keeps `初步观察/分析基础`; forbidden wording `已证明/最终模型` is absent from generated slide text.

## Template / Design Rules

- Template source read: `2025nianduyanshiwengaomoban2-tongyongzhuti.pptx`
- Template design rules: `align/template_design_rules_v0.md`, status confirmed.
- Direct template master reuse: not used. `python-pptx` could read template size and slide count, but layout enumeration hit an internal layout relationship error; deck was generated as a clean 16:9 editable deck using the confirmed colors, typography, and layout archetypes.

## Layout / Template Mapping

| Slide | Storyboard item | Layout archetype | Template/source mapping | Visual route |
|---:|---|---|---|---|
| 1 | 研究方法：多源互证闭环 | action_title_plus_process | template style reference; editable redraw | local_editable_diagram |
| 2 | 案例基础：以深圳歌尔泰克走访材料为入口 | action_title_plus_three_column_matrix | template style reference; editable redraw | local_editable_diagram/table |
| 3 | 初步观察：技术突围的五个维度 | action_title_plus_five_dimension_framework | template style reference; editable redraw | local_editable_diagram |
| 4 | 参考文献与资料来源 | references_table | template style reference; editable table | local_editable_table |

## Visual Route Outcomes

| Slide | Asset | Route outcome | Evidence status | Editability |
|---:|---|---|---|---|
| 1 | 方法闭环流程图 | local_editable_diagram; generated as editable PPT objects | source_derived_explanation | yes |
| 2 | 走访入口-公开资料-分析用途矩阵 | local_editable_diagram; generated as editable PPT objects | source_derived_explanation | yes |
| 3 | 技术突围五维框架 | local_editable_diagram; generated as editable PPT objects | source_derived_explanation | yes |
| 4 | 参考文献与资料来源表 | local_editable_table; generated as editable PPT objects | source_evidence | yes |

## Assets Used

- No external raster assets embedded.
- No practice-post screenshots, annual-report screenshots, AI-generated images, or whole-slide images used.
- All slide bodies are editable PowerPoint text boxes, shapes, connectors, and table cells.

## Generated Image Provenance

- None. `align/visual_enrichment_plan_v0.md` marks `requires_academic_figure_prompt: false`; OpenRouter ICU Image was not called.

## Generation Log

- slide_1: editable closed-loop process diagram; notes inserted
- slide_2: editable three-column evidence matrix; entity-boundary wording preserved; notes inserted
- slide_3: editable five-dimension framework; initial-observation wording preserved; notes inserted
- slide_4: editable reference table; English appears only in reference row; notes inserted

## Structural Validation

- aspect_ratio_16_9: True
- file_exists: True
- forbidden_wording_absent: True
- notes_slides_present: True
- opened_by_python_pptx: True
- placeholder_text_absent: True
- slide_2_entity_boundary: True
- slide_3_initial_observation: True
- slide_count: 4

## Known Pre-render Risks

- Chinese font substitution may change wrapping on another machine.
- Reference slide uses 10.5 pt text; readable structurally, but final visual acceptance requires render QA.
- Template master/layout was not directly reused due to `python-pptx` layout relationship instability; visual style follows confirmed rules instead.
- Speaker notes were inserted but not inspected through PowerPoint UI in this lane.

## Required Handoff

- Next stage: `ppt-render-qa-loop`.
- This draft is not self-confirmed and should be handed to render QA before acceptance.
