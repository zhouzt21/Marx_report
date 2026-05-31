---
stage: render_qa
stage_status: needs_human_acceptance
requires_confirmed:
  - deck_build
allowed_next_stage: human_acceptance_or_repair
accepted_by:
created_at: 2026-06-01
pptx: generated_pptx_test/marx_report_7_8_section_v4_researched_slide2.pptx
render_method: PowerPoint COM
qa_result: render-pass-human-acceptance-pending
---

# PPT Render QA v4 Researched Slide 2

## Scope

本阶段复检根据调研和第 7-8 部分改写文本重做后的 v4：

- PPTX：`generated_pptx_test/marx_report_7_8_section_v4_researched_slide2.pptx`
- Revised text：`align/section_7_8_revised_text_v1.md`
- Rendered pages：`qa/template_v4_researched_slide2/rendered_pages/slide_001.png` 至 `slide_004.png`
- PDF：`qa/template_v4_researched_slide2/deck_render.pdf`
- Contact sheet：`qa/template_v4_researched_slide2/contact_sheet.png`

## Overall Result

结论：render QA 通过，等待用户人工接受。

Slide 2 已从“材料来源三栏”改为“材料入口—公开补强—分析产出”的证据链，更贴合第 7-8 部分修改稿。三栏正文、口径说明和来源行可读，未发现文本截断、明显越界、空白页、缺图或中文缺字。

## Visual QA

| Slide | Result | Notes |
|---:|---|---|
| 1 | PASS | 未改动；方法闭环保持模板风格。 |
| 2 | PASS | 新内容可读；三栏逻辑与改写文本一致；底部口径说明可辨认。 |
| 3 | PASS | 未改动；image2 框架图与模板页脚不冲突。 |
| 4 | PASS WITH MINOR NOTE | 未改动；参考文献页可读，仍建议合并前统一格式核对。 |

## Content QA

| Check | Result | Evidence |
|---|---|---|
| 与第 7-8 修改稿一致 | PASS | `align/section_7_8_revised_text_v1.md` 将第八部分收束为多源互证和五维框架。 |
| 外部资料口径稳妥 | PASS | Slide 2 标注集团公开数据不直接等同于单一走访主体。 |
| 参考来源可追溯 | PASS | 来源行覆盖实践推文、歌尔 2025 年报/摘要和核心理论文献。 |

## Residual Risks

| ID | Severity | Risk | Suggested handling |
|---|---|---|---|
| RQA-TPL4-001 | minor / final-merge check | 参考文献格式和 2025 年报题录需最终合并前按组内格式核对。 | 合并前统一到总 PPT 的参考文献格式。 |

## Stop Point

请用户选择：

1. 接受当前 v4 researched slide2 deck：回复“确认 v4，通过”。
2. 继续修复：指出具体页面或问题。

