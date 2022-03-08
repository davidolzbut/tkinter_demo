import tkinter as tk
import time
from tkinter import messagebox
'''
LABEL
ENTRY
BUTTON
TEXTBOX
'''


def say_hello():
    # uzivatel_entry.insert(0, str(time.time()))
    messagebox.showerror("Say hello", uzivatel_entry.get())
    uzivatel_entry.delete(0, tk.END)
    nazev_aplikace_label.destroy()


window = tk.Tk()
window.title("První applikace")
window.geometry("500x500")

nazev_aplikace_label = tk.Label(
    text="Moje super aplikace!",
    background="black",
    foreground="white"
)
nazev_aplikace_label.grid(column=0, row=0)

uzivatel_entry = tk.Entry(
    width=20,
)
uzivatel_entry.grid(column=0, row=1)

uzivatel_button = tk.Button(
    text="Odeslat!",
    width=20,
    height=5,
    bg="blue",
    fg="green",
    command=say_hello
)
uzivatel_button.grid(column=1, row=1)

txt_vstup_uzivatel = tk.Text(
    width=20,
    height=20,
    fg="yellow",
    bg="blue",
)
txt_vstup_uzivatel.grid(column=0, columnspan=100, row=4, rowspan=100, sticky="SE")

'''
label = lbl_nazev_labelu
button = btn_nazev....
entry = ent_nzev...
text = txt_nazev...

'''

window.mainloop()
