# import pyautogui
# import tkinter as tk
# from tkinter.filedialog import *

# root = tk.Tk()
# canvas1 = tk.Canvas(root, width=300, height=300)
# canvas1.pack()

# def takeScreenshot():
#     myscreenshot = pyautogui.screenshot()
#     save_path = asksaveasfilename()
#     myScreenshot.save(save_path+"_Screenshot.png")

# myButton = tk.Button(text="Take Screenshot" , command=takeScreenshot , font=10)
# canvas1.create_window(150,150,window=myButton)

# mainloop();
import tkinter as tk
from tkinter import filedialog
import pyautogui

def take_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if file_path:
            screenshot.save(file_path)
            print(f"Screenshot saved as {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    root = tk.Tk()
    root.title("Screenshot Taker")

    button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()


