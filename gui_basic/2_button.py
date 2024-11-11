from tkinter import *

root = Tk()
root.title("GUI program")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼22222222222222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼44444444444444444")  # 고정된 크기
btn4.pack()

#! 일반 Button에 배경색 적용안됨. (MacOS)
#! 윈도우에서는 잘 적용됨 
btn5 = Button(root, text="버튼5", fg="red", bg="yellow")
btn5.pack()

root.mainloop()
