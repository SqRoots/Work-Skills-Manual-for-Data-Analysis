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
    md_str = fo.read()
    fo.close()
    # 处理 {% raw %}--{% endraw %} 或 {% math %}--{% endmath %}
    md_str_raws = re.findall(r'\{\%\s*raw\s*\%\}(.+?)\{\%\s*endraw\s*\%\}', md_str, flags=re.I|re.M|re.S)
    k = 1
    for md_str_raw in md_str_raws:
        ii = md_str_raw.strip(' \n\r')
        if ii[0] == '$' or ii[0:2] == r'\[':
            k += 1
            ii = re.sub(r'^\\\[|\\\]$', '$$', ii, flags=re.I) # 处理 \[--\]
            ns = re.sub(r'(?P<aa>[\_\{\}\\\$])', r'\\\g<aa>', ii, flags=re.I | re.M | re.S)
            md_str = md_str.replace(md_str_raw, ns)
        if k > 10000:
            break
    # 处理 \[--\]

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
    with open(path_new, 'w', encoding="utf8") as f:
        f.write(md_str)


curr_folder = os_path_join(os_path_abspath('.'), 'docs/')
for (path, sub_paths, file_names) in os_walk(curr_folder):
    for f in file_names:
        if f[-5:] == '-o.md':
            replace_escaped_characters(os_path_join(path, f))


