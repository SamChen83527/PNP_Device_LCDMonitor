import tkinter as tk  # 使用Tkinter前需要先匯入
import tkinter.messagebox  # 要使用messagebox先要匯入模組
from SerialPortManager import*
import json

Device_ID = 'Level-2-Right-Corridor-A_Actuator_Monitor'

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
                msg_split = msg.strip().split('$')
                deviceID = msg_split[0]
                text = msg_split[1]
                print (deviceID)
                print (text)
                
                case1 = 'Right-Stairs-2-1'
                case2 = 'Level-2-Mid-Corridor-E'
                case3 = 'Level-2-Right-Corridor-B'
                
                if deviceID == Device_ID:
                    if text == case1:
                        print ('case 1')
                        tkinter.messagebox.showwarning(title='Warning', message='Warning:\n Please go downstairs for evacuation!')       # 提出警告對話窗
                        break
                    elif text == case2:
                        print ('case 2')
                        tkinter.messagebox.showwarning(title='Warning', message='Warning: Please turn right for evacuation!')       # 提出警告對話窗
                        break
                    elif text == case3:
                        print ('case 3')
                        tkinter.messagebox.showwarning(title='Warning', message='Warning: Please trun left for evacuation!')       # 提出警告對話窗
                        break

tk.Button(window, text='開始火災警戒', bg='white', font=('Arial', 18), command=show_alert).pack()

window.mainloop()