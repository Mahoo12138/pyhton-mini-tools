import os
import re


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)   # 0-当前目录路径(string)
        print(dirs)   # 1-当前路径下所有子目录(list)
        print(files)  # 2-当前路径下所有非目录子文件(list)


for files in os.walk('D:/blog-with-hexo/source/_posts/'):
    print('当前目录下共有{}篇文章\n'.format(len(files[2])))
# file_name('D:/Mahoo/BLog/source/_posts/')


for i in range(len(files[2])):
    f = open('D:/blog-with-hexo/source/_posts/' + files[2][i], 'r', encoding="utf-8")
    string = f.read()
    f.close()
    key = 'http://img.mahoo12138.cn/'  # 旧域名
    new = 'https://img.mahoo12138.cn/'  # 新域名
    string = re.sub(key, new, string)
    f = open('D:/blog-with-hexo/source/_posts/' + files[2][i], 'w', encoding="utf-8")
    f.write(string)
    f.close()
    print('第{}篇操作完毕\n'.format(i))