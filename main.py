import ctypes
from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
# 导入库


window = Tk()
# 初始化窗口
window.title("MC服务器启动脚本生成器")
# 标题
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# 告诉操作系统使用程序自身的dpi适配
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
# 获取屏幕的缩放因子
window.tk.call('tk', 'scaling', ScaleFactor/75)


javapath = StringVar()
# 定义java路径变量


def seljava():
    openjavapath = filedialog.askopenfilename(
        title="请选择 Java", initialdir="C:\Program Files\Java", filetypes=[("Java Files", "java.exe")])
    javapath.set(openjavapath)
# 定义 选择Java路径 的函数


Label(window, text="Java路径:").grid(row=0, column=0, padx=40, pady=5)
# 文本 Java路径:
Entry(window, textvariable=javapath).grid(
    row=0, column=1, padx=40, pady=5)
# 文本框 Java路径
Button(window, text="选择Java路径", command=seljava).grid(
    row=0, column=2, padx=10, pady=5)
# 按钮 选择Java路径

# 以下第二行----------------------------------
serverpath = StringVar()


def selserverjar():
    openserverpath = filedialog.askopenfilename(
        title="请选择服务器核心", initialdir=os.getcwd(), filetypes=[("Any Files", "")])
    serverpath.set(openserverpath)


Label(window, text="服务器核心路径:").grid(row=1, column=0, padx=10, pady=5)

Entry(window, textvariable=serverpath).grid(row=1, column=1, padx=10, pady=5)

Button(window, text="选择服务器核心路径", command=selserverjar).grid(
    row=1, column=2, padx=10, pady=5)

# 以下第三行----------------------------------

Label(window, text="最大内存(G):").grid(row=2, column=0, padx=10, pady=5)

max_memory = Entry(window)

max_memory.grid(row=2, column=1)

# 以下第四行----------------------------------

Label(window, text="最小内存(G):").grid(row=3, column=0, padx=10, pady=5)

min_memory = Entry(window)

min_memory.grid(row=3, column=1)

# 以下第五行----------------------------------
seltype = StringVar()
seltype.set("原版 | Fabric | 旧版 Forge 服务器 | 水龙头服务器")
OptionMenu(window, seltype, "原版 | Fabric | 旧版 Forge 服务器 | 水龙头服务器", "原版 | Fabric | 旧版 Forge 服务器 | 水龙头服务器",
           "新版 Forge 服务器", "Paper 插件服务器").grid(row=4, pady=5, padx=10, columnspan=2, sticky=N+E+W)


# 下拉框

# <生成批处理文件----------------------------------


def output():
    only_server_name = os.path.basename(serverpath.get())
    finally_seltype = seltype.get()
    d = max_memory.get()
    x = min_memory.get()
    if finally_seltype == "原版 | Fabric | 旧版 Forge 服务器 | 水龙头服务器":
        doc = open("打开我来启动游戏.bat", "w")
        doc.write("@echo off\n"+"\""+javapath.get()+"\" -Xms"+x +
                  "G -Xmx"+d+"G -jar \""+serverpath.get()+"\"\n"+"pause")
    elif finally_seltype == "新版 Forge 服务器":
        doc = open("打开我来启动游戏.bat", "w")
        doc.write("@echo off\n"+"\""+javapath.get()+"\" -Xms"+x +
                  "G -Xmx"+d+"G "+"@\""+serverpath.get()+"\"\n"+"pause")
    elif finally_seltype == "Paper 插件服务器":
        doc = open("打开我来启动游戏.bat", "w")
        doc.write("@echo off\n"+"\""+javapath.get()+"\" -Xms"+x +
                  "G -Xmx"+d+"G -jar "+only_server_name+"\n"+"pause")
    else:
        print("nooooo")
    doc.close()
    messagebox.showinfo("提示", "脚本生成成功")


# ----------------------------------生成批处理文件>


Button(window, text="生成.bat文件", command=output).grid(
    row=4, column=2, padx=10, pady=5)
# 生成.bat

# <设置窗口居中----------------------------------


def set_win_center(window, curWidth="", curHight=""):
    curWidth = window.winfo_width()
    curHight = window.winfo_height()
    scn_w, scn_h = window.maxsize()
    cen_x = (scn_w - curWidth) / 2
    cen_y = (scn_h - curHight) / 2
    size_xy = "%dx%d+%d+%d" % (curWidth, curHight, cen_x, cen_y)
    window.geometry(size_xy)


window.update()
set_win_center(window)
# ----------------------------------设置窗口居中>

window.resizable(0, 0)
# 不可拉伸
window.mainloop()
# 消息循环

# 打包 pyinstaller -F -w -i icon.ico main.py
