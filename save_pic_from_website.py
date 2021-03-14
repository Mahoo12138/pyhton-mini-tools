import os
import re
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process,Pool

def downloadImgs(url):
    # 发起网页请求
    html = requests.get(url)
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


web_list_1 = [
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E9%80%B8%E4%BB%99-51P-12-26',
    'https://telegra.ph/rioko%E5%87%89%E5%87%89%E5%AD%90---%E5%9C%A3%E8%AF%9E%E8%B4%9D%E5%B0%94%E6%B3%95%E6%96%AF%E7%89%B9-24P-12-24',
    'https://telegra.ph/%E5%8D%97%E6%A1%83Momoko---%E6%98%A5%E6%97%A5%E9%87%8E%E7%A9%B9%E4%BD%93%E6%93%8D%E6%9C%8D-28P-12-23',
    'https://telegra.ph/%E5%B7%A5%E5%8F%A3%E5%B0%8F%E5%A6%96%E7%B2%BE---%E8%BE%93%E4%BA%86%E9%BA%BB%E5%B0%86%E5%85%A8%E8%A3%B8%E5%9C%A8%E6%A1%8C%E4%B8%8A%E7%9A%84%E5%B0%8F%E8%B1%B9%E7%8C%AB-52P-12-20',
    'https://telegra.ph/%E6%9F%9A%E6%9C%A8%E4%BC%97%E7%AD%B9%E4%BD%9C%E5%93%81%E6%97%A0%E5%9C%A3%E5%85%89%E5%A5%97%E5%9B%BE-43P-12-19',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E4%BC%8A%E8%8E%89%E9%9B%85-80P-12-17',
    'https://telegra.ph/%E7%94%9C%E7%BE%8E%E5%B0%8F%E6%AB%BB%E5%AD%90---%E6%83%85%E8%B6%A3%E8%82%9A%E5%85%9C-73P-12-11',
    'https://telegra.ph/%E6%81%B6%E7%8A%AC%E5%B0%8F%E5%A7%90%E5%A7%90-JK%E5%A5%97-28P-12-10',
    'https://telegra.ph/%E6%9F%9A%E6%9C%A8%E6%88%B7%E5%A4%96%E7%B2%BE%E9%80%89%E6%97%A0%E5%9C%A3%E5%85%89%E5%A5%97%E5%9B%BE-61P-12-07',
    'https://telegra.ph/%E8%BD%AF%E8%BD%AF%E9%85%B1%E6%82%A0%E5%AE%9D-%E5%A4%A7%E5%AD%A6%E9%9C%B2%E5%87%BA-59P-12-06',
    'https://telegra.ph/%E7%BE%8E%E7%BE%BDmiu---%E6%80%A7%E6%84%9F%E4%B9%8B%E5%A4%9C-34P-11-30',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB%E8%A1%A5%E5%85%85---GF-60P-11-21',
    'https://telegra.ph/%E6%AB%BB%E6%A1%83%E5%96%B5---%E5%A5%B3%E4%BB%86-38P-11-21',
    'https://telegra.ph/%E5%AE%8C%E7%BE%8E%E8%83%B8%E5%9E%8BNaughtyThrowawayF-81P-11-21',
    'https://telegra.ph/%E8%90%8C%E5%85%B0%E9%85%B1---%E5%92%8C%E6%9C%8D-100P-11-21',
    'https://telegra.ph/%E8%BD%AF%E8%BD%AF%E9%85%B1m---%E5%AE%A4%E5%A4%96%E6%A0%A1%E6%9C%8D-60P-11-19',
    'https://telegra.ph/%E8%BD%AF%E8%BD%AF%E9%85%B1---%E6%82%A0%E5%AE%9D---%E7%99%BD%E4%B8%9D%E7%99%BE%E5%90%88---Loli-lesbian-girls-80P-12-02',
    'https://telegra.ph/Yoko%E5%AE%85%E5%A4%8F%E5%A6%B9%E6%B1%A4%E7%89%A9%E8%AF%AD-%E6%A0%A1%E6%9C%8D-63P-11-18',
    'https://telegra.ph/%E9%9D%A2%E9%A5%BC%E4%BB%99%E5%84%BF-%E7%8E%89%E7%8E%B2%E7%8F%91-27P-11-16',
    'https://telegra.ph/AISS%E7%88%B1%E4%B8%9D-%E5%81%87%E6%97%A5%E6%B8%B8%E4%B9%90%E5%9B%AD-78P-11-12',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E7%BB%9A%E6%BF%91%E7%BB%98%E7%90%86-87P-11-08',
    'https://telegra.ph/%E9%BB%91%E5%B7%9D---%E5%AD%A6%E7%94%9F-Black-School-Unifrom-52P-10-24',
    'https://telegra.ph/%E8%BD%AF%E8%BD%AF%E9%85%B1%E7%99%BD%E8%A1%AC%E8%A1%AB-60P-11-06',
    'https://telegra.ph/Yoko%E5%AE%85%E5%A4%8F%E5%92%8C%E6%9C%8D-53P-11-05',
    'https://telegra.ph/Fantasy-Factory%E5%8D%95%E8%BD%A6%E9%AA%91%E8%A1%8C-53P-11-04',
    'https://telegra.ph/Yuzuki%E6%9F%9A%E6%9C%A8%E5%86%99%E7%9C%9F-%E6%B6%A0%E6%B4%B2%E5%B2%9B-71P-11-03',
    'https://telegra.ph/%E6%B1%A1%E7%A5%9E%E6%98%A0%E7%94%BB---%E7%8C%AB%E5%92%AA%E5%9C%86%E8%88%9E%E6%9B%B2-73P-10-31',
    'https://telegra.ph/%E8%BD%AF%E8%BD%AF%E9%85%B1m---%E6%A0%A1%E6%9C%8D-60P-10-30',
    'https://telegra.ph/Yoko%E5%AE%85%E5%A4%8F%E8%89%B6%E5%A8%98%E5%B9%BB%E6%A2%A6%E8%B0%AD-%E9%87%91%E8%8E%B2---24P-10-28',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E5%B0%8F%E5%8F%BD-80P-10-25',   
    'https://telegra.ph/%E9%88%B4%E6%9C%A8%E7%BE%8E%E5%92%B2---Fornication-game---33P-10-25',
    'https://telegra.ph/%E6%A8%B1%E7%A9%BA%E6%A1%83Momo-Sakura---120P-10-24',
    'https://telegra.ph/Ahihi---Little-Cute-cosplay-girl---89P-10-23',   
    'https://telegra.ph/%E9%82%BB%E5%AE%B6%E5%A4%A7%E5%A7%90%E5%A7%90%E7%9A%84%E9%BB%91%E4%B8%9D-%E7%99%BD%E9%93%B6---45P-10-21',
    'https://telegra.ph/%E5%A5%88%E8%8E%89%E9%85%B1%E5%B8%86%E9%A3%8ELolita---48P-10-21',
    'https://telegra.ph/Yoko%E5%AE%85%E5%A4%8F%E7%AA%81%E5%87%BB%E6%90%9C%E6%9F%A5%E5%AE%98-32P-09-28',
    'https://telegra.ph/%E8%8F%A0%E8%90%9D%E7%A4%BE---%E7%8C%AB%E4%B9%9D%E9%85%B1-%E5%A4%A7%E5%B0%BA%E5%BA%A6%E8%A7%86%E5%9B%BE%E6%B5%81%E5%87%BA-80P-10-13',
    'https://telegra.ph/Yuzuki%E6%9F%9A%E6%9C%A8%E5%86%99%E7%9C%9F-%E8%B5%9B%E5%8D%9A%E6%9C%8B%E5%85%8B-51P-10-11',
    'https://telegra.ph/%E4%B8%80%E5%B0%8F%E5%A4%AE%E6%B3%BD%E5%92%8C%E9%A3%8E-41P-09-28',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E5%A4%95%E7%AB%8B-80P-09-26',    
    'https://telegra.ph/Misaki-Suzuki---Sexy-girl-in-old-china-architecture-44P-09-28',
    'https://telegra.ph/%E9%9D%A2%E9%A5%BC%E4%BB%99%E5%84%BFAzur-Lane-Atago-2Vers-40P-10-02',
    'https://telegra.ph/%E8%98%BF%E8%8E%89-%E6%83%85%E8%B6%A3%E5%A9%9A%E7%B4%97---50P-09-28',    
    'https://telegra.ph/Hodori---Casual-Night-Selfie---23P-09-28',
    'https://telegra.ph/%E8%BD%AF%E8%BD%AF%E9%85%B1%E5%8E%A8%E5%A8%98-19P-09-28',
    'https://telegra.ph/Fantasy-FactoryCOS%E8%A3%85-89P-09-27',
    'https://telegra.ph/AKekiMaru-%E5%B0%8F%E8%9B%8B%E7%B3%95%E5%A7%8A%E5%A7%8A-Small-cake-sister-35P-09-25',    
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E8%BF%B7%E4%B9%8B%E5%A5%B3%E4%B8%BB%E8%A7%92X-78P-09-18',
    'https://telegra.ph/BoLoLi%E6%B3%A2%E8%90%9D%E7%A4%BEBOL130-%E5%A4%8F%E7%BE%8E%E9%85%B1-%E5%A4%8F%E6%97%A5%E9%AA%84%E9%98%B3-41P-09-16',
    'https://telegra.ph/%E6%B4%9B%E7%BE%8E%E6%97%A0%E5%86%85%E9%BB%91%E4%B8%9D-41P-09-14',    
    'https://telegra.ph/%E6%A1%9C%E6%A1%83%E5%96%B5---%E5%86%AC%E7%9C%A0%E7%B3%BB%E5%88%97-%E7%B2%89%E8%89%B2%E6%B5%B4%E7%BC%B8-57P-09-13',
    'https://telegra.ph/%E5%A5%B6%E8%82%8C%E9%85%B1-%E5%85%AC%E5%9B%AD%E9%9C%B2%E5%87%BA-36P-09-12',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E5%86%B2%E7%94%B0%E6%80%BB%E5%8F%B8-111P-09-07',
    'https://telegra.ph/%E8%BF%87%E6%9C%9F%E7%B1%B3%E7%BA%BF%E7%BA%BF%E5%96%B5-%E6%B5%B4%E7%BC%B8%E7%97%9B%E8%A2%9C-51P-09-06',
    ]


web_list_2 = [
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E6%97%B6%E5%B4%8E%E7%8B%82%E4%B8%89-%E6%8A%A4%E5%A3%AB%E7%99%BD%E4%B8%9D-80P-08-17',
    'https://telegra.ph/%E6%8A%96%E5%A8%98%E5%88%A9%E4%B8%96---%E9%BB%91%E7%99%BD%E6%97%97%E8%A2%8D%E5%8F%8C%E5%AD%90-41P-08-18',
    'https://telegra.ph/MiiTao%E8%9C%9C%E6%A1%83%E7%A4%BEVol120-Mia%E7%B1%B3%E5%A8%85-52P-09-29',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E7%BB%9A%E6%BF%91%E7%BB%98%E7%90%86-87P-11-08',
    'https://telegra.ph/%E9%BB%91%E5%B7%9D---%E5%AD%A6%E7%94%9F-Black-School-Unifrom-52P-10-24',
]

web_list_3 = [
    'https://telegra.ph/Thuy-Nga-Ph%E1%BA%A1m-%E9%99%B6%E7%93%B7%E5%86%99%E7%9C%9F-103P-03-18',
    'https://telegra.ph/%E6%8A%B1%E8%B5%B0%E8%8E%AB%E5%AD%90aa-%E9%BB%91%E4%B8%9D%E7%8C%AB%E5%92%AA%E5%B0%8F%E5%A5%B3%E4%BB%86-44P-03-17',
    'https://telegra.ph/Graphis-Remu-Suzumori-%E6%B6%BC%E6%A3%AE%E3%82%8C%E3%82%80-132P-03-16',
    'https://telegra.ph/JVID-%E9%BB%91%E4%B8%9DOL%E4%B8%8B%E7%8F%AD%E5%90%8E%E7%9A%84%E6%97%85%E9%A6%86-104P-03-15',
    'https://telegra.ph/YUZUKI-%E7%BE%8A%E5%9F%8E%E7%99%BE%E5%90%88-62P-03-14',
    'https://telegra.ph/PDLONE%E6%BD%98%E5%A4%9A%E6%8B%89%E9%93%82%E9%87%91%E5%88%8AVOL2974P-03-13',
    'https://telegra.ph/CHOKmoson%E8%84%AB%E7%A5%9E-%E5%B0%91%E5%A5%B3%E8%84%AB-108P-03-10',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E7%9C%9F%E5%A7%AC%E6%97%97%E8%A2%8D-94P-03-09',
    'https://telegra.ph/%E4%BA%AC%E9%A6%99Julia160P-03-08',
    'https://telegra.ph/Yuzuki-%E6%9F%9A%E6%9C%A8%E5%86%99%E7%9C%9F---%E5%8E%A6%E9%97%A8%E6%B0%91%E5%AE%BF-35P-03-07',
    'https://telegra.ph/Kancolle-Shigure-Cosplay-%E5%B0%8F%E4%B8%81Ding---65P-03-06',
    'https://telegra.ph/%E7%99%BD%E9%93%B681---%E5%B0%8F%E7%99%BD%E5%85%94-105P-03-04',
    'https://telegra.ph/%E6%B4%9B%E7%BE%8E---%E7%BA%A2%E6%83%85%E8%B6%A3%E5%A5%97-44P-03-01',
    'https://telegra.ph/%E9%9B%AF%E5%A6%B9-%E5%A5%B3%E8%AD%A6-32P-02-29',
    'https://telegra.ph/%E8%B5%B7%E5%8F%B8%E5%9D%97wii-Vol004-%E4%BC%A0%E7%BB%9F%E5%A5%B3%E4%BB%86-58P-02-28',
    'https://telegra.ph/%E6%91%84%E5%BD%B1%E5%B8%88%E6%9D%8E%E6%80%9D%E8%B0%8B%E5%87%BA%E5%93%81%E6%97%A0%E5%9C%A3%E5%85%89%E5%A5%97%E5%9B%BE-77P-02-27',
    'https://telegra.ph/%E4%B8%89%E4%B8%8A%E6%82%A0%E4%BA%9AYua-Mikami-140P-02-26',
    'https://telegra.ph/Yuzuki-%E5%93%81%E7%8E%89%E7%B3%BB%E5%88%97-1-3%E5%A5%97%E5%90%88%E9%9B%86-86P-02-24',
    'https://telegra.ph/%E4%B8%89%E5%BA%A6-69-%E7%8B%90%E5%B7%AB%E5%A5%B3%E7%BA%A2%E8%89%B2%E6%97%97%E8%A2%8D-45P-02-20',
    'https://telegra.ph/%E6%9F%9A%E6%9C%A8%E5%86%99%E7%9C%9Fx%E6%9D%AA%E5%A4%8F---%E9%81%8E%E6%BF%80%E3%81%AA%E5%A7%89%E5%A6%B9H%E8%A1%8C%E7%88%B2-93P-02-18',
    'https://telegra.ph/Misaki-Suzuki-%E5%A4%A7%E5%B0%8F%E5%A7%90%E7%9A%84%E7%BE%8E%E8%B6%B3%E7%89%B9%E5%85%B8-182P-02-16',
    'https://telegra.ph/PR%E7%A4%BE%E5%B0%91%E5%A5%B3%E9%9A%94%E5%A3%81%E5%B0%8F%E5%A7%90%E5%A7%9039P-02-15',
    'https://telegra.ph/MISSLEG%E8%9C%9C%E4%B8%9D-%E4%B9%94%E4%BE%9D%E7%90%B3-%E6%83%85%E4%BA%BA%E8%8A%82%E7%8E%AB%E7%91%B0%E7%89%A9%E8%AF%AD-41P-02-14',
    'https://telegra.ph/%E5%96%B5%E9%85%B1%E6%98%AFhentai%E6%97%A0%E5%9C%A3%E5%85%89%E5%A5%97%E5%9B%BE48P-02-12',
    'https://telegra.ph/%E6%B1%A4%E4%B8%8A%E7%BA%A2%E4%BA%BA%E6%B0%B4%E6%BA%90%E8%80%81%E5%B8%88%E9%AB%98%E6%B8%85%E7%A7%81%E6%8B%8D-163P-02-11',
    'https://telegra.ph/Yuzuki%E8%B4%AB%E4%B9%B3JK%E9%BB%91%E9%95%BF%E7%9B%B4-54P-02-10',
    'https://telegra.ph/%E7%99%BD%E9%8A%80-White-Virgin---56P-02-07',
    'https://telegra.ph/%E7%A8%9A%E9%A2%9C%E9%85%B1-%E4%B8%9D%E8%A2%9C%E5%90%88%E9%9B%86-96P-02-06',
    'https://telegra.ph/MyGirl%E7%BE%8E%E5%AA%9B%E9%A6%86-VOL336-%E7%8B%90%E5%B0%8F%E5%A6%96Baby-41P-02-03',
    'https://telegra.ph/Nagesa%E9%AD%94%E7%89%A9%E5%96%B5-VOL9-SSSSGRIDMAN---96P-02-02',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%9E%AA%E6%A2%B0%E5%B8%88---%E5%A5%B3%E4%BB%86%E7%9A%AE%E8%A3%A4-50P-02-01',
    'https://telegra.ph/%E8%B5%B7%E5%8F%B8%E5%9D%97wii-%E9%95%9C%E4%B8%AD%E7%97%B4%E5%A7%AC-41P-01-31',
    'https://telegra.ph/%E8%BF%87%E6%9C%9F%E7%B1%B3%E7%BA%BF%E7%BA%BF%E5%96%B5-%E6%96%B0%E5%B9%B4%E6%97%97%E8%A2%8D-60P-01-30',
    'https://telegra.ph/CHOKmoson%E8%84%AB%E7%A5%9E-%E8%84%AB%E4%BD%A0%E5%A6%B9-56P-01-28',
    'https://telegra.ph/%E6%9C%89%E5%96%B5%E9%85%B1HK%E6%97%85%E6%8B%8D-82P-01-22',
    'https://telegra.ph/%E5%8D%97%E6%A1%83Momoko-87P-01-22',
    'https://telegra.ph/Fantasy-Factory-%E5%B0%8F%E4%B8%81-58P-01-21',
    'https://telegra.ph/%E7%9F%A5%E4%B8%80%E5%A6%B9%E5%A6%B9--Perfect-Boobies---41P-01-14',
    'https://telegra.ph/%E6%81%B6%E7%8A%AC%E5%B0%8F%E5%A7%90%E5%A7%90-%E5%A5%B3%E8%AD%A6%E5%A5%97-39P-01-12',
    'https://telegra.ph/%E5%96%B5%E7%B3%96%E6%98%A0%E7%94%BB-%E7%9D%A1%E8%A1%A3%E8%95%BE%E5%A7%86-40P-01-11',
    'https://telegra.ph/%E6%9E%81%E5%93%81%E7%BD%91%E7%BB%9C%E7%BA%A2%E4%BA%BA%E8%93%9D%E8%89%B2%E6%B0%B4%E8%91%97%E6%97%A0%E5%9C%A3%E5%85%89%E5%A5%97%E5%9B%BE-67P-12-31',
    'https://telegra.ph/%E6%B1%A1%E7%A5%9E%E6%98%A0%E7%94%BB---%E5%A5%B3%E4%BB%86-70P-01-07',
    'https://telegra.ph/%E8%BF%87%E6%9C%9F%E7%B1%B3%E7%BA%BF%E7%BA%BF%E5%96%B5-%E5%9C%A3%E8%AF%9E-52P-01-06',
    'https://telegra.ph/%E7%A6%8F%E5%88%A9%E5%A7%AC%E5%8C%97%E4%B9%83%E8%8A%BD%E5%AD%90Hokunaimeko-138P-12-31',
    'https://telegra.ph/%E5%BE%AE%E5%8D%9A%E7%BA%A2%E4%BA%BA%E5%BE%85%E5%AE%89%E5%A8%9C%E6%B3%B0%E5%9B%BD%E5%86%99%E7%9C%9F%E5%9B%BE%E5%8C%85%E6%97%A0%E5%9C%A3%E5%85%89%E5%8E%9F%E7%89%88-33P-01-01',
    'https://telegra.ph/%E4%B8%80%E5%B0%8F%E5%A4%AE%E6%B3%BD-%E9%A3%8E%E9%93%83%E8%8A%B1%E4%B8%8E%E8%96%B0%E8%A1%A3%E8%8D%89-48P-01-01',
    'https://telegra.ph/Nagisa%E9%AD%94%E7%89%A9%E5%96%B5vol04-171P-12-26',
]

web_list_4 = [
    'https://telegra.ph/Fantasy-Factory%E5%B0%8F%E4%B8%81-45P-08-21',
    'https://telegra.ph/%E6%9D%AA%E5%A4%8F---%E7%88%B1%E4%B8%BD%E4%B8%9D%E6%A2%A6%E6%B8%B8%E4%BB%99%E5%A2%83-50P-04-04-2',
    'https://telegra.ph/MISSLEG%E8%9C%9C%E7%B5%B2-N004-%E5%9C%98%E5%9C%98-%E5%AD%A4%E7%8D%A8-60P-04-08',
    'https://telegra.ph/%E6%8A%96%E5%A8%98%E5%88%A9%E4%B8%96---%E5%A5%B3%E5%B7%AB-40P-04-09',
    'https://telegra.ph/%E6%9D%AA%E5%A4%8F---%E5%A4%A9%E4%BD%BF-76P-04-10',
    'https://telegra.ph/ATFMaker--%E7%99%BD%E4%BF%AE%E5%A5%B3-63P-04-11',
    'https://telegra.ph/ATFMaker---%E6%8D%86%E7%BB%91Play-40P-04-12',
    'https://telegra.ph/%E6%82%A0%E5%AE%9D-%E5%B9%BC%E7%A8%9A%E5%9B%AD%E9%9C%B2%E5%87%BA-44P-04-14',
    'https://telegra.ph/rioko%E5%87%89%E5%87%89%E5%AD%90-%E5%AD%A6%E5%A7%90-40P-04-15',
    'https://telegra.ph/Misaki-Suzuki-%E5%B9%BC%E7%A8%9A%E7%9A%84%E6%81%8B%E7%88%B1-46P-04-16',
    'https://telegra.ph/%E8%A0%A2%E6%B2%AB%E6%B2%AB---%E6%81%B6%E9%AD%94-40P-04-18',
    'https://telegra.ph/%E8%BF%87%E6%9C%9F%E7%B1%B3%E7%BA%BF%E7%BA%BF%E5%96%B5---6%E7%82%B9%E5%8D%8A%E7%9A%84%E6%9C%88%E4%BA%AE-64P-04-22',
    'https://telegra.ph/Fantasy-Factory-Evangelion---52P-04-24',
    'https://telegra.ph/Nagisa%E9%AD%94%E7%89%A9%E5%96%B5--%E8%B6%85%E7%B4%9A%E7%B4%A2%E5%B0%BC%E5%AD%90-48P-04-25',
    'https://telegra.ph/ATFMakerTsubaki-Album-Vol-002-%E3%82%B9%E3%82%B1%E3%82%B9%E3%82%B1%E9%9D%92%E3%81%84%E3%82%BB%E3%83%BC%E3%83%A9%E3%83%BC%E6%9C%8D-45P-04-26',
    'https://telegra.ph/%E6%B0%B4%E6%B7%BCaqua---%E6%81%B6%E9%AD%94%E5%A6%B9%E5%A6%B9-31P-05-01',
    'https://telegra.ph/%E5%A9%95%E5%93%A5-%E4%B8%8B%E6%B0%B4%E9%81%93-68P-05-05',
    'https://telegra.ph/%E9%9B%AA%E5%8B%8B%E5%92%8C%E9%98%BF%E6%9C%B1-%E6%8D%86%E7%BB%91%E5%86%99%E7%9C%9F-52P-05-06',
    'https://telegra.ph/YUZUKI-%E6%9F%9A%E6%9C%A84%E6%9C%88%E6%96%B0%E4%BD%9C-70P-05-07',
    'https://telegra.ph/YUZUKI-%E6%9F%9A%E6%9C%A85%E6%9C%88%E6%96%B0%E4%BD%9C-49P-05-08',
    'https://telegra.ph/%E6%9C%89%E5%96%B5%E9%85%B1---%E5%90%91%E9%98%B3%E5%B0%91%E5%A5%B356P-05-11',
    'https://telegra.ph/%E5%A5%88%E5%A5%88%E8%82%89---%E7%99%BD%E8%89%B2%E7%9D%A1%E8%A1%A3-37P-05-12',
    'https://telegra.ph/%E6%9D%AA%E5%A4%8F---%E5%B7%A5%E5%9C%B0%E5%88%B6%E6%9C%8D%E9%9C%B2%E5%87%BA-30P-05-23',
    'https://telegra.ph/ATF-Maker-Tsubaki-Album-Vol-014Cat-Ear-Set%E7%8C%AB%E8%80%B3%E4%B8%8B%E7%9D%80%E3%82%BB%E3%83%83%E3%83%88-42P-05-25',
    'https://telegra.ph/ATF-Maker-Tsubaki-Album-Vol-016-GYM-SUIT-Bloomers-%E4%BD%93%E6%93%8D%E6%9C%8D%E3%83%96%E3%83%AB%E3%83%9E-43P-05-26',
    'https://telegra.ph/maikeyiSmaikeyi3-33P-06-06',
    'https://telegra.ph/%E9%9D%A2%E9%A5%BC%E4%BB%99%E5%84%BF---%E9%80%B8%E4%BB%99-40P-06-08',
    'https://telegra.ph/%E9%98%BF%E8%96%B0Kaori---%E9%BB%91%E6%9A%97%E7%8E%8B%E6%9C%9D-25P-06-09',
    'https://telegra.ph/%E6%9F%9A%E6%9C%A8---E%E7%BD%A9%E6%9D%AF%E5%A4%A9%E7%84%B6%E7%BE%8E%E5%B0%91%E5%A5%B3-56P-06-09',
    'https://telegra.ph/%E6%9F%9A%E6%9C%A8---%E5%B7%A8%E4%B9%B3%E5%A8%98-40P-06-11',
    'https://telegra.ph/%E5%90%B8%E8%A1%80%E9%AC%BC%E6%98%A0%E7%94%BB-%E5%92%8C%E6%B3%89%E7%BA%B1%E9%9B%BE-47P-06-20',
    'https://telegra.ph/%E6%9F%9A%E6%9C%A8---Vol26-JKx%E7%99%BE%E5%90%88-47P-06-25',
    'https://telegra.ph/%E7%99%BD%E9%93%B681---%E7%94%9C%E7%BE%8E%E5%90%8E%E8%BE%88-130P-06-25',
    'https://telegra.ph/%E9%9B%AF%E5%A6%B9%E4%B8%8D%E8%AE%B2%E9%81%93%E7%90%86---%E5%9C%A3%E6%AF%8D-38P-06-27',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB-DVA-DLC-100P-07-06',
    'https://telegra.ph/Cazi-%E5%A7%AC%E7%BA%AA-53P-07-08',
    'https://telegra.ph/%E9%97%AB%E7%9B%BC%E7%9B%BC-72P-07-12',
    'https://telegra.ph/%E6%8A%96%E5%A8%98%E5%88%A9%E4%B8%96---%E7%B2%BE%E6%B2%B9-43P-07-13',
    'https://telegra.ph/Nagisa%E9%AD%94%E7%89%A9%E5%96%B5-Vol04-85P-07-15',
    'https://telegra.ph/%E6%A1%9C%E6%A1%83%E5%96%B5---%E8%80%B3%E7%95%94%E7%9A%84%E9%A3%8E%E5%B0%8F%E5%A8%87%E5%A6%BB-61P-07-30',
    'https://telegra.ph/%E6%81%B6%E7%8A%AC-%E7%81%B0%E8%89%B2%E5%8C%85%E8%87%80%E9%92%88%E7%BB%87%E8%A1%AB-43P-03-25',
    'https://telegra.ph/Nagisa%E9%AD%94%E7%89%A9%E5%96%B5-vol10122P-03-24',
    'https://telegra.ph/%E9%9C%B2%E8%A5%BF%E5%AE%9D%E8%B4%9D---%E7%A0%B4%E6%B4%9E%E7%89%9B%E4%BB%94%E8%A3%A4-24P-03-22',
    'https://telegra.ph/%E6%9D%AA%E5%A4%8F---%E6%B4%9B%E4%B8%BD%E5%A1%94-101P-03-20',
    'https://telegra.ph/XiuRen---N01771-%E6%9D%A8%E6%99%A8%E6%99%A8sugar-57P-03-19',
]
web_list_5 = [
    'https://telegra.ph/%E8%BD%AF%E8%BD%AF%E9%85%B1%E7%99%BD%E8%A1%AC%E8%A1%AB-60P-11-06',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E8%BF%B7%E4%B9%8B%E5%A5%B3%E4%B8%BB%E8%A7%92X-78P-09-18',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E5%86%B2%E7%94%B0%E6%80%BB%E5%8F%B8%E5%88%9D%E5%A7%8B-76P-08-16',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E9%98%BF%E8%92%82%E6%8B%89-Altera-86P-08-05',
    'https://telegra.ph/%E6%B1%A1%E7%A5%9E%E6%98%A0%E7%94%BB--%E6%B5%B7%E7%9B%97%E7%86%8A-89P-08-04',
    'https://telegra.ph/%E7%A6%8F%E5%88%A9%E5%A7%AC-%E9%82%AA%E9%AD%94%E6%9A%96%E6%9A%96-49P-08-02',
    'https://telegra.ph/e%E6%9D%AF%E5%A5%B6%E8%8C%B6%E6%9D%8E%E5%AE%9D%E5%AE%9D-37P-08-01',
    'https://telegra.ph/AKAMI-EIGA%E7%98%BE%E5%B0%91%E5%A5%B3-70P-07-31',
    'https://telegra.ph/Yoko%E5%AE%85%E5%A4%8F-30P-07-30',
    'https://telegra.ph/%E6%9C%89%E5%B8%8C%E5%B0%91%E5%A5%B3-50P-07-27',
    'https://telegra.ph/%E5%8F%8C%E5%9F%8E%E8%AE%B0-54P-07-25',
    'https://telegra.ph/YUZUK%E6%9F%9A%E6%9C%A8%E5%AF%AB%E7%9C%9F-63P-07-24',
    'https://telegra.ph/%E5%85%94%E5%AE%9D%E5%AE%9DBABY-38P-07-24',
    'https://telegra.ph/%E6%88%91%E7%9A%84%E5%A5%B3%E5%A5%B4%E6%98%AF%E5%90%B8%E8%A1%80%E9%AC%BC-34P-07-23',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E5%B9%BC%E7%A8%9A%E5%9B%AD-49P-07-20',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E6%98%A0%E7%94%BB---%E5%8F%8B%E5%88%A9%E5%A5%88%E7%B7%92-60P-07-19',
    'https://telegra.ph/%E6%B1%A1%E7%A5%9E%E6%98%A0%E7%94%BB---%E5%B2%9B%E9%A3%8E%E5%B0%91%E5%A5%B3-80P-07-18',
    'https://telegra.ph/%E6%8F%90%E4%BA%9A%E8%A5%BF%E8%A5%BF-56P-07-17',
    'https://telegra.ph/%E7%BE%9E%E6%AC%B2%E5%A8%98%E5%A8%98%E6%B2%B9%E4%BA%AE%E8%82%89%E7%B5%B2%E7%B4%85%E8%89%B2%E9%AB%98%E8%B7%9F-44P-07-07',
    'https://telegra.ph/%E5%82%B2%E5%A8%87%E8%90%8C%E8%90%8C-35P-06-13',
    'https://telegra.ph/%E6%9E%B3%E5%A7%AC-%E6%B0%B4%E4%B8%AD%E4%BB%99%E5%AD%90-76P-06-11',
    'https://telegra.ph/%E6%83%A1%E7%8A%AC%E5%B0%8F%E5%A7%90%E5%A7%90--%E6%96%B0%E5%A8%98%E8%A3%85-33P-06-10',
    'https://telegra.ph/Cris%E9%BB%83%E7%93%9C-31P-06-10',
    'https://telegra.ph/%E5%B0%91%E5%A5%B3%E9%97%BA%E6%88%BF%E8%AF%B1%E6%83%91-36P-06-09',
    'https://telegra.ph/%E5%82%B2%E5%AC%8C%E8%90%8C%E8%90%8C-%E8%B5%A4%E8%A3%B8%E7%89%B9%E5%B7%A5-36P-06-09',
    'https://telegra.ph/%E7%B2%89%E8%89%B2%E7%B2%BE%E7%81%B5-40P-06-08',
    'https://telegra.ph/%E5%B7%A5%E5%8F%A3%E5%B0%91%E5%A5%B3-74-06-06',
    'https://telegra.ph/%E9%AD%94%E6%B3%95%E5%B0%91%E5%A5%B3%E5%B0%8F%E6%9F%A0%E6%AA%AC---%E6%B1%89%E6%9C%8D%E5%B0%8F%E8%A3%99%E5%AD%90-66P-06-04',
    'https://telegra.ph/JK%E9%BB%91%E8%84%9A%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F-70P-06-04',
    'https://telegra.ph/%E6%9D%8E%E4%B8%BD%E8%8E%8E%E6%AC%A7%E6%B4%B2%E6%9D%AF-54P-06-04',
    'https://telegra.ph/%E5%B2%9B%E9%A3%8E%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F-81P-06-05',
    'https://telegra.ph/%E8%BD%B0%E8%B6%B4%E7%8C%AB-%E7%AC%AC%E4%B8%80%E5%88%8A-34P-06-06',
    'https://telegra.ph/%E8%BD%B0%E8%B6%B4%E7%8C%AB-%E7%AC%AC2%E5%88%8A-55P-06-06',
    'https://telegra.ph/%E7%88%B1%E4%B8%BD%E4%B8%9D%E5%B0%91%E5%A5%B3-68P-06-07',
    'https://telegra.ph/%E8%BD%B0%E8%B6%B4%E7%8C%AB-%E7%AC%AC3%E5%88%8A-45P-06-08',
]
if __name__ == '__main__':
    p = Pool(12)
    for i in range(len(web_list_5)):
        print(web_list_5[i])
        p.apply_async(downloadImgs, args=(web_list_5[i],))
    print('\n====  开始下载图片  ====\n')
    p.close()
    p.join()
    print('\033[1;36;41m\n====  所有页面图片下载完成！  ====\033[0m\n')
    