import tkinter as tk



def main():
    '''
    主函数
    :return:
    '''
    # 调用Tk()创建主窗口
    root =tk.Tk()

    # 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
    root.geometry('450x300')

    # 主窗口标题
    root.title('mcJe版本史莱姆批量查询  by：mouren-zhang')

    text = tk.Label(root, text="种子：", fg='black', font=('Times', 10))
    # 将文本内容放置在主窗口内
    text.pack()








    #开启主循环，让窗口处于显示状态
    root.mainloop()














if __name__ == '__main__':
    main()