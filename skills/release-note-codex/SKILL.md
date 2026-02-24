---
name: release-note
description: 生成软件 Release Note（中文，Feishu/Markdown）。当用户提到 release note、更新记录、发布记录、版本发布说明、飞书发布文档、回滚流程、模块负责人或模块级变更汇总时使用。支持输入来源：(1) 用户提供的原始变更列表，(2) git log/commit messages，(3) 已有草稿。输出固定结构：版本标题、版本范围、发布时间、功能新增、功能变更、问题修复、注意事项。
---

# 软件 Release Note 生成指南

## 输出要求

严格按照 [references/template.md](references/template.md) 的结构输出，不添加模板外章节。

- 每条变更必须带模块前缀：`[module] 描述`
- 若原文无模块且无法判断，使用 `[misc]`
- 仅当输入里存在 URL 时，才在对应条目附带链接
- 若某章节无内容，保留章节并填 `-`
- 输出纯 Markdown，不附带解释文本

## 工作流程

### 场景 1：用户提供原始变更

1. 读取 [references/template.md](references/template.md)
2. 提取产品名、版本号、版本范围、发布时间、注意事项
3. 将条目分类到对应章节（见下方分类规则）
4. 按模板输出完整的 Release Note

### 场景 2：用户要求从 Git 生成

1. 读取 [references/template.md](references/template.md)
2. 若用户未提供版本范围，先确认起止 tag（例如 `v1.1.0..v1.2.0`）
3. 使用以下命令收集提交信息：
   ```bash
   git log v1.1.0..v1.2.0 --pretty=format:"%h %s" --no-merges
   ```
4. 将 commit message 分类到对应章节
5. 按模板输出完整的 Release Note

### 场景 3：用户提供半成品草稿

1. 读取 [references/template.md](references/template.md)
2. 保留原始事实，不改写技术名词、接口名、topic 名、型号名
3. 统一格式并补全缺失章节

## 分类规则

| 章节 | 判断依据 |
|------|---------|
| 功能新增 | 新增能力、接口、服务、话题、硬件支持、部署方式 |
| 功能变更 | 既有行为调整、兼容性变更、优化、重构、默认值变化 |
| 问题修复 | 修复 bug、错误、异常 |
| 注意事项 | 不兼容变更、废弃功能、使用限制、升级注意 |

## 版本与时间规则

- 发布时间格式固定为 `YYYY-MM-DD`；未提供时默认当天日期
- 范围说明使用 `起始版本-当前版本`（例如 `1.1.0-1.2.0`）
- 若一次输出多个版本块，按“最新版本在前”排序
