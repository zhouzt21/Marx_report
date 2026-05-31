---
stage: render_qa
stage_status: pass
related_report: qa/ppt_render_qa_v0.md
repair_required_for_acceptance: false
created_at: 2026-05-31
---

# PPT Repair Backlog v0

## Summary

本 backlog 只记录 render QA 阶段发现的非阻断项。当前没有必须修复后才能接受的 blocker 或 major 问题。

## Items

| ID | Severity | Evidence | Owner stage | Suggested repair path | Human confirmation required |
|---|---|---|---|---|---|
| RQA-001 | minor / optional visual polish | `qa/rendered_pages/slide_003.png` | deck_build / layout | 若追求更干净视觉，可将 Slide 3 中心连线改为绕开中心文字，或把连线置于中心椭圆后并略微降低透明度。 | 是，仅当用户希望微调。 |
| RQA-002 | minor / final-merge bibliographic check | `qa/rendered_pages/slide_004.png` | content_fidelity / final_merge | 最终交给组长合并前，核对“歌尔股份有限公司. 2025 年年度报告[R]. 2026.”的实际题录和组内统一格式。 | 是，由最终合并者确认。 |

## Repair Routing

- 若用户接受当前 deck：无需修复，进入人工验收/交付。
- 若用户要求修复 RQA-001：回到 deck build/layout 微调后重新 render QA。
- 若用户要求处理 RQA-002：回到 content fidelity / reference formatting，核对题录后重新导出参考文献页。
