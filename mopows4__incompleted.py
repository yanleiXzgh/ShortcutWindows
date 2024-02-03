import tkinter as tk
import win32api,win32gui
import os
import win32com.client as win32comc
import json
#import speech_recognition as sr语音分析用的库
import re
class options():

    def open_prog(self):    
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
    def open_web(self):
        wt1=tk.Text(window, height=1) 
        wt1.pack()
        def tinput():
            result=wt1.get("1.0","end")
            y = f'https://www.{result}'
            win32api.ShellExecute(0, 'open', y, '', '', 1)    
            print('Have already opened',result)                         
        wb1=tk.Button(window, height=1, width=30, text="Input the name", command=tinput)  
        wb1.pack()
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


window=tk.Tk()
window.title('mopow')
window.geometry('300x300')#窗口大小以及距离x轴与y轴的距离
   
#菜单
#菜单创建
menus=tk.Menu(window)#在window上创建一个菜单栏menus
num1=tk.Menu(menus)#在menus上面创建一个选项栏num1
    
#菜单命名
menus.add_cascade(label='File',menu=num1)#将num1命名为File
num1.add_command(label='Web',command=op.open_web)
num1.add_command(label='Programe',command=op.open_prog)
num1.add_command(label='New_Mode',command= op.new_mode)
num1.add_command(label='Exit',command=window.quit)#退出命令
#显示
window.config(menu=menus)#显示菜单
window.mainloop()#显示窗口
