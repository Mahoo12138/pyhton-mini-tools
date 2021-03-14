import os

filepath = 'D:\Mahoo12138\Code\VS2019Projects\C 语言程序设计'

for file in os.listdir(filepath):
    if (file.endswith(".c")):
        name1 = file.replace('(','')
        name2 = name1.replace(')','')

        print(name2)
