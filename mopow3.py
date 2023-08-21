# -*- coding: utf-8 -*-
#库
import tkinter as tk
import win32api,win32gui
import win32com.client as win32comc
import speech_recognition as sr
import os
import time
import json

data = {}

#手动控制

#new
def news():    
    nt1=tk.Text(window, height=1) 
    nt1.pack()
    nt2=tk.Text(window, height=1)
    nt2.pack()
    def pinput():
        resultp1 =nt1.get("1.0","end")[:-1]
        resultp2 =nt2.get("1.0","end")[:-1]
        data[resultp1] = resultp2
        with open('m(信息文件，勿删).json',mode='w') as  f:
            json.dump(data,f)                           
    nb1=tk.Button(window, height=1, width=30, text="Input the name and the address", command=pinput)  
    nb1.pack()
#program  
def prog():    
    pt1=tk.Text(window, height=1) 
    pt1.pack()
    def pinput():
        path = os.getcwd()
        result=pt1.get("1.0","end")[:-1]
        with open(path + r'\\m(信息文件，勿删).json',mode='r') as  f:
            data = json.load(f)
            address = data[result]
            win32api.ShellExecute(0, 'open',address , '', '', 1)                         
    pb1=tk.Button(window, height=1, width=30, text="Input the name", command=pinput)  
    pb1.pack()
#web
def webs():
    wt1=tk.Text(window, height=1) 
    wt1.pack()
    def tinput():
        result=wt1.get("1.0","end")
        y = f'https://www.{result}'
        win32api.ShellExecute(0, 'open', y, '', '', 1)    
        print('Have already opened',result)                         
    wb1=tk.Button(window, height=1, width=30, text="Input the name", command=tinput)  
    wb1.pack()
def mode():    
    mt1=tk.Text(window, height=1) 
    mt1.pack()
    def minput():
        resultm1 =mt1.get("1.0","end")[:-1]
        if resultm1 == 'study mode':
            win32api.ShellExecute(0, 'open','www.bilibili.com' , '', '', 1)
            win32api.ShellExecute(0, 'open','www.4399.com' , '', '', 1)
            win32api.ShellExecute(0, 'open','https://www.qidian.com/' , '', '', 1)
        if resultm1 == 'play mode':
            win32api.ShellExecute(0, 'open','http://www.qiusuozhilu.com/' , '', '', 1)
            win32api.ShellExecute(0, 'open','https://space.bilibili.com/1581404549/' , '', '', 1)
            win32api.ShellExecute(0, 'open','https://hgcserver.gitee.io/tools/CircuitJS1-for-giteepages/circuitjs.html' , '', '', 1)
                                   
    mb1=tk.Button(window, height=1, width=30, text="Input the mode name", command=minput)  
    mb1.pack()

#语音模式
#录音函数
def invoice():
    speak = win32comc.Dispatch("SAPI.SpVoice")
    r = sr.Recognizer()
    mic = sr.Microphone()
    #进行录音
    speak.Speak('您想打开什么')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    #进行识别
    global t1
    speak.Speak('录音结束，正在识别')
    t1 = r.recognize_google(audio, language='cmn-Hans-CN')#这样设置language可以支持中文
    speak.Speak('您的命令是打开'+t1)

def vprog():
    invoice()
    with open(path + r'\\m(信息文件，勿删).json',mode='r') as  f:
        data = json.load(f)
        address = data[t1]
        win32api.ShellExecute(0, 'open',address , '', '', 1)
def vmode():
    invoice()
    if resultm1 == 'study mode':
        win32api.ShellExecute(0, 'open','www.bilibili.com' , '', '', 1)
        win32api.ShellExecute(0, 'open','www.4399.com' , '', '', 1)
        win32api.ShellExecute(0, 'open','https://www.qidian.com/' , '', '', 1)
    if resultm1 == 'play mode':
        win32api.ShellExecute(0, 'open','http://www.qiusuozhilu.com/' , '', '', 1)
        win32api.ShellExecute(0, 'open','https://space.bilibili.com/1581404549/' , '', '', 1)
        win32api.ShellExecute(0, 'open','https://hgcserver.gitee.io/tools/CircuitJS1-for-giteepages/circuitjs.html' , '', '', 1)
#新窗体
def voicewind():
    #窗体
    voicewin =tk.Toplevel(window)
    voicewin.geometry('320x240')
    voicewin.title('voice mode')
    label = tk.Label(voicewin,text='欢迎使用语音功能.')
    label.pack()
    speak = win32comc.Dispatch("SAPI.SpVoice")
    speak.Speak('你好,欢迎使用语音功能.')
    #录音
    invoice()
    if t1 == 'program':
        vprog()
    if text == 'mode':
        vmode()
#窗口
window=tk.Tk()
window.title('mopow')
window.geometry('300x300')#窗口大小以及距离x轴与y轴的距离
#欢迎语
speak = win32comc.Dispatch("SAPI.SpVoice")
speak.Speak('您好，欢迎使用mopow.')
#菜单
#菜单创建
menus=tk.Menu(window)#在window上创建一个菜单栏menus
num1=tk.Menu(menus)#在menus上面创建一个选项栏num1
submenu = tk.Menu(num1)#二级菜单
#菜单命名
#一级
menus.add_cascade(label='File',menu=num1)#将num1命名为File
num1.add_command(label='Web',command=webs)
num1.add_command(label='Programe',command=prog)
num1.add_command(label='Mode',command=mode)
num1.add_command(label='Exit',command=window.quit)#退出命令
num1.add_command(label='voicewind',command=voicewind)#语音模式
#二级

num1.add_cascade(label='New', menu=submenu, underline=0)
#submenu.add_command(label='Web',command=)
submenu.add_command(label='Programe',command=news)
#submenu.add_command(label='Mode',command=)

#显示
window.config(menu=menus)#显示菜单
window.mainloop()#显示窗口