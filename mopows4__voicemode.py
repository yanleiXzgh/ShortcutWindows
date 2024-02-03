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


