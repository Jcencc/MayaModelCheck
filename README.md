# MayaModelCheck

MayaModelCheck 是一个用于 Autodesk Maya 软件的模型检查工具，旨在帮助用户规范模型资产、检查潜在问题，提高工作流程的效率和模型质量。

## 使用说明
- 将该工具集成到 Maya 环境中
- 通过行为树（Behavior Tree）框架调用相应的检查器：
- ShapeNameChecker：执行形状节点命名检查
- ShapeNameFix：执行形状节点命名修复
- TriangleFaceChecker：执行三角形面检查（开发中）

## 实现原理

工具基于行为树（Behavior Tree）架构设计，每个检查/修复功能封装为独立的 Action 类，通过 Blackboard 实现数据共享。

- 检查过程中发现的问题会记录到 Blackboard 中
- 修复功能会读取 Blackboard 中的问题数据并进行相应处理


## 作者

Jcen