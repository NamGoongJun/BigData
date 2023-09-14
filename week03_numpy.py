import numpy as np
import random
import tkinter as tk  # Built in GUI
from tkinter import messagebox # pop-up window

def click_button():
    try:
        r = int(en_row.get())
        c = int(en_column.get())

        rows = list()
        for i in range(c):
            rows.append([random.randint(1, 100) for i in range(r)])
        matrix = np.array(rows, dtype='int16')
        lbl_result.config(text=matrix)

    except ValueError as err:
        # lbl_result.config(text=f"입력 값이 없습니다.\n{err}")
        messagebox.showerror('Error', f"입력 값이 없습니다.\n{err}")


window = tk.Tk()
window.title('numpy gui version v0.7')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy array")
en_row = tk.Entry()
en_column = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

# widget layout
# lbl_result.place(x=50, y=50)
# btn_click.place(x=0, y=0)
lbl_result.grid(row=0, column=0, columnspan=2)
en_row.grid(row=1, column=0)
en_column.grid(row=1, column=1)
btn_click.grid(row=2, column=0, columnspan=2, sticky=tk.EW)


window.mainloop()
# n = int(input("input number : "))
# l = [random.randint(1, 100) for i in range(n)]
# v = np.array(l, dtype='int16')
# print(v)