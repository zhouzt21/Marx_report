---
stage: render_qa
stage_status: pass
requires_confirmed:
  - deck_build
allowed_next_stage: human_acceptance_or_repair
accepted_by:
created_at: 2026-06-01
pptx: generated_pptx_test/marx_report_7_8_section_v2_template.pptx
render_method: PowerPoint COM
qa_result: render-pass-human-acceptance-pending
---

# PPT Render QA v2 Template

## Scope

本阶段复检基于用户模板页重做后的 v2：

- PPTX：`generated_pptx_test/marx_report_7_8_section_v2_template.pptx`
- Deck build manifest：`align/ppt_deck_build_manifest_v2_template.md`
- Rendered pages：`qa/template_v2/rendered_pages/slide_001.png` 至 `slide_004.png`
- PDF：`qa/template_v2/deck_render.pdf`
- Contact sheet：`qa/template_v2/contact_sheet.png`

## Overall Result

结论：render QA 通过，等待用户人工接受。

v2 已从用户提供的模板中选用第 11、13、23、26 页作为基础页，保留清华 logo、紫色标题线、淡灰斜纹背景和模板式白色内容区。相比 v1，统一风格明显增强。未发现占位文字残留、空白页、标题重叠、内容越界、图片缺失或中文缺字。

## Template Mapping

| Deck slide | Template slide | Result |
|---:|---:|---|
| 1 | 11 | PASS，方法闭环置入模板正文内容区。 |
| 2 | 13 | PASS，案例矩阵沿用模板顶部与淡背景风格。 |
| 3 | 23 | PASS，五维框架图置入中心框架页，已裁掉图内重复来源。 |
| 4 | 26 | PASS，参考文献表置入模板页，保留底部注释和来源。 |

## Visual QA

| Slide | Result | Notes |
|---:|---|---|
| 1 | PASS | 模板标题线、logo、背景纹理统一；方法链条可读。 |
| 2 | PASS | 三栏矩阵与模板风格协调；主体口径保留。 |
| 3 | PASS | image2 框架图未遮挡标题、页脚和页码；底部来源只保留 PPT 页脚。 |
| 4 | PASS WITH MINOR NOTE | 参考文献表单页可读，缩略图下偏小；最终合并前仍需核对年报题录。 |

## Academic / Fidelity QA

| Check | Result | Evidence / comment |
|---|---|---|
| 行动标题完整 | PASS | 4 页均保留行动标题或功能句。 |
| 论证顺序完整 | PASS | 方法闭环 -> 案例入口 -> 五维观察 -> 参考来源。 |
| 来源策略可见 | PASS | 每页保留页脚来源，Slide 4 有完整参考页。 |
| 生成图未被当作证据 | PASS | Slide 3 仍定义为解释性框架图，无 logo、数据、客户名或实拍证据。 |
| 占位文本清除 | PASS | 结构验证和渲染检查均未发现“添加标题/添加正文/输入图片”等模板占位。 |
| Speaker notes | PASS | `python-pptx` 可读取 4 页 notes 正文，字符数约 805、859、913、609。 |

## Residual Risks

| ID | Severity | Risk | Suggested handling |
|---|---|---|---|
| RQA-TPL2-001 | minor | Slide 4 参考文献文字在缩略图下偏小，但单页可读。 | 若最终展示屏幕较小，可交给组长合并到总参考页，或把局部参考页删去。 |
| RQA-TPL2-002 | minor / final-merge check | 2025 年报题录仍需最终合并前核对。 | 合并前按组内统一格式核对题录。 |

## Stop Point

请用户选择：

1. 接受当前 v2 template deck：回复“确认 v2 模板版，通过”。
2. 继续修复：指出具体页面或指定 `RQA-TPL2-001` / `RQA-TPL2-002`。
