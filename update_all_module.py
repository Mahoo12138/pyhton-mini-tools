import re
import os
pak_re = re.compile(r'[\w\-]+')
print("正在获取需要升级的包列表，需要网络，可能需要一点时间")
pak_list = os.popen("pip list -o").readlines()
print("已获取全部需要升级的包，总共", str(len(pak_list)-2), "个，请耐心等待")
for i in range(3,len(pak_list)):
    pak_list[i-3] = pak_re.search(pak_list[i])[0] + os.linesep
 
for i in range(len(pak_list)-2):
    print("正在安装：" + str(pak_list[i][0:-1]) + "\n")
    os.system("pip install --upgrade " + str(pak_list[i]))
    # print("\n\n第" + str(i+1) + "个包")
    print(str(pak_list[i][0:-1]) + "升级完成！")
 
print("恭喜！全部升级完成了！")