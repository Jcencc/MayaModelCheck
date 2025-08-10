# -*- coding: utf-8 -*-
# Jcen

from behavior_tree.core import (
    Action, Blackboard, Status, Inverter, Condition, Repeater, UntilFail
)


class TriangleFaceChecker(Action):
    def execute(self, blackboard: Blackboard) -> Status:
        print('TriangleFaceChecker.....')
        return Status.SUCCESS