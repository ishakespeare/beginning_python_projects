# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     list_item_rule
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'


from src.rule.base_rule import BaseRule


class ListItemRule(BaseRule):
    """

    """
    type = "listitem"

    def condition(self, block):
        """

        :param block:
        :return:
        """
        return block.lstrip()[0] == '-'

    def action(self, block, handler):
        """

        :param block:
        :param handler:
        :return:
        """
        handler.start(ListItemRule.type)
        handler.feed(block[1:].strip())
        handler.end(ListItemRule.type)
        return True
