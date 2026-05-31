---
stage: render_qa
stage_status: pass
related_report: qa/image2_v1/ppt_render_qa_v1_image2.md
repair_required_for_acceptance: false
created_at: 2026-05-31
---

# PPT Repair Backlog v1 Image2

## Summary

当前 v1 image2 版本没有必须修复后才能接受的 blocker 或 major 问题。以下仅为非阻断优化项。

## Items

| ID | Severity | Evidence | Owner stage | Suggested repair path | Human confirmation required |
|---|---|---|---|---|---|
| RQA-IMG2-001 | minor / optional | `qa/image2_v1/rendered_pages/slide_003.png` | image generation / deck build | 若希望投影时更清爽，可重生成低密度版本，减少内部小标签，只保留五个维度大标题和关键图标。 | 是 |
| RQA-IMG2-002 | minor / optional | `qa/image2_v1/rendered_pages/slide_003.png` | image generation / layout | 若嫌来源重复，可裁剪掉生成图内左下角小来源，保留 PPT 页脚来源线。 | 是 |
| RQA-IMG2-003 | minor / final-merge bibliographic check | `qa/image2_v1/rendered_pages/slide_004.png` | content_fidelity / final_merge | 最终交给组长合并前，核对“歌尔股份有限公司. 2025 年年度报告[R]. 2026.”的实际题录和组内统一格式。 | 是 |

## Repair Routing

- 若用户接受当前 deck：无需修复，进入人工验收/交付。
- 若用户要求修复 RQA-IMG2-001 或 RQA-IMG2-002：回到 image generation / layout 后重新 render QA。
- 若用户要求处理 RQA-IMG2-003：回到 content fidelity / reference formatting，核对题录后重新导出参考文献页。
