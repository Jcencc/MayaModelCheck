# -*- coding: utf-8 -*-
# Jcen

from behavior_tree.core import (
    Action, Blackboard, Status, Inverter, Condition, Repeater, UntilFail
)
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'  # 只保留级别和消息，去掉日志器名称
)


class ShapeNameChecker(Action):
    def execute(self, blackboard: Blackboard) -> Status:
        import maya.cmds as cmds

        select = blackboard.get('select', None)
        if not select:
            logging.info('请设置选择模型')
            return Status.FAILURE
        logging.info('正在执行Model Shape Name 检查')
        objs = cmds.listRelatives(select, ad=True, fullPath=True, type="transform") or []
        objs.insert(0, select)
        blackboard.set('shapeError', [])
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
                        logging.info("   检查到不规范命名：" + shape)
                        blackboard.get('shapeError', []).append(shape)

        return Status.SUCCESS


class ShapeNameFix(Action):
    def execute(self, blackboard: Blackboard) -> Status:
        import maya.cmds as cmds
        logging.info('shape名称修复中.....')
        for path in blackboard.get('shapeError') or []:
            logging.info("  "+ path+"--->"+path.split('|')[-1].replace('Shape', '') + 'Shape')
            cmds.rename(path, path.split('|')[-1].replace('Shape', '') + 'Shape')
        return Status.SUCCESS  # 语义正确：数据更新成功
