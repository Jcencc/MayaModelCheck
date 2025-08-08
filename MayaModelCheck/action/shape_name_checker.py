# -*- coding: utf-8 -*-
# Jcen

from behavior_tree import (
    BehaviorTree, Sequence, Selector, Action, Condition, Status, Blackboard, Inverter, MockBackendFetcher, Parallel,
    Succeeder, Repeater, BackendFetcher
)


class ShapeNameChecker(Action):
    def execute(self, blackboard: Blackboard) -> Status:
        import maya.cmds as cmds
        select = blackboard.get('select', None)
        if not select:
            print('请设置选择模型', "\n")
            return Status.FAILURE
        print('正在执行Model Shape Name 检查', "\n")
        objs = cmds.listRelatives(select, ad=True, fullPath=True, type="transform") or []
        objs.insert(0, select)

        for obj in objs:
            shapes = cmds.listRelatives(
                obj, children=True, fullPath=True, shapes=True) or []
            if shapes:
                for shape in shapes:
                    isIntermediate = cmds.getAttr(
                        shape + ".intermediateObject")
                    if isIntermediate:
                        continue
                    shortName = obj.split("|")[-1]
                    shapeShortName = shape.split("|")[-1]

                    if shortName + "Shape" != shapeShortName:
                        print("  ", "检查到不规范命名：", shape, "\n")
                        blackboard.get('shapeError', []).append(shape)

        return Status.SUCCESS


class ShapeNameFix(Action):
    def execute(self, blackboard: Blackboard) -> Status:
        import maya.cmds as cmds
        print('shape名称修复中.....', "\n")
        for path in blackboard.get('shapeError') or []:
            print("  ", path, "--->", path.split('|')[-1].replace('Shape', '') + 'Shape', "\n")
            cmds.rename(path, path.split('|')[-1].replace('Shape', '') + 'Shape')
        return Status.SUCCESS  # 语义正确：数据更新成功
