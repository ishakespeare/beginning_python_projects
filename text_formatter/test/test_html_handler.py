# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_html_handler
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'

from src.handler.html_handler import HTMLHandler

if __name__ == '__main__':
    handler = HTMLHandler()
    handler.start("document")
    handler.start("title")
    handler.end("title")
    handler.start("heading")
    handler.end("heading")
    handler.start("paragraph")
    handler.end("paragraph")
    handler.start("list")
    handler.start("listitem")
    handler.feed("one")
    handler.end("listitem")
    handler.start("listitem")
    handler.feed("two")
    handler.end("listitem")
    handler.start("listitem")
    handler.feed("three")
    handler.end("listitem")
    handler.end("list")
    handler.end("document")

    em = handler.sub("emphasis")
    url = handler.sub("url")
    mail = handler.sub("mail")
    print(type(em))
    print(type(url))
    print(type(mail))

    import re
    em_str = r"ab*aaa*ba"
    print(re.sub(r"b(\*.*?\*)b", em, em_str))
    print(em_str)

    url_str = r"ab*aaa*ba"
    print(re.sub(r"b(\*.*?\*)b", url, url_str))
    print(url_str)

    mail_str = r"ab*aaa*ba"
    print(re.sub(r"b(\*.*?\*)b", mail, mail_str))
    print(mail_str)
