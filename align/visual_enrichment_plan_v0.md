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
requires_academic_figure_prompt: false
required_prompt_artifact:
---

# 视觉强化计划 v0

## Summary

本局部 PPT 不需要 AI 生成学术图片，也不需要 `academic-figure-prompt`。视觉强化以可编辑结构图为主：

1. 方法闭环流程图。
2. 三栏证据矩阵。
3. 五维技术突围框架图。
4. 参考文献分类表。

## Routing Decisions

| Slide | Visual | Route | Reason | Fallback |
|---:|---|---|---|---|
| 1 | 方法闭环流程图 | local_editable_diagram | 适合用形状和箭头表达，来源已确认 | 若拥挤，改为“方法-材料-产出”三列表 |
| 2 | 三栏证据矩阵 | local_editable_diagram/table | 能清楚区分走访入口、公开资料、分析用途 | 若空间不足，改为两栏“材料来源/分析用途” |
| 3 | 五维框架图 | local_editable_diagram | 体现系统协同，避免大段文字 | 若节点重叠，改为 5 张小卡片 |
| 4 | 参考文献表 | local_editable_table | 便于组长合并和统一格式 | 若总 PPT 有参考页，本页删除并交付条目 |

## No-Generation Decision

- `requires_academic_figure_prompt: false`
- 不调用 `openrouter-icu-image`。
- 不使用装饰性 AI 图片。
- 不生成证据图、数据图或年报截图替代真实资料。

## Visual Tone

- 学术、克制、可合并。
- 白底为主，紫蓝作强调。
- 图表承载结构关系，不做装饰性大图。

## Content Fidelity Notes

- Slide 2 必须保留主体口径：“以深圳歌尔泰克走访材料为入口，结合歌尔股份公开资料补充背景”。
- Slide 3 必须保留降调：“初步观察/分析基础”，不要写成“最终模型”。
- Slide 4 的参考文献条目后续需统一格式。
