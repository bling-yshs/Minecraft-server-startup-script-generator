from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("简易MC服务器启动脚本生成器")
#----------------------------------
javal = StringVar() 

def xzjaval():
    openjaval = filedialog.askopenfilename(filetypes=[("Exe Files", "*.exe")])
    javal.set(openjaval) 

Label(root,text = "Java路径:").grid(row = 0, column = 0,padx=10,pady=5)

Entry(root, textvariable = javal).grid(row = 0, column = 1,padx=10,pady=5)

Button(root, text = "选择Java路径", command = xzjaval).grid(row = 0, column = 2,padx=10,pady=5)

#----------------------------------
fwqhxl = StringVar()

def xzfwqhxl():
    openfwqhxl = filedialog.askopenfilename(filetypes=[("Jar Files", "*.jar")])
    fwqhxl.set(openfwqhxl)

Label(root,text = "服务器核心路径:").grid(row = 1, column = 0,padx=10,pady=5)

Entry(root, textvariable = fwqhxl).grid(row = 1, column = 1,padx=10,pady=5)

Button(root, text = "选择服务器核心路径", command = xzfwqhxl).grid(row = 1, column = 2,padx=10,pady=5)

#----------------------------------

Label(root,text = "最大内存(G):").grid(row = 2, column = 0,padx=10,pady=5)

maxm = Entry(root)

Label(root,text = "最小内存(G):").grid(row = 3, column = 0,padx=10,pady=5)

minm = Entry(root)

#----------------------------------
def output():
    d = maxm.get()
    x = minm.get()
    doc = open("打开我来启动游戏.bat","w")
    doc.write("@echo off\n"+"\""+javal.get()+"\" -Xms"+x+"G -Xmx"+d+"G -jar \""+fwqhxl.get()+"\"\n"+"pause")
    doc.close()

maxm.grid(row = 2, column = 1)
minm.grid(row = 3, column = 1)

Button(root, text = "生成.bat文件", command = output).grid(row = 4, column = 0,pady=10)

root.mainloop()