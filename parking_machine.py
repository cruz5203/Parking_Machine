from tkinter import Tk, Label, Button, Entry, Text, ttk

window = Tk()  # 創建主視窗
window.minsize(width=500, height=300)  # 設置視窗最小大小
window.title("停車繳費系統")  # 設置視窗標題
window.resizable(True, True)  # 設置視窗是否可以調整大小
a = ttk.Frame(window, padding=10)
# window.grid()# 創建網格佈局
window.grid_rowconfigure(0, minsize=100)  # 設置標籤

label = Label(window, text="輸入車牌", padx=10, pady=20)

# 設置標籤位置
label.grid(row=0, column=0)
# label.place(x=50, y=50)

# 設置文字輸入框
entry = Entry(window, width=30)

# 設置文字輸入框位置
entry.grid(row=0, column=1)

# 設置按鈕
button = Button(window, text="確定")

# 設置按鈕位置
button.grid(row=0, column=2)

# 設置文本
text = Text(window, width=40, height=5)

# 設置文本位置
text.grid(row=1, column=1, columnspan=2, pady=10)
label1 = Label(window, text="金額", padx=10, pady=20)
label1.grid(row=2, column=0)
entry1 = Entry(window, width=10)
entry1.grid(row=2, column=1, columnspan=2, sticky="W")

button1 = Button(window, text="確定付款")
button1.grid(row=3, column=0)
button2 = Button(window, text="取消付款")
button2.grid(row=3, column=1)

# 執行視窗循環
window.mainloop()
