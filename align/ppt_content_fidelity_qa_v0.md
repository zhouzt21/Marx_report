---
stage: content_fidelity_qa
stage_status: confirmed
requires_confirmed:
  - ppt_production_brief
  - fact_ledger
  - defense_narrative
  - storyboard
  - speaker_notes_rehearsal
  - defense_qa_backup
  - asset_layout_plan
  - academic_figure_prompt_when_required
allowed_next_stage: ppt-deck-build
confirmed_by: user/2026-05-31
created_at: 2026-05-31
qa_result: draft-pass-ready
---

# 内容保真 QA v0

## Scope

本阶段检查以下已确认产物是否与事实台账、材料清单和用户确认一致：

- `align/ppt_defense_narrative_v0.md`
- `align/PPT_storyboard_v0.md`
- `align/ppt_speaker_notes_rehearsal_v0.md`
- `align/ppt_defense_qa_backup_v0.md`
- `align/PPT_asset_audit_v0.md`
- `align/visual_enrichment_plan_v0.md`
- `align/ppt_layout_plan_v0.json`

未执行 PPTX 生成、图片生成、渲染 QA 或正文改写。

## Overall Result

结论：可进入 deck build 前的用户确认阶段。当前未发现 blocker 或 major 问题；发现 3 个 minor 风险，均已有后续 deck build/QA 处理建议。

## Pass Criteria Check

| 检查项 | 结果 | 证据 |
|---|---|---|
| 行动标题有事实或用户确认依据 | PASS | Slide 1 对应 F1/F3/F4/F16；Slide 2 对应 F2/F4-F12；Slide 3 对应 F7-F15；Slide 4 对应 F11-F16 |
| 结果、指标、数据、基线没有无来源扩展 | PASS | 主体页不放具体营收/专利数；年报只作为公开资料来源 |
| 视觉不把生成图当证据 | PASS | `requires_academic_figure_prompt: false`，全部为可编辑结构图/表格 |
| Q&A 不承诺未做实验或内部资料 | PASS | Q9 明确本部分不做量化实验；Q&A 禁止承诺未获取数据 |
| 备份页映射真实预期问题 | PASS | B1-B5 均对应 Q1-Q10 |
| relaxed assertion-evidence policy 已记录 exhibit 字段 | PASS | Storyboard 每页有 exhibit type、claim、so what、citation need |
| 主体口径保持谨慎 | PASS | Slide 2、讲稿、Q&A 均保留“走访入口 + 公开资料补充” |
| 英文文献不进入主体展示语言 | PASS | 英文文献只在参考文献页出现 |

## Issue Log

| Issue ID | Artifact / Anchor | Claim or decision under review | Source requirement | Severity | Owner stage | Recommended repair |
|---|---|---|---|---|---|---|
| CFQ-001 | `ppt_defense_narrative_v0.md` / Defense Thesis | “第 7-8 部分应证明……”措辞略强 | 已确认事实只支持“说明/支撑/形成初步分析”，不支持最终证明 | minor | deck build / copy polish | 生成 PPT 和最终群发文案时改为“应说明”或“应支撑” |
| CFQ-002 | `ppt_layout_plan_v0.json` / Slide 4 | `歌尔股份有限公司. 2025 年年度报告[R]. 2026.` 条目仍需最终核对 | F11 确认存在 2025 年报/摘要，但最终引用应以实际文件题录为准 | minor | content fidelity / deck build | Deck build 前保留该条，但在最终输出中标注“公开资料/年报”，必要时用巨潮资讯网版本核对 |
| CFQ-003 | `PPT_storyboard_v0.md` / Slide 2 asset note | 曾提到“如后续允许，可考虑截图” | 资产规划已确认不默认使用截图 | minor | asset/layout / deck build | Deck build 严格按已确认资产规划执行：不使用截图，全可编辑图表 |

## Slide-by-Slide Fidelity

### Slide 1

- Claim：研究方法与案例观察形成可验证闭环。
- Source basis：F1、F3、F4、F16。
- Fidelity：PASS。
- Notes：方法闭环为解释性图，不作为证据图；符合 relaxed policy。

### Slide 2

- Claim：多源互证避免案例分析停留在参观感想或企业介绍。
- Source basis：F2、F4、F5、F6、F7、F8、F11、F12、F12b。
- Fidelity：PASS。
- Notes：主体边界已明确：“以深圳歌尔泰克走访材料为入口，结合歌尔股份公开资料补充背景”。

### Slide 3

- Claim：技术突围依赖研发、工程、供应链、人才和全球布局的系统协同。
- Source basis：F7、F8、F9、F10、F13、F14、F15。
- Fidelity：PASS。
- Notes：讲稿和视觉计划均保留“初步观察/分析基础”降调，未写成最终模型。

### Slide 4

- Claim：参考文献为方法、理论和案例材料提供最低限度支撑。
- Source basis：F11、F12、F13、F14、F15、F16。
- Fidelity：PASS WITH MINOR NOTE。
- Notes：参考文献格式需在最终 PPT 生成时保持可编辑并可由组长合并；2025 年报条目需最终核对。

## Q&A Fidelity

| Q&A Area | Result | Notes |
|---|---|---|
| 案例选择 | PASS | 不夸大为完整企业评估 |
| 主体关系 | PASS | 明确数据不直接归属深圳歌尔泰克单体 |
| 五维框架 | PASS | 说成初步归纳，非最终模型 |
| 方法有效性 | PASS | 承认无量化实验，符合案例研究边界 |
| 英文文献 | PASS | 仅作为参考文献 |
| 企业宣传风险 | PASS | 已有降调和风险回答 |

## Visual / Asset Fidelity

- No generated image：PASS。
- No academic figure prompt required：PASS。
- Full editability：PASS by plan。
- Screenshot use：PASS, because confirmed asset plan says no default screenshot.
- Whole-slide image risk：PASS, explicitly prohibited.

## Content Fidelity Requirements For Deck Build

Deck build 阶段必须遵守：

1. Slide 2 必须保留主体口径，不得把“歌尔股份公开资料”直接写成“深圳歌尔泰克数据”。
2. Slide 3 必须使用“初步观察”“分析基础”等降调表达，不得写“最终模型/已证明”。
3. 不使用实践推文截图、年报截图或 AI 生成图。
4. 所有图表必须可编辑。
5. Slide 4 参考文献可独立保留，也可交给组长合并；但条目要可编辑。
6. 最终给群里的修改段落应将“证明”改为“说明/支撑/体现”，保持开题阶段口径。

## Repair Routing

无 blocker 或 major 需要回退。Minor issue 建议在 deck build 和最终文案整理时直接按本 QA 要求处理，无需回退前序阶段。

## User Confirmation Needed

请用户确认：

1. 是否接受本 QA 结果为 `draft-pass-ready`。
2. 是否同意 deck build 阶段按上述 6 条内容保真要求执行。
