---
stage: render_qa
stage_status: pass
related_report: qa/template_v2/ppt_render_qa_v2_template.md
repair_required_for_acceptance: false
created_at: 2026-06-01
---

# PPT Repair Backlog v2 Template

## Summary

当前 v2 template 版本没有必须修复后才能接受的 blocker 或 major 问题。以下为非阻断优化项。

## Items

| ID | Severity | Evidence | Owner stage | Suggested repair path | Human confirmation required |
|---|---|---|---|---|---|
| RQA-TPL2-001 | minor / optional | `qa/template_v2/rendered_pages/slide_004.png` | final_merge / deck_build | 若展示屏较小，可删除局部参考页并把参考文献交给组长合并，或拆成两页参考文献。 | 是 |
| RQA-TPL2-002 | minor / final-merge bibliographic check | `qa/template_v2/rendered_pages/slide_004.png` | content_fidelity / final_merge | 最终合并前核对“歌尔股份有限公司. 2025 年年度报告[R]. 2026.”实际题录和组内格式。 | 是 |

## Repair Routing

- 若用户接受当前 deck：无需修复，进入人工验收/交付。
- 若用户要求修复 RQA-TPL2-001：回到 deck build 或 final merge 处理参考页。
- 若用户要求处理 RQA-TPL2-002：回到 content fidelity / reference formatting 核对题录。
