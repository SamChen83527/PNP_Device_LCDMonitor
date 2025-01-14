import tkinter as tk  # 使用Tkinter前需要先匯入
import tkinter.messagebox  # 要使用messagebox先要匯入模組
from SerialPortManager import*
import json

Device_ID = 'Level-1-Left-Corridor-G_Actuator_Monitor'

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('Fire Alert')

# 第3步，設定視窗的大小(長 * 寬)
window.geometry('2000x1200')  # 這裡的乘是小x

# 第4步，定義觸發函式功能
def show_alert ():
    # loop
    while True:
        msg = ''
        # read msg from XBee
        # task template- <DeviceID>$<msg>
        
        try:
            while True:
                msg = SerialPortManager().readMsg()
                check = msg.find('$')
                if msg != '' and check != -1:
                    msg_split = msg.strip().split('$')
                    deviceID = msg_split[0]
                    text = msg_split[1]
                    print (deviceID)
                    print (text)
                    
                    case1 = 'Left-Stairs-1-2'
                    case2 = 'Level-1-Mid-Corridor-A'
                    case3 = 'Level-1-Left-Corridor-F'
                    
                    if deviceID == Device_ID:
                        if text == case1:
                            print ('case 1')
                            tkinter.messagebox.showwarning(title='Warning', message='Warning:\n Please go upstairs for evacuation!')       # 提出警告對話窗
                            break
                        elif text == case2:
                            print ('case 2')
                            tkinter.messagebox.showwarning(title='Warning', message='Warning: Please turn right for evacuation!')       # 提出警告對話窗
                            break
                        elif text == case3:
                            print ('case 3')
                            tkinter.messagebox.showwarning(title='Warning', message='Warning: Please trun left for evacuation!')       # 提出警告對話窗
                            break
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)

tk.Button(window, text='開始火災警戒', bg='white', font=('Arial', 64), command=show_alert).pack()

window.mainloop()