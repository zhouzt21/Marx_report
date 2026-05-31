---
stage: asset_layout_plan
stage_status: confirmed
requires_confirmed:
  - ppt_production_brief
  - fact_ledger
  - defense_narrative
  - storyboard
  - speaker_notes_rehearsal
  - defense_qa_backup
allowed_next_stage: ppt-content-fidelity-qa-stage
confirmed_by: user/2026-05-31
created_at: 2026-05-31
---

# PPT 资产审计 v0

## Asset Policy

- 默认不使用外部图片，不使用 AI 生成图。
- 主体页全部使用可编辑 PowerPoint 形状、表格、文本框和图标。
- 参考文献页使用可编辑表格。
- 实践推文和年报截图暂不进入主体页；如组长需要，可后续作为备份或附录素材。

## Slide-Level Asset Decisions

| Slide | 视觉需求 | 决策 | visual_route | evidence_status | generation_allowed | 理由 |
|---:|---|---|---|---|---|---|
| 1 | 方法闭环流程图 | redraw as editable | local_editable_diagram | source_derived_explanation | no | 方法来自已确认事实台账，适合用 PPT 箭头和节点重绘 |
| 2 | 三栏证据矩阵 | redraw as editable | local_editable_diagram | source_derived_explanation | no | 需要表达材料来源和分析用途，不需要截图 |
| 3 | 五维分析框架 | redraw as editable | local_editable_diagram | source_derived_explanation | no | 属于解释性框架，使用可编辑形状最稳 |
| 4 | 参考文献表 | redraw as editable | local_editable_table | source_evidence | no | 完整条目需可编辑，方便组长合并 |
| B1-B5 | 备份页表格/框架 | omit from main, keep as optional editable backups | local_editable_diagram/table | source_derived_explanation | no | 当前不进主讲 PPT，后续可选 |

## Source Assets

| 来源 | 是否使用为视觉资产 | 用途 | 风险 |
|---|---|---|---|
| `show_705035364_1780137861277.pdf` | 暂不截图 | 事实依据、必要时作为备份素材 | PDF 来源和版权/授权需谨慎；截图可能降低可编辑性 |
| `2025nianduyanshiwengaomoban2-tongyongzhuti.pptx` | 使用风格和布局，不直接嵌入整页图片 | 16:9、配色、字体、页面风格 | 占位文本和装饰图形残留 |
| 歌尔 2025 年报/摘要 | 不截图，作为参考文献和事实来源 | 公开资料补强 | 最终引用信息需核对 |
| 文献网页/检索结果 | 不截图 | 参考文献条目 | 不应把搜索结果当作最终引用格式 |

## Editability Tradeoffs

- 选择全可编辑图表牺牲一点“真实素材感”，但便于组长合并和修改。
- 不使用实践推文截图可以降低版权和清晰度风险。
- 不使用年报截图可以避免页内信息过密。

## QA Checklist For Assets

- 每页图表中的文字都能编辑。
- 无模板占位文本残留。
- 无未授权图片或截图。
- 来源线与参考文献页一致。
- 图表中的节点名称与 fact ledger/storyboard 一致。
