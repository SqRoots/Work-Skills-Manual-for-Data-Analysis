#!/usr/bin/python3
# coding=utf-8
# 1. 修改“*.html”中的：http 为 https
# 2. 修改“*.html”中的：国外镜像为国内镜像
import sys
import os



current_path = sys.path[0]

shell1 = 'python3 ' + os.path.join(current_path, 'replace_escaped_characters-markdown-p3.py')
shell2 = 'gitbook build '
shell3 = 'python3 ' + os.path.join(current_path, 'modify_html_or_js-p3.py')

print(os.system(shell1))
print(os.system(shell2))
print(os.system(shell3))