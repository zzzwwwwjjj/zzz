from tkinter import *
root=Tk()
root.title('search')
root.geometry('600x600')
root.resizable(False,False)
# Label(root,text='金额').pack()
# entry1=Entry(root).pack()
# Label(root,text='时间').pack()
# var=IntVar()
lb=Listbox(root,height=4,width=4)
list=['liyuan','fasdffasd','fsadf','888']
for item in list:
    lb.insert(END,item)
 
# Label(root,text='最终').pack()
# entry2=Text(root).pack()
var=StringVar()
var.set('look here!')
label=Label(root,textvariable=var).pack()
 
#定义的函数在（）内需添加event，要不会报错显示：search函数为给定赋值位置，但有一个值要赋予。
def search(event):
    var.set(lb.get(lb.curselection()))
lb.bind('<ButtonRelease-1>',search)
lb.pack()
mainloop()
