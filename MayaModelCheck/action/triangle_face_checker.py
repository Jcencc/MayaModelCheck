# -*- coding: utf-8 -*-
# Jcen

from behavior_tree import (
    BehaviorTree, Sequence, Selector, Action, Condition, Status, Blackboard, Inverter, MockBackendFetcher, Parallel,
    Succeeder, Repeater, BackendFetcher
)


class TriangleFaceChecker(Action):
    def execute(self, blackboard: Blackboard) -> Status:
        print('TriangleFaceChecker.....')
        return Status.SUCCESS