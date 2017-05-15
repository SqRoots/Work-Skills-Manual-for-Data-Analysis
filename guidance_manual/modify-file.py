#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
#import io
#import sys
#import urllib.request
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 打开一个文件
with open('./_book/index.html', 'r', encoding='UTF-8') as f:
  str = f.read();

str2=re.sub(r'https://cdn\.mathjax\.org/mathjax/[^\/]+/MathJax\.js', r'//cdn.bootcss.com/mathjax/2.7.0/MathJax.js', str)

str2=re.sub(r'https://maxcdn.bootstrapcdn.com/bootstrap/[^\/]+/js/bootstrap.min.js', r'//cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js', str2)

str2=re.sub(r'https://maxcdn.bootstrapcdn.com/bootstrap/[^\/]+/css/bootstrap.min.css', r'//cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css', str2)

fo = open("./_book/index.html", "w+", encoding='utf8');

# 关闭打开的文件

fo.write(str2)

fo.close();
