import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import ttkthemes
import requests
import json
import threading
import time
import os
import webbrowser

def Refresh():
    listOld = []
    
    while True:
        global list
        listOld = list
        list = []
        jsons = json.loads(requests.get("https://upload.deepinos.org/api/index/get_examine_list").text)["data"]
        for i in range(0, len(jsons)):
            if jsons[i]["status"] == 1:
                #text = json[i]["application_name_zh"] + "\n" + text
                list.append(jsons[i]["application_name_zh"] + " " + jsons[i]["contributor"] + " 未审核")
        if list == []:
            list.append("空")
        lablText.set("\n".join(list))
        if not list == listOld and  not list == ["空"]:
            os.system("notify-send -i spark-store '星火应用商店审核提醒' '有新的应用需要审核！'")
        time.sleep(1)

def TouGao():
    webbrowser.open_new_tab("https://upload.deepinos.org")

def ShenHe():
    messagebox.showinfo(title="提示", message="因为敏感原因，已经禁用！")

list = []
window = tk.Tk()
win = ttk.Frame(window)
control = ttk.Frame(win)
button1 = ttk.Button(control, text="打开投稿页面", command=TouGao)
button2 = ttk.Button(control, text="打开审核页面", command=ShenHe)
button1.grid(row=0, column=0, sticky=tk.W+tk.E)
button2.grid(row=0, column=1, sticky=tk.E+tk.W)
window.geometry("300x300")
themes = ttkthemes.ThemedStyle(window)
themes.set_theme("ubuntu")
lablText = tk.StringVar()
threading.Thread(target=Refresh).start()
label = ttk.Label(win, textvariable=lablText)
control.pack(fill="both")
label.pack(fill="both", expand="yes")
win.pack(fill="both", expand="yes")
window.mainloop()