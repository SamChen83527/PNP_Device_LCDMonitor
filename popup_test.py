import tkinter as tk  # 使用Tkinter前需要先匯入
import tkinter.messagebox  # 要使用messagebox先要匯入模組

# 第1步，例項化object，建立視窗window
window = tk.Tk()

# 第2步，給視窗的視覺化起名字
window.title('Fire Alert')

# 第3步，設定視窗的大小(長 * 寬)
window.geometry('1000x600')  # 這裡的乘是小x

window.wm_title("!")
label = ttk.Label(window, text=msg, font=NORM_FONT)
label.pack(side="top", fill="x", pady=10)

# 第6步，主視窗迴圈顯示
window.mainloop()