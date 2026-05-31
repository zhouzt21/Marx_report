---
stage: render_qa
stage_status: pass
requires_confirmed:
  - deck_build
allowed_next_stage: human_acceptance_or_repair
accepted_by:
created_at: 2026-05-31
pptx: generated_pptx_test/marx_report_7_8_section_v0.pptx
render_method: PowerPoint COM
qa_result: render-pass-human-acceptance-pending
---

# PPT Render QA v0

## Scope

本阶段检查已确认 deck build 产物：

- PPTX：`generated_pptx_test/marx_report_7_8_section_v0.pptx`
- deck build manifest：`align/ppt_deck_build_manifest_v0.md`
- 渲染输出：`qa/rendered_pages/slide_001.png` 至 `qa/rendered_pages/slide_004.png`
- PDF 备查：`qa/deck_render.pdf`
- contact sheet：`qa/contact_sheet.png`

## Overall Result

结论：render QA 通过，等待人工最终接受。

未发现阻断项或 major 问题：无空白页、无内容越界、无明显标题重叠、无中文缺字、无图片缺失、无不可读图表。发现 2 个 non-blocking / minor follow-up，已记录到 `qa/ppt_repair_backlog_v0.md`，不影响当前 deck 作为组内合并稿使用。

## Render Evidence

| Item | Result | Evidence |
|---|---|---|
| PowerPoint COM 渲染 | PASS | 4 页均导出为 PNG |
| PDF 导出 | PASS | `qa/deck_render.pdf` |
| Contact sheet | PASS | `qa/contact_sheet.png` |
| Slide count | PASS | 4 页，与 deck build manifest 一致 |
| Notes evidence | PASS | manifest 记录 notes 已插入；COM 读取到 4 个 notes slide |

## Slide Visual QA

| Slide | Render check | Result | Notes |
|---:|---|---|---|
| 1 | 标题、行动标题、方法闭环图、页脚来源线 | PASS | 字体显示正常，流程节点间距充足，无截断。 |
| 2 | 三栏矩阵、主体口径提示、页脚来源线 | PASS | “走访入口 + 公开资料补充”口径清楚，正文可读。 |
| 3 | 五维框架、中心节点、so what 提示 | PASS WITH MINOR NOTE | 中心节点连线略穿过文字，但文字仍可读；可选优化见 backlog。 |
| 4 | 参考文献表、支撑点列、最终核对注释 | PASS | 参考文献页可读；2025 年报条目仍按前序 QA 保留最终题录核对提醒。 |

## Academic QA Checklist

| Check | Result | Evidence / comment |
|---|---|---|
| 每个内容页有行动标题 | PASS | Slides 1-4 均有明确判断句或功能句。 |
| ghost-deck sequence 能讲清论证 | PASS | 方法闭环 -> 案例入口 -> 五维观察 -> 参考来源。 |
| 外部资料有来源或引用政策 | PASS | 主体页有短来源线，Slide 4 有完整参考文献页。 |
| exhibit 有清楚 so what | PASS | Slides 1-3 均有底部总结句或路径提示。 |
| 借用来源时存在参考文献页 | PASS | Slide 4 为参考文献与资料来源。 |
| 最后一页不是空白或泛泛感谢页 | PASS | 最后一页为资料来源页，适合交给组长合并。 |
| 正文和表格可读 | PASS | 渲染图中正文、表格和页脚均可辨读。 |
| backup/appendix 处理符合确认策略 | PASS | deck manifest 记录 0 张 backup；B1-B5 保留为可选计划，不进入主讲 4 页。 |
| 生成视觉未被当作证据 | PASS | 未使用 AI 生成图或外部截图；图形均为可编辑结构图。 |
| 模板设计规则 | PASS WITH MINOR NOTE | 色彩、字号、安全边界整体符合；Slide 3 连线可选微调。 |

## Notes And Backup Evidence

- Speaker notes：`align/ppt_deck_build_manifest_v0.md` 记录 4 页 notes 已通过 `python-pptx` 插入 PowerPoint notes pane；本阶段用 PowerPoint COM 读取到 4 个 notes slide，字符数分别约为 805、859、913、609。
- Backup slides：`align/ppt_defense_qa_backup_v0.md` 规划 B1-B5 作为 Q&A/appendix 备份，但 deck build manifest 明确主讲稿为 4 页、0 张 backup；此处理符合用户此前确认的“干净 4 页主体”策略。

## Blocking Failure Review

未发现以下阻断问题：

- 标题/副标题重叠
- 正文截断或明显越界
- 图表、表格、公式不可读
- 严重拥挤
- CJK 缺字或错误字体替换导致不可读
- 空白页
- 缺失图片或资产
- 备份页误混入主讲流程
- 未标注来源的证据截图或生成图

## Residual Risks

| ID | Severity | Risk | Status |
|---|---|---|---|
| RQA-001 | minor / optional | Slide 3 中心连线略穿过中心文字 | 不阻断，可按需回退 deck build 做视觉微调。 |
| RQA-002 | minor / final-merge check | Slide 4 的 2025 年报题录需在最终合并前按组内格式核对 | 不属于渲染失败，建议最终合并时核对。 |

## Stop Point

请用户选择：

1. 接受当前 deck：回复“确认 render QA，通过”。
2. 回退修复：指定 `RQA-001`、`RQA-002` 或新的页面问题，再进入对应修复阶段。
