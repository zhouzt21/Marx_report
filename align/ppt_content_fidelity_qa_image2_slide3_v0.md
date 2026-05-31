---
stage: content_fidelity_qa
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
allowed_next_stage: ppt-deck-build
confirmed_by: user/2026-05-31
created_at: 2026-05-31
scope: slide_3_image2_redraw_only
---

# Slide 3 Image2 Content Fidelity Quick Check v0

## Scope

本快检只覆盖用户确认后的 Slide 3 image2 重绘请求，不重做全 deck 内容保真 QA。

- Prompt artifact：`align/academic_figure_prompt_v0.md`
- Target slide：Slide 3 `初步观察：技术突围的五个维度`
- Existing render issue：`qa/ppt_repair_backlog_v0.md` / `RQA-001`

## Result

结论：可调用 image2 生成解释性框架示意图。

## Checks

| Check | Result | Evidence / boundary |
|---|---|---|
| Prompt 已经用户确认 | PASS | `academic_figure_prompt_v0.md` status 已更新为 confirmed |
| 视觉化主张有事实锚点 | PASS | F7-F10 支撑案例观察，F13-F15 支撑理论解释 |
| 不新增数值或企业事实 | PASS | prompt 明确禁止专利数、营收、客户名、真实 logo、地图坐标 |
| 不把生成图当证据 | PASS | prompt 与后续 PPT 只把图作为解释性框架图 |
| 保留开题阶段降调 | PASS | prompt 使用“初步观察”“不是最终证明”的边界 |
| PPT 可编辑性风险已记录 | PASS | raster image 不逐元素可编辑，但标题、行动标题、页脚和备注保留为 PPT 文本 |

## Required Build Constraints

1. 只替换 Slide 3 中部五维框架图区域。
2. Slide 3 标题、行动标题、底部注释、页脚来源、speaker notes 必须保留为可编辑 PPT 文本。
3. 图片不得覆盖页脚来源或页码。
4. 生成图若出现乱码、英文残留、伪数据、logo 或无关图形，必须重新生成或回退可编辑图。
