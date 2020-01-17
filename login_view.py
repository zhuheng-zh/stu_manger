from tkinter import  *
class view:
    def login_view1(self):
        root=Tk()
        root.title("这是我的第一个python窗体")
        root.geometry('240x240')
        lb=Label(root,text='欢迎使用学生管理系统',
                 bg='blue',
                 fg='red',
                 font=("黑体",32),
                 width=20,
                 height=2,
                 relief=RAISED)
        lb.pack()
        root.mainloop()

v=view()
v.login_view1()

