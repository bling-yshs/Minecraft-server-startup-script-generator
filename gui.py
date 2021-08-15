from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("服务器脚本生成器")
# root.geometry("640x360")
#----------------------------------

javal = StringVar() #声明Java路径为变量

def xzjaval(): #定义一个函数，函数名为选择Java路径
    openjaval = filedialog.askopenfilename(filetypes=[("Exe Files", "*.exe")]) #打开文件资源管理器，选择Java路径
    javal.set(openjaval) #将选择完的Java路径定义到第10行的Java路径里


Label(root,text = "Java路径:").grid(row = 0, column = 0,padx=10,pady=5)

Entry(root, textvariable = javal).grid(row = 0, column = 1,padx=10,pady=5)

Button(root, text = "选择Java路径", command = xzjaval).grid(row = 0, column = 2,padx=10,pady=5) #点击按钮运行第12行的函数

#------------------------------------------------------------------------------------

fwqhxl = StringVar() #声明服务器核心路径为变量

def xzfwqhxl(): #定义一个函数，函数名为选择服务器核心路径
    openfwqhxl = filedialog.askopenfilename(filetypes=[("Jar Files", "*.jar")]) #打开文件资源管理器，选择服务器核心路径
    fwqhxl.set(openfwqhxl) #将选择完的Java路径定义到第25行的Java路径里

Label(root,text = "服务器核心路径:").grid(row = 1, column = 0,padx=10,pady=5)

Entry(root, textvariable = fwqhxl).grid(row = 1, column = 1,padx=10,pady=5)

Button(root, text = "选择服务器核心路径", command = xzfwqhxl).grid(row = 1, column = 2,padx=10,pady=5) #点击按钮运行第27行的函数

#------------------------------------------------------------------------------------





Label(root,text = "最大内存:").grid(row = 2, column = 0,padx=10,pady=5)

maxm = Entry(root)

Label(root,text = "最小内存:").grid(row = 3, column = 0,padx=10,pady=5)

minm = Entry(root)



#------------------------------------------------------------------------------------

def output():
    d = maxm.get()
    x = minm.get()
    doc = open("打开我来启动游戏.bat","w")
    doc.write("@echo off\n"+"\""+javal.get()+"\" -Xms"+x+"G -Xmx"+d+"G -jar \""+fwqhxl.get()+"\"\n"+"pause>nul")
    doc.close()

maxm.grid(row = 2, column = 1)
minm.grid(row = 3, column = 1)


Button(root, text = "生成.bat文件", command = output).grid(row = 4, column = 0,pady=10)

root.mainloop()
