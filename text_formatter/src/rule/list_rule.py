# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     list_rule
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'


from src.rule.list_item_rule import ListItemRule


class ListRule(ListItemRule):
    """

    """

    type = "list"
    inside = False

    def condition(self, block):
        """

        :param block:
        :return:
        """
        # return (not self.inside and ListItemRule.condition(self, block)) or \
        #        (self.inside and (not ListItemRule.condition(self, block)))
        return True

    def action(self, block, handler):
        """

        :param block:
        :param handler:
        :return:
        """
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(ListRule.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(ListRule.type)
            self.inside = False

        return False
