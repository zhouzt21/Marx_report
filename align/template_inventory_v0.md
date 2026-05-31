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

# PPT 模板清单 v0

## Template Source

- 文件：`2025nianduyanshiwengaomoban2-tongyongzhuti.pptx`
- 用途：作为局部 PPT 的风格参考和可复制版式来源。
- 直接绑定程度：中等。后续生成可编辑 PPTX 时优先借用其 16:9、紫蓝色、清华模板风格；不强制逐页复刻。

## Technical Inventory

| 项目 | 结果 |
|---|---|
| 幻灯片尺寸 | 16:9，`12192000 x 6858000` EMU |
| 模板页数 | 29 页 |
| slide layouts | 401 个布局 XML，数量较多，名称多数为空 |
| 主题字体 | `等线 Light`、`等线` |
| 主题颜色 | 黑白 + 紫蓝系，含 `3C3652`、`912C8D`、`7561D6`、`68A4C6`、`6A69B6`、`5199EA`、`5B84D8` 等 |
| 占位内容 | 多数页面为“添加标题/添加正文/输入图片”等占位文本 |
| 图片依赖 | 多页包含背景/装饰图片，后续需避免整页不可编辑化 |

## Candidate Template Slides

| 模板页 | 观察 | 适合用途 | 风险 |
|---|---|---|---|
| slide 11 | 正文+小标题结构 | 一般内容页，可用于方法闭环页的文本区 | 文字框较多，需控制密度 |
| slide 13/14 | 图文排版、关键词 | 适合证据矩阵或案例基础页 | 需避免套用图片占位导致视觉空洞 |
| slide 16/23 | 多模块正文结构 | 适合五维框架或多维分析 | 模块多，文字容易小 |
| slide 22 | 文字小结结构 | 适合参考文献或结论说明 | 需重绘为清晰表格 |
| slide 27/29 | 结束页 | 不用于局部 PPT 主体，除非组长需要单独结尾 | 汇报局部内容通常不需要结束页 |

## Design Constraints For This Deck

- 只生成第 7-8 部分局部 PPT，不做完整开题报告封面和结束页。
- 主体页保持中文，英文只在参考文献条目中出现。
- 页面优先全可编辑：形状、箭头、表格、文本框。
- 不使用 AI 生成图片。
- 不默认使用实践推文或年报截图；如后续确需截图，只能作为辅助素材并标注来源。
- 保留紫蓝模板气质，但避免整页过度花哨和信息遮挡。

## Template Risks

- 模板 master/layout 数量过多，自动匹配布局可能不稳定；后续 deck build 宜基于空白/近似布局手工放置可编辑元素。
- 占位文字多，需在生成后检查是否残留“添加正文”“XXX”等模板文本。
- 主题为紫蓝系，若使用大量同色块，页面会显得单调；后续应以白底、深色文字、少量紫蓝强调为主。
- CJK 字体应优先使用本机常见字体，如等线、微软雅黑；避免使用缺失字体。
