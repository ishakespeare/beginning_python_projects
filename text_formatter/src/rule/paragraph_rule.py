# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     paragraph_rule
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'


from src.rule.base_rule import BaseRule


class ParagraphRule(BaseRule):
    """

    """
    type = 'paragraph'

    def condition(self, block):
        """

        :param block:
        :return:
        """
        return True
