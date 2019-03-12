# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_htm_parser
   Description :
   date：          2019/3/12
-------------------------------------------------
   Change Activity:
                   2019/3/12:
-------------------------------------------------
"""
__author__ = 'daydream'

from src.handler.html_handler import HTMLHandler
from src.parse.html_parser import BasicTextParser

if __name__ == '__main__':
    handler = HTMLHandler()
    parser = BasicTextParser(handler)

    parser.parse(r"B:\pycharm workplace\beginning_python_projects\text_formatter\test\listing20-1.txt")
