import tkinter as tk
import basic_options
import mopows4__voicemode

op = basic_options.options()


window_root=tk.Tk()
window_root.title('mopow')
window_root.geometry('300x300')#窗口大小以及距离x轴与y轴的距离
op.App_bottom(window_root)
#菜单
#菜单创建
menus=tk.Menu(window_root)#在window上创建一个菜单栏menus
num1=tk.Menu(menus)#在menus上面创建一个选项栏num1
    
#菜单命名
menus.add_cascade(label='File',menu=num1)#将num1命名为File
# num1.add_command(label='Web',command=op.open_web)
# num1.add_command(label='App',command=op.open_App)
# num1.add_command(label='New_Mode',command= op.new_mode)
num1.add_command(label='New_app',command=op.new_App)
num1.add_command(label='Exit',command=window_root.quit)#退出命令

Web = tk.Button(text ="open a website", command = op.open_web)
Web.pack()
App = tk.Button(text ="open an app", command = op.open_App)
App.pack()

#显示
window_root.config(menu=menus)#显示菜单
window_root.mainloop()#显示窗口
