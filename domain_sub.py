import os
import re


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)   # 0-当前目录路径(string)
        print(dirs)   # 1-当前路径下所有子目录(list)
        print(files)  # 2-当前路径下所有非目录子文件(list)


# 注意，文件地址后的 ‘ / ’不能少
path = 'D:/Website/blog-with-hexo/source/_posts/'
if not os.path.exists(path):
    print("请检查路径是否正确！")
else:
    for files in os.walk(path):
        print('当前目录下共有{}篇文章\n'.format(len(files[2])))
        for i in range(len(files[2])):
            f = open(path + files[2][i], 'r', encoding="utf-8")
            string = f.read()
            f.close()
            old = 'https://cdn.jsdelivr.net/gh/mahoo12138/js-css-cdn/hexo-images/Study/'  # 旧域名
            new = 'https://cdn.jsdelivr.net/gh/mahoo12138/js-css-cdn/hexo-images/study/'  # 新域名
            string = re.sub(old, new, string)
            f = open(path + files[2][i], 'w', encoding="utf-8")
            f.write(string)
            f.close()
            print('第{}篇操作完毕\n'.format(i))
