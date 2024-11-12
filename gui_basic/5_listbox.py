from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480") # 가로 * 세로

# Listbox : 목록 위젯
listbox = Listbox(root, selectmode="extended", height=0) # extended 선택 옵션 # 0 = all
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
  # 삭제
  # listbox.delete(0) # 0 : 맨 앞, END : 맨 뒤 항목 삭제 
  
  # 갯수 확인
  # print("리스트에는", listbox.size(), "개가 있어요.") # 리스트에는 5 개가 있어요.

  # 항목 확인
  # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2)) # ('사과', '딸기', '바나나')
  
  # 선택된 항목 확인 
  print("선택된 항목 : ", listbox.curselection()) # 선택된 항목 :  (3, 4)
  
btn = Button(root, text="클릭", command=btncmd)  
btn.pack()

root.mainloop()

