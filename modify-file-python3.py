#!/usr/bin/python
# coding=utf-8
import re
from os import walk
from os.path import join

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 修改 *.html 中的链接：改为国内 CDN 镜像


def replace_cdn(p):
    fo = open(p, 'r', encoding='UTF-8')
    fc = fo.read()
    fo.close()
    fc2 = re.sub(r'https://cdn\.mathjax\.org/mathjax/[^\/]+/MathJax\.js',
                           r'//cdn.bootcss.com/mathjax/2.7.0/MathJax.js', fc)
    fc2 = re.sub(r'https://maxcdn.bootstrapcdn.com/bootstrap/[^\/]+/js/bootstrap.min.js',
                           r'//cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js', fc2)
    fc2 = re.sub(r'https://maxcdn.bootstrapcdn.com/bootstrap/[^\/]+/css/bootstrap.min.css',
                           r'//cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css', fc2)
    fo = open(p, 'w+', encoding="utf8")
    fo.write(fc2)
    fo.close()

my_path = r'./_book/'
for (path, sub_paths, file_names) in walk(my_path):
    for f in file_names:
        if f[-5:] == '.html':
            replace_cdn(join(path, f))

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 修改 畅言 中的链接：改 http 为 https
my_path = './_book/gitbook/gitbook-plugin-changyan/changyan.js'
with open(my_path, 'r', encoding='UTF-8') as f:
    file_content = f.read()

file_content2 = re.sub(r'http://', r'https://', file_content)
with open(my_path, 'w+', encoding="utf8") as f:
    f.write(file_content2)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 修改 MathJax 配置
mathjax_conf = '''
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

my_path = './_book/gitbook/gitbook-plugin-mathjax/plugin.js'
with open(my_path, 'r', encoding='UTF-8') as f:
    file_content = f.read()

file_content2 = re.sub(r'tex2jax\:\s\{\}', mathjax_conf, file_content)
with open(my_path, 'w+', encoding="utf8") as f:
    f.write(file_content2)
