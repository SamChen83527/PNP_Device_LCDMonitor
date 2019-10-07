import tkinter as tk  # 使用Tkinter前需要先匯入
import tkinter.messagebox  # 要使用messagebox先要匯入模組
from SerialPortManager import*
import json

Device_ID = 'Level-1-Mid-Corridor-B'

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('Fire Alert')

# 第3步，設定視窗的大小(長 * 寬)
window.geometry('1000x600')  # 這裡的乘是小x

# 第4步，定義觸發函式功能
def show_alert ():
    # loop
    while True:
        msg = ''
        # read msg from XBee
        # task template- <DeviceID>$<msg>
        while True:
            msg = SerialPortManager().readMsg()
            if msg != '':
                deviceID = msg.strip().split('$')[0]
                text = msg.strip().split('$')[1]
                print (deviceID)
                print (text)
                if deviceID == Device_ID:
                    tkinter.messagebox.showwarning(title='Hi', message='警告: '+text)       # 提出警告對話窗
                    break
    # tkinter.messagebox.showinfo(title='Hi', message='你好！')              # 提示資訊對話窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告對話窗
    # tkinter.messagebox.showerror(title='Hi', message='出錯了！')         # 提出錯誤對話窗
    # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 詢問選擇對話窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'

# 第4步，在圖形介面上建立一個標籤用以顯示內容並放置
tk.Button(window, text='開始火災警戒', bg='white', font=('Arial', 18), command=show_alert).pack()

# 第6步，主視窗迴圈顯示
window.mainloop()