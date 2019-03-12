# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_utils
   Description :
   date：          2019/3/12
-------------------------------------------------
   Change Activity:
                   2019/3/12:
-------------------------------------------------
"""
__author__ = 'daydream'


from src import utils

if __name__ == '__main__':
    for line in utils.file_block_generator("listing20-1.txt"):
        print(line)
