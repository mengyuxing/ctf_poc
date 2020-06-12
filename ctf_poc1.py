# -*- coding:utf-8 -*-
# name: Meng
# mail: 614886708@qq.com
# ctf_poc01: BugkuCTF 秋名山老司机

import requests
import re


class Driver:
    def __init__(self, url):
        self.url = url          # 输入链接
        self.s = requests.Session()

        self.expression = ''    # 计算表达式
        self.flag = ''        # flag

    def compute(self):
        # 获取计算表达式
        source = self.s.get(self.url).text
        self.expression = re.search(r'(\d+[+*/-])+(\d+)', source).group()

        # 计算表达式并POST传参
        data = {'value': eval(self.expression)}
        result = self.s.post(self.url, data=data).text

        # 过滤结果 只保留flag内容
        self.flag = re.search(r'Bugku\{.+\}', result).group()

        return self.flag


if __name__ == '__main__':
    print('ctf_poc01: BugkuCTF 秋名山老司机')
    url = input('请输入题目链接：')
    flag = Driver(url).compute()
    print(flag)
