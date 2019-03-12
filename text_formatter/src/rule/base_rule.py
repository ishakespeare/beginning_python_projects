# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base_rule
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'


class BaseRule:
    """
    base rule for all rules
    """

    def action(self, block, handler):
        """

        :param block:
        :param handler:
        :return:
        """
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True
