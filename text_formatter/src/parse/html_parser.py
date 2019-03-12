# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     html_parser
   Description :
   date：          2019/3/12
-------------------------------------------------
   Change Activity:
                   2019/3/12:
-------------------------------------------------
"""
__author__ = 'daydream'

from src.parse.base_parse import BaseParse
from src.rule.heading_rule import HeadingRule
from src.rule.titile_rule import TitleRule
from src.rule.paragraph_rule import ParagraphRule
from src.rule.list_item_rule import ListItemRule
from src.rule.list_rule import ListRule


class BasicTextParser(BaseParse):
    """
    A specific Parser that adds rules and filters in its constructor.
    """
    def __init__(self, handler):
        BaseParse.__init__(self, handler)
        self.add_rule(ListRule())
        self.add_rule(ListItemRule())
        self.add_rule(TitleRule())
        self.add_rule(HeadingRule())
        self.add_rule(ParagraphRule())

        self.add_filter(r'\*(.+?)\*', 'emphasis')
        self.add_filter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.add_filter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


