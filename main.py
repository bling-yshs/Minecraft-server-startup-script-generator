import ctypes
from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
import base64

import requests
from bs4 import BeautifulSoup

from icon import img

# 导入库


window = Tk()
# 初始化窗口

window.withdraw()
# 隐藏窗口防止闪烁

window.title("MC服务器启动脚本生成器")
# 标题
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# 告诉操作系统使用程序自身的dpi适配
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
# 获取屏幕的缩放因子
window.tk.call('tk', 'scaling', ScaleFactor / 75)

server_button_name = StringVar()
server_button_name.set("下载服务器核心")


def download_minecraft_server():
    if check_server_exist():
        return
    download_minecraft_server_main_method()


def check_server_exist():
    # 检查服务器核心是否存在
    if os.path.exists("server.jar"):
        res = messagebox.askquestion("提示", "服务器核心已存在，是否重新下载？")
        if res == "yes":
            # 删除服务器核心
            os.remove("server.jar")
            return False
        else:
            return True
    return False


def download_minecraft_server_main_method():
    original_url = "https://mcversions.net/download/"
    new_url = original_url + mc_version.get()
    response = requests.get(new_url)
    if response.status_code != 200:
        messagebox.showerror("错误", "该网址不存在或无法访问")
        server_button_name.set("下载服务器核心")
        return
    response.encoding = 'utf-8'  # 设置编码格式为utf-8
    # 解析HTML页面标签
    soup = BeautifulSoup(response.text, 'html.parser')
    # 获取所有链接
    links = soup.find_all('a')
    # 筛选server.jar结尾的链接并输出
    for link in links:
        href = link.get('href')
        if href and href.endswith('server.jar'):
            server_button_name.set("正在下载...")
            # 下载文件
            r = requests.get(href)
            with open("server.jar", "wb") as code:
                code.write(r.content)
            server_button_name.set("下载服务器核心")
            messagebox.showinfo("下载完成", "下载完成")
            return


# 第一行
Label(window, text="原版 MC 服务器版本:").grid(row=0, column=0, padx=40, pady=5)

mc_version = Entry(window)
mc_version.grid(
    row=0, column=1, padx=40, pady=5)

Button(window, text="下载", command=download_minecraft_server, textvariable=server_button_name).grid(
    row=0, column=2, padx=10, pady=5)

# 按钮 选择Java路径


java_path = StringVar()


def select_java():
    open_java_path = filedialog.askopenfilename(
        title="请选择 Java", initialdir="C:\\Program Files\\Java", filetypes=[("Java Files", "java.exe")])
    java_path.set(open_java_path)


# 第二行
Label(window, text="Java路径:").grid(row=1, column=0, padx=40, pady=5)
# 文本 Java路径:
Entry(window, textvariable=java_path, state='readonly').grid(
    row=1, column=1, padx=40, pady=5)
# 文本框 Java路径
Button(window, text="选择Java路径", command=select_java).grid(
    row=1, column=2, padx=10, pady=5)
# 按钮 选择Java路径

# 以下第二行----------------------------------
server_path = StringVar()


def select_server_jar():
    open_server_path = filedialog.askopenfilename(
        title="请选择服务器核心", initialdir=os.getcwd(), filetypes=[("Any Files", "")])
    server_path.set(open_server_path)


Label(window, text="服务器核心路径:").grid(row=2, column=0, padx=10, pady=5)

Entry(window, textvariable=server_path, state='readonly').grid(row=2, column=1, padx=10, pady=5)

Button(window, text="选择服务器核心路径", command=select_server_jar).grid(
    row=2, column=2, padx=10, pady=5)

# 以下第三行----------------------------------

Label(window, text="最大内存(G):").grid(row=3, column=0, padx=10, pady=5)

max_memory = Entry(window)

max_memory.grid(row=3, column=1)

# 以下第四行----------------------------------

Label(window, text="最小内存(G):").grid(row=4, column=0, padx=10, pady=5)

min_memory = Entry(window)

min_memory.grid(row=4, column=1)

# 以下第五行----------------------------------
select_type = StringVar()
select_type.set("原版 | Fabric | 旧版 Forge 服务器 | 水龙头服务器")
OptionMenu(window, select_type, "原版 | Fabric | 旧版 Forge 服务器 | 水龙头服务器",
           "原版 | Fabric | 旧版 Forge 服务器 | 水龙头服务器",
           "新版 Forge 服务器", "Paper 插件服务器").grid(row=5, pady=5, padx=10, columnspan=2, sticky=N + E + W)


# 下拉框

# <生成批处理文件----------------------------------
def create_eula_txt():
    if not os.path.exists("eula.txt"):
        with open("eula.txt", "w") as doc:
            doc.write("eula=true")
    return True


def output():
    finally_select_type = select_type.get()
    a = java_path.get()
    if a == "":
        messagebox.showerror("错误", "请先选择Java路径")
        return
    b = server_path.get()
    if b == "":
        messagebox.showerror("错误", "请先选择服务器核心路径")
        return
    only_server_name = os.path.basename(server_path.get())
    x = min_memory.get()
    if x == "":
        x = "1"
    d = max_memory.get()
    if d == "":
        d = "2"
    filename = "打开我来启动游戏.bat"
    if finally_select_type == "原版 | Fabric | 旧版 Forge 服务器 | 水龙头服务器":
        with open(filename, "w") as doc:
            doc.write(f'@echo off\n"{a}" -Xms{x}G -Xmx{d}G -jar "{b}"\npause')
        create_eula_txt()
    elif finally_select_type == "新版 Forge 服务器":
        with open(filename, "w") as doc:
            doc.write(f'@echo off\n"{a}" -Xms{x}G -Xmx{d}G @"{b}"\npause')
        create_eula_txt()
    elif finally_select_type == "Paper 插件服务器":
        with open(filename, "w") as doc:
            doc.write(f'@echo off\n"{a}" -Xms{x}G -Xmx{d}G -jar {only_server_name}\npause')
        create_eula_txt()
    else:
        messagebox.showerror("错误", "未知服务器类型")
        return
    messagebox.showinfo("提示", "脚本生成成功")


# ----------------------------------生成批处理文件>


Button(window, text="生成.bat文件", command=output).grid(
    row=4, column=2, padx=10, pady=5)


# 生成.bat

# <设置窗口居中----------------------------------


def set_win_center(root):
    cur_width = root.winfo_width()
    cur_height = root.winfo_height()
    scn_w, scn_h = root.maxsize()
    cen_x = (scn_w - cur_width) / 2
    cen_y = (scn_h - cur_height) / 2
    size_xy = "%dx%d+%d+%d" % (cur_width, cur_height, cen_x, cen_y)
    root.geometry(size_xy)


window.update()
set_win_center(window)
# ----------------------------------设置窗口居中>

window.resizable(False, False)
# 不可拉伸

tmp = open("tmp.ico", "wb+")
tmp.write(base64.b64decode(img))
tmp.close()
window.iconbitmap("tmp.ico")
os.remove("tmp.ico")

window.deiconify()
# 恢复窗口显示


window.mainloop()
# 消息循环

# 打包 pyinstaller -F -w -i icon.ico main.py
