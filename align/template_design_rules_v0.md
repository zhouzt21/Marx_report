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

# 模板设计规则 v0

## Canvas

- 尺寸：16:9 widescreen。
- 安全边界：左右至少 0.45 inch，上下至少 0.35 inch。
- 页脚：如使用页码，保持小号浅灰；不抢正文。

## Typography

- 中文标题：等线/微软雅黑，28-34 pt。
- 行动标题或页内核心句：20-24 pt。
- 正文：16-20 pt；参考文献页可降到 10.5-12 pt，但必须可读。
- 字重：标题半粗，正文常规；避免整页加粗。
- 字距：默认，不使用负字距。

## Color

- 主色：深紫蓝 `#3C3652` 或深蓝灰。
- 强调色：`#7561D6`、`#5199EA`、`#68A4C6`。
- 背景：优先白色或极浅灰，不做大面积深色底。
- 禁止：整页大面积紫蓝渐变、低对比浅紫文字、多个高饱和色并列。

## Layout Archetypes

| 页面类型 | 推荐结构 |
|---|---|
| 方法闭环 | 顶部行动标题 + 中部横向流程/闭环图 + 底部材料来源小注 |
| 证据矩阵 | 顶部行动标题 + 三栏矩阵 + 右下角 so what 注释 |
| 五维框架 | 顶部行动标题 + 中心辐射或五宫格框架 + 一句理论连接 |
| 参考文献 | 顶部标题 + 两列表格，左侧文献，右侧支撑点 |
| 备份页 | 与主体页同风格，但放 appendix/hidden，不计入主讲 |

## Citation Rules

- 主体页允许短来源线，如“来源：实践推文；歌尔公开资料；相关文献整理”。
- 不在主体页堆完整参考文献。
- 完整条目放参考文献页或交给组长合并。

## Forbidden Patterns

- 整页截图或整页图片化。
- 截图未标注来源。
- 大段正文超过 6 行。
- 用“全球前列”“突破封锁”等无强出处的绝对化词作为页面标题。
- 模板占位文本残留。
- 备份页混入主讲流程导致超时。

## Render QA Risks

- 中文字体替换导致换行变化。
- 参考文献页文字过小。
- 五维框架节点文字过长导致重叠。
- 紫蓝色块过多时对比不足。
- 从模板复制的装饰图形可能遮挡可编辑元素。
