# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     titile_rule
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'


from src.rule.heading_rule  import HeadingRule


class TitleRule(HeadingRule):

    type = "title"
    first = True

    def condition(self, block):
        """

        :param block:
        :return:
        """
        if HeadingRule.condition(self, block) and TitleRule.first:
            TitleRule.first = False
            return True

        self.first = False
        return False

