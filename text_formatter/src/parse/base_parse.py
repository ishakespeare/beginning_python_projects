# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     BaseParse
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'

import re
from src import utils


class BaseParse:
    """

    """
    def __init__(self, handler):
        """

        :param handler:
        """
        self.handler = handler

        self.rules = []

        self.filters = []

    def add_rule(self,rule):
        """

        :param rule:
        :return:
        """
        self.rules.append(rule)

    def add_filter(self, pattern, name):
        """

        :param patter:
        :return:
        """

        def filter(block, handler):
            """

            :param block:
            :param handler:
            :return:
            """
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start("document")

        for block in utils.file_block_generator(file):

            for m_filter in self.filters:
                block = m_filter(block, self.handler)

            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end("document")
