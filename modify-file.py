#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
#import io
#import sys
#import urllib.request
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 打开一个文件

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 修改 index.html 中的链接：改为国内 CDN 镜像
with open('./_book/index.html', 'r', encoding='UTF-8') as f:
  str = f.read();

str2=re.sub(r'https://cdn\.mathjax\.org/mathjax/[^\/]+/MathJax\.js', r'//cdn.bootcss.com/mathjax/2.7.0/MathJax.js', str)

str2=re.sub(r'https://maxcdn.bootstrapcdn.com/bootstrap/[^\/]+/js/bootstrap.min.js', r'//cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js', str2)

str2=re.sub(r'https://maxcdn.bootstrapcdn.com/bootstrap/[^\/]+/css/bootstrap.min.css', r'//cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css', str2)

#str2=re.sub(r'\n', '', str2)

#str2=re.sub(r'\s+', r' ', str2)

with open('./_book/index.html', 'w+', encoding="utf8") as f:
  str = f.write(str2)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 修改 畅言 中的链接：改 http 为 https
with open('./_book/gitbook/gitbook-plugin-changyan/changyan.js', 'r', encoding='UTF-8') as f:
  str = f.read();

str2=re.sub(r'http://', r'https://', str)

with open('./_book/gitbook/gitbook-plugin-changyan/changyan.js', 'w+', encoding="utf8") as f:
  str = f.write(str2)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 修改 MathJax 配置
new_mathjax='''
      extensions: ["tex2jax.js"],
      jax: ["input/TeX", "output/HTML-CSS"],
      tex2jax: {
        inlineMath: [
          ['$', '$'],
          ["\\(", "\\)"]
        ],
        displayMath: [
          ['$$', '$$'],
          ["\\[", "\\]"]
        ],
        processEscapes: true
      },
      "HTML-CSS": {
        availableFonts: ["TeX"],
        styles: {
          "#MathJax_Zoom": {
            'background': '#eaeaea',
            '-webkit-box-shadow': '3px 3px 3px rgba(100,100,100,0.2)',
            'box-shadow': '3px 3px 3px rgba(100,100,100,0.2)'
          }
        }
      },
      menuSettings: { zoom: "Click" }
'''

with open('./_book/gitbook/gitbook-plugin-mathjax/plugin.js', 'r', encoding='UTF-8') as f:
  str = f.read();

str2=re.sub(r'tex2jax\:\s\{\}', new_mathjax, str)

with open('./_book/gitbook/gitbook-plugin-mathjax/plugin.js', 'w+', encoding="utf8") as f:
  str = f.write(str2)
