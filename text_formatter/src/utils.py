# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     utils
   Description :
   date：          2019/3/10
-------------------------------------------------
   Change Activity:
                   2019/3/10:   Created
-------------------------------------------------
"""
__author__ = 'daydream'


def file_block_generator(file):
    """
    transform a file into blocks generator
    :param file: str, the location of the file
    :return:

    """

    block = []
    with open(file=file) as f:
        for line in f:
            if line.strip():
                block.append(line)
            else:
                if block:
                    yield "".join(block)
                    block = []

    if block:
        yield "".join(block)


if __name__ == '__main__':

    for index, block in enumerate(file_block_generator(r"..\test\listing20-1.txt")):
        print(index, ":", block, end="")
