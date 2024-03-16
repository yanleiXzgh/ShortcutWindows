import tkinter as tk
import tkinter.simpledialog as tks
import tkinter.messagebox as tkm
import win32api
import os
import json

class options():
    def new_App(self):    
        data = {}
        def pinput(resultp1,resultp2):
            with open('data.json',mode='r') as f:
                data = json.load(f)
            data[resultp1] = resultp2
            # data.append({'name': resultp1, 'address': resultp2})  # 将新数据添加到列表中
            with open('data.json',mode='w') as f:
                json.dump(data,f)                           
        resultp1 = tks.askstring("store the app", "input the name：", parent=window_root)
        resultp2 = tks.askstring("store the app", "input the address：", parent=window_root)
        pinput(resultp1,resultp2)
        tkm.showinfo(title = '',message=f"You've stored：{resultp1}")
        op.App_bottom(window_root)   
    def open_App(self):    
        def pinput(result):
            path = os.getcwd()
            with open(path + r'\\data.json',mode='r') as  f:
                data = json.load(f)
                address = data[result]
                win32api.ShellExecute(0, 'open',address , '', '', 1)                         
        result = tks.askstring("input the name", "input the name：", parent=window_root)
        pinput(result)
        tkm.showinfo(title = '',message=f"You've opened：{result}")
    
    def App_bottom(self,window_root):
        path = os.getcwd()
        def open_App(i,result):    
            win32api.ShellExecute(0, 'open',result, '', '', 1)                         
            tkm.showinfo(title = '',message=f"You've opened：{i}")
        with open(path + r'\\data.json',mode='r') as  f:
            data = json.load(f)
            for i in data:
                b = tk.Button(window_root, text=i, command=lambda:open_App(i,data[i]))
                b.pack()
    
    #web
    def open_web(self):
        def tinput(result):
            y = f'https://www.{result}.com'
            win32api.ShellExecute(0, 'open', y, '', '', 1)    
            print('Have already opened',result)                         
        result = tks.askstring("input the website", "input the website：", parent=window_root)
        tinput(result)
        tkm.showinfo(title = '',message=f"You've opened：{result}")

if __name__ == '__main__':
    op = options()