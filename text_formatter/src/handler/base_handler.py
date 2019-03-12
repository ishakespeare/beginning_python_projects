# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     handler
   Description :
   date：          2019/3/11
-------------------------------------------------
   Change Activity:
                   2019/3/11:
-------------------------------------------------
"""
__author__ = 'daydream'


class Handler:
    """

    """
    def callback(self, prefix, name, *args):
        """
        调用本对象方法名为 prefix + name的方法method
        :param prefix: 方法名 = prefix + name
        :param name: 方法名 = prefix + name
        :param args: method的参数
        :return: 如果method存在，返回调用method的返回结果，
        否则返回None

        """
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        """
        调用方法名为 start_<name>的方法
        :param name:
        :return:
        """
        return self.callback("start_", name)

    def end(self, name):
        """
        调用方法名为 end_<name>的方法
        :param name:
        :return:
        """
        return self.callback("end_", name)

    def sub(self, name):
        """
        根据替换名返回替换的策略函数
        :param name:
        :return:
        """
        def substitution(match):
            """

            :param match:
            :return:
            """
            result = self.callback("sub_", name, match)
            if result is None:
                return match.group(0)
            return result
        return substitution
