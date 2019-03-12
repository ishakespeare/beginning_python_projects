# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     HTMLHandler
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'

from src.handler import base_handler


class HTMLHandler(base_handler.Handler):
    """

    """

    def start_document(self):
        """

        :return:
        """
        print(r"<html><head><title>...</title></head>")

    def end_document(self):
        """

        :return:
        """
        print(r"</body></html>")

    def start_paragraph(self):
        """

        :return:
        """
        print(r"<p>")

    def end_paragraph(self):
        """

        :return:
        """
        print(r"<\p>")

    def start_heading(self):
        """

        :return:
        """
        print(r"<h2>")

    def end_heading(self):
        """

        :return:
        """
        print(r"<\h2>")

    def start_title(self):
        """

        :return:
        """
        print(r"<h1>")

    def end_title(self):
        """

        :return:
        """
        print(r"<\h1>")

    def start_list(self):
        """

        :return:
        """
        print(r"<ul>")

    def end_list(self):
        """

        :return:
        """
        print(r"<\ul>")

    def start_listitem(self):
        """

        :return:
        """
        print(r"<li>")

    def end_listitem(self):
        """

        :return:
        """
        print(r"</li>")

    def feed(self, data):
        """

        :param data:
        :return:
        """
        print(data)

    def sub_emphasis(self, match):
        """

        :param match:
        :return:
        """
        return r'<em>{}</em>'.format(match.group(1))

    def sub_url(self, match):
        """

        :param match:
        :return:
        """
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))

    def sub_mail(self,match):
        """

        :param match:
        :return:
        """
        return '<a href="mailto:{}">{}</a>'.format(match.group(1), match.group(1))



