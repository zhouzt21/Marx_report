---
stage: render_qa
stage_status: pass
requires_confirmed:
  - deck_build
allowed_next_stage: human_acceptance_or_repair
accepted_by:
created_at: 2026-05-31
pptx: generated_pptx_test/marx_report_7_8_section_v1_image2.pptx
render_method: PowerPoint COM
qa_result: render-pass-human-acceptance-pending
---

# PPT Render QA v1 Image2

## Scope

本阶段复检 image2 重绘后的 PPTX：

- PPTX：`generated_pptx_test/marx_report_7_8_section_v1_image2.pptx`
- Generated image：`assets/generated/slide3_image2_v0.png`
- Rendered pages：`qa/image2_v1/rendered_pages/slide_001.png` 至 `slide_004.png`
- PDF：`qa/image2_v1/deck_render.pdf`
- Contact sheet：`qa/image2_v1/contact_sheet.png`

## Overall Result

结论：render QA 通过，等待人工最终接受。

Slide 3 已成功替换为 image2 生成的五维框架示意图。渲染结果未发现空白页、标题/副标题重叠、内容越界、中文缺字、图片缺失或未确认数据。Slide 3 的中部生成图信息密度高于 v0，缩略图下小字偏小，但在单页 1920x1080 渲染中可读，记为 minor follow-up，不阻断当前交付。

## Render Evidence

| Item | Result | Evidence |
|---|---|---|
| PowerPoint COM 渲染 | PASS | 4 页 PNG 已导出 |
| PDF 导出 | PASS | `qa/image2_v1/deck_render.pdf` |
| Contact sheet | PASS | `qa/image2_v1/contact_sheet.png` |
| Slide count | PASS | 4 页 |
| Notes evidence | PASS | `python-pptx` 可读取 4 页 notes 正文，字符数约 805、859、913、609 |
| Slide 3 image insertion | PASS | Slide 3 有 1 张 raster image，标题、行动标题、页脚仍为 PPT 文本 |

## Slide Visual QA

| Slide | Result | Notes |
|---:|---|---|
| 1 | PASS | 未改动；方法闭环图正常。 |
| 2 | PASS | 未改动；三栏矩阵和主体口径清楚。 |
| 3 | PASS WITH MINOR NOTE | image2 图未压住标题、页码或页脚；生成图内中文标签基本清楚；局部小字偏小但不影响主讲理解。 |
| 4 | PASS | 未改动；参考文献表可读，年报题录仍需最终合并前核对。 |

## Academic / Fidelity QA

| Check | Result | Evidence / comment |
|---|---|---|
| 生成图与确认 prompt 一致 | PASS | 五维结构、系统协同、降调说明均存在。 |
| 不新增企业事实或数据 | PASS | 未出现营收、专利数、客户名、真实 logo、地图坐标或实拍证据。 |
| 不把生成图当证据 | PASS | 图内与页脚均标注来源整理口径，报告中定义为解释性框架。 |
| 保留开题阶段谨慎口径 | PASS | Slide 3 仍使用“初步观察”，无“已证明/最终模型”。 |
| 参考来源可见 | PASS | Slide 3 页脚保留；图内也有小来源注记。 |
| 可编辑性边界清楚 | PASS WITH NOTE | 中部图为 raster，不可逐元素编辑；其他页面和 Slide 3 文本仍可编辑。 |

## Residual Risks

| ID | Severity | Risk | Suggested handling |
|---|---|---|---|
| RQA-IMG2-001 | minor | Slide 3 生成图内部小标签比 v0 更密，远距离投影时可能不适合逐字阅读。 | 主讲时只读五个大标题和底部结论；若老师要求极简，可回退 v0 可编辑图或再生成低密度版本。 |
| RQA-IMG2-002 | minor | Slide 3 图内来源小字与 PPT 页脚来源重复。 | 不阻断；若嫌重复，可后续裁剪图片底部来源小字或重新生成无内嵌来源版本。 |
| RQA-IMG2-003 | minor / final-merge check | Slide 4 的 2025 年报题录仍需最终合并前核对。 | 交给组长合并前统一参考文献格式。 |

## Stop Point

请用户选择：

1. 接受当前 v1 image2 deck：回复“确认 v1 image2，通过”。
2. 回退修复：指定 `RQA-IMG2-001`、`RQA-IMG2-002`、`RQA-IMG2-003` 或新的页面问题。
