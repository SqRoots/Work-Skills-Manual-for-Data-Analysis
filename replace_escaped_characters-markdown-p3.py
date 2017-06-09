#!/usr/bin/python3
# -*- coding:utf8 -*-
# 替换 Markdown 中的逃逸字符
import re
from os import walk as os_walk
from os.path import abspath as os_path_abspath
from os.path import join as os_path_join


# 替换Markdown文档中的转义字符
def replace_escaped_characters(path):
    fo = open(path, 'r+', encoding="utf8")
    s = fo.read()
    fo.close()
    # 处理 {% raw %}--{% endraw %} 或 {% math %}--{% endmath %}
    ss = re.findall(r'\{\%\s*raw\s*\%\}(.+?)\{\%\s*endraw\s*\%\}', s, flags=re.I|re.M|re.S)
    k = 1
    for i in ss:
        k += 1
        ns = re.sub(r'(?P<aa>[\_\{\}\\\$])', r'\\\g<aa>', i, flags=re.I | re.M | re.S)
        print(i)
        s = s.replace(i, ns)
    # 处理 $$--$$
    # ss = re.findall(r'\${2}([^$]+?|\\\$+?)\${2}', s, flags=re.I|re.M|re.A)
    # k = 1
    # for i in ss:
    #     k += 1
    #     if len(i) > 2:
    #         ns = re.sub(r'(?P<aa>[\_\{\}\\])', r'\\\g<aa>', i, flags=re.I)
    #         print(ns)
    #         s = s.replace(i, ns)
    path_new = re.sub(r'-o\.md$', r'.md', path, flags=re.I)
    print(path_new)
    fo = open(path_new, 'w', encoding="utf8")
    fo.write(s)
    fo.close()


curr_folder = os_path_join(os_path_abspath('.'), 'docs/')
for (path, sub_paths, file_names) in os_walk(curr_folder):
    for f in file_names:
        if f[-5:] == '-o.md':
            replace_escaped_characters(os_path_join(path, f))


