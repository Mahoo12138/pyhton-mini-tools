import os
import re
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup


web_list_6 = [
    'https://telegra.ph/%E6%9F%9A%E6%9C%A8-17728-1840861P-03-22',
    'https://telegra.ph/%E8%90%8C%E7%99%BD%E9%85%B1-%E5%8F%8C%E9%A9%AC%E5%B0%BE%E5%85%A8%E8%A3%B836P-01-22',
    'https://telegra.ph/%E8%90%8C%E7%99%BD%E9%85%B1-%E7%99%BD%E7%99%BD%E5%AB%A9%E5%AB%A9%E5%8F%8C%E9%A9%AC%E5%B0'
    '%BE49P1V-03-23',
    'https://telegra.ph/%E5%8F%91%E6%9D%A1%E5%B0%91%E5%A5%B3-%E6%82%A0%E8%8C%B6%E7%99%BE%E5%90%88129P-03-26',
    'https://telegra.ph/%E6%9F%9A%E6%9C%A8-1680557P-03-07',
    'https://telegra.ph/%E6%9F%9A%E6%9C%A8-%E5%9C%A3%E8%AF%9Ex%E5%B0%8F%E9%B9%BF56P1V-12-24',
    'https://telegra.ph/%E6%9F%9A%E6%9C%A8-%E5%A7%89%E3%81%A8%E5%A6%B9%E3%81%A8%E6%AF%8D42P1V-01-12'
]

def downloadImgs(url):
    # 发起网页请求\
    html = requests.get(url)
    # print(html)
    html.encoding = 'utf-8'
    # 
    html = BeautifulSoup(html.text, 'lxml')
    
    # 获取网页标题
    folder = html.title.text
    
    # 创建图片文件夹
    print('\n====  准备下载 %s 页面的图片  ====\n' % folder)
    if not os.path.exists(os.getcwd() + '\\' + folder):
        os.mkdir(folder)
    print('\n====  文件夹创建完毕，开始下载  ====\n')
    # 图片链接正则
    imagelist=re.findall('img src="(.*?)"',str(html))
    i = 0
    for url in imagelist:
        i += 1
        if not os.path.exists(os.getcwd() + '\\' + folder + '\\pic_' + str(i) + '.png'):
            print("{:65}  {:20}".format('\033[1;33m' + folder + '\033[0m:',"正在下载---第 \033[1;32m%d\033[0m 张图片" % i))
            #从图片地址下载数据
            image=requests.get('https://telegra.ph' + url)
            #在目标路径创建相应文件
            f=open(os.getcwd() + '\\' + folder + '\\pic_' + str(i) + '.png','wb')
            #将下载到的图片数据写入文件
            f.write(image.content)
            f.close()
        else:
            print("{:65}".format('\033[1;34m\n====  图片已下载，开始下载下一张  ====\033[0m\n'))
        
    print("\n\n\033[1;34m{:60s}\033[0m \033[1;32m下载成功\033[0m".format(folder))


if __name__ == '__main__':
    p = Pool(processes=7)
    for i in range(len(web_list_6)):
        print(web_list_6[i])
        p.apply_async(downloadImgs, args=(web_list_6[i],))
    print('\n====  开始下载图片  ====\n')
    p.close()
    p.join()
    print('\033[1;36;41m\n====  所有页面图片下载完成！  ====\033[0m\n')

    