# coding=utf-8
#开进程的方法一：
import os
import re
import time
import random
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process,Pool

def test(name):
    print('%s process starts' % name)
    print('Run task %s (%s)...' % (name, os.getpid()))
    time.sleep(1)
    print('%s process ended\n' % num)

def Section_1():
    print('Main process %s.' % os.getpid())
    p1 = Process(target = test,args = ('first','1',)) #必须加,号
    Process(target = test,args = ('second','2',)).start()
    p3 = Process(target = test,args = ('third','3',))
    p4 = Process(target = test,args = ('forth','4',))

    p1.start()
    p3.start()
    p4.start()
    print('主线程')

def Section_2():
    print('Main process %s.' % os.getpid())
    p = Pool(100)
    for i in range(1,200):
        p.apply_async(test,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
if __name__ == '__main__':
    folder = "save"
    if not os.path.exists(os.getcwd() + '\\' + folder):
        os.mkdir(folder)
