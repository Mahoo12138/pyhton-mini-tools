import win32con
import win32api
import time

def PressCaps(key):
    if key==188 or key==190 or key==222:
        PressLow(key)
    else:
        key = key - 30
        win32api.keybd_event(16, 0, 0, 0)
        win32api.keybd_event(key, 0, 0, 0)
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0) 
        time.sleep(0.1)

def PressLow(key):
    win32api.keybd_event(key, 0, 0, 0)
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)

def PressCH(key):
    # 按下 shift
    win32api.keybd_event(16, 0, 0, 0)
    win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0) 
    win32api.keybd_event(key, 0, 0, 0)
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(16, 0, 0, 0)
    win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0) 
    time.sleep(0.1)



dic = {',':188,'.':190,'?':191,'’':222 ,'\'':222 ,' ':32,'0':48,'1':49,'2':50,'3':51,'4':52,'5':53,'6':54,'7':55,'8':56,'9':57,'!':48,'%':53,\
'a': 65, 'b': 66, 'c': 67,'d': 68,'e':69,'f': 70,'g':71,'h':72,'i':73,'j':74,'k':75,'l':76,'m':77,'n':78,\
    'o':79,'p':80,'q':81,'r':82,'s':83,'t':84,'u':85,'v':86,'w':87,'x':88,'y':89,'z':90,\
    'A': 95, 'B': 96, 'C': 97,'D': 98,'E':99,'F': 100,'G':101,'H':102,'I':103,'J':104,'K':105,'L':106,'M':107,'N':108,\
    'O':109,'P':110,'Q':111,'R':112,'S':113,'T':114,'U':115,'V':116,'W':117,'X':118,'Y':119,'Z':120,}

print('\t\t1.首先确认输入法处于英文输入模式！\n')
print('\t\t2.使用Ctrl + V 将文章粘贴入控制台内！\n')
print('\t\t3.按下回车键后，请将输入光标放到输入框内！，你将有 10 秒的时间！！！\n')

pages = str(input('请输入你的文章：'))
time.sleep(10)
for i in pages:
    for key in dic.keys():
        if (i==key) and (dic[key]>=95):
            PressCaps(dic[key])
        elif i==key:
            if i=='’':
                PressCH(222)
            PressLow(dic[key])
