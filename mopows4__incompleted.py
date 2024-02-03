import tkinter as tk
import tkinter.simpledialog as tks
import win32api,win32gui
import os
import win32com.client as win32comc
import json
#import speech_recognition as sr语音分析用的库
import re
import time

class options():

    def new_App(self):    
        data = {}
        def pinput(resultp1,resultp2):
            data[resultp1] = resultp2
            with open('data.json',mode='w') as  f:
                json.dump(data,f)                           
        resultp1 = tks.askstring("store the app", "input the name：", parent=window_root)
        resultp2 = tks.askstring("store the app", "input the address：", parent=window_root)
        pinput(resultp1,resultp2)
        web_ask = tk.Label(window_root, text=f"You've stored：{resultp1}")
        web_ask.pack()
    def open_App(self):    
        def pinput(result):
            path = os.getcwd()
            with open(path + r'\\data.json',mode='r') as  f:
                data = json.load(f)
                address = data[result]
                win32api.ShellExecute(0, 'open',address , '', '', 1)                         
        result = tks.askstring("input the name", "input the name：", parent=window_root)
        pinput(result)
        web_ask = tk.Label(window_root, text=f"You've opened：{result}")
        web_ask.pack()
    #web
    def open_web(self):
        def tinput(result):
            y = f'https://www.{result}.com'
            win32api.ShellExecute(0, 'open', y, '', '', 1)    
            print('Have already opened',result)                         
        result = tks.askstring("input the website", "input the website：", parent=window_root)
        tinput(result)
        web_ask = tk.Label(window_root, text=f"You've opened：{result}")
        web_ask.pack()
    #simple command
    def simpe_command(self,question):
        speak = win32comc.Dispatch("SAPI.SpVoice")
        r = sr.Recognizer()
        mic = sr.Microphone()
        #进行录音
        speak.Speak(question)
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        #进行识别
        global rely_message
        speak.Speak('Let me take a think')
        rely_message = r.recognize_google(audio, language='cmn-Hans-CN')#这样设置language可以支持中文
        speak.Speak('your command is'+rely_message)    
        print(rely_message)#调试用
    def new_mode():
    #TODO 新建一个模组
        pass

op = options()


window_root=tk.Tk()
window_root.title('mopow')
window_root.geometry('300x300')#窗口大小以及距离x轴与y轴的距离
   
#菜单
#菜单创建
menus=tk.Menu(window_root)#在window上创建一个菜单栏menus
num1=tk.Menu(menus)#在menus上面创建一个选项栏num1
    
#菜单命名
menus.add_cascade(label='File',menu=num1)#将num1命名为File
# num1.add_command(label='Web',command=op.open_web)
# num1.add_command(label='App',command=op.open_App)
num1.add_command(label='New_Mode',command= op.new_mode)
num1.add_command(label='New_app',command=op.new_App)
num1.add_command(label='Exit',command=window_root.quit)#退出命令

Web = tk.Button(text ="open a website", command = op.open_web)
Web.pack()
App = tk.Button(text ="open an app", command = op.open_App)
App.pack()

#显示
window_root.config(menu=menus)#显示菜单
window_root.mainloop()#显示窗口
