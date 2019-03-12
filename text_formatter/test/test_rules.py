# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_rules
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'

from src.rule.heading_rule import HeadingRule
from src.rule.titile_rule import TitleRule
from src.rule.paragraph_rule import ParagraphRule
from src.rule.list_item_rule import ListItemRule
from src.rule.list_rule import ListRule
from src.handler.html_handler import HTMLHandler
from src import utils

if __name__ == '__main__':
    rules = list()
    rules.append(HeadingRule())
    rules.append(TitleRule())
    rules.append(ParagraphRule())
    rules.append(ListItemRule())
    rules.append(ListRule())

    handler = HTMLHandler()

    for block in utils.file_block_generator("listing20-1.txt"):
        print(block.rstrip(), ": ", end="")
        for rule in rules:
            if rule.condition(block):
                print(rule.type, ",", end="")
        print("\n\n")

