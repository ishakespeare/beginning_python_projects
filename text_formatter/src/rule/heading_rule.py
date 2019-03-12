# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     heading_rule
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'


from src.rule.base_rule import BaseRule


class HeadingRule(BaseRule):

    type = "heading"

    def condition(self, block):
        """

        :param block:
        :return:
        """
        return ('\n' not in block.rstrip()) and len(block) <= 70 and not block[-1] == ':'
