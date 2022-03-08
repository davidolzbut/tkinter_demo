import tkinter_demo as tk
from tkinter_demo import messagebox


def get_user_input():
    user_input = entry1.get()
    messagebox.showinfo("Pozdrav", "Ahoj " + user_input + "!")
    entry1.delete(0, tk.END)
    entry1.insert(0, "!")


window = tk.Tk()
window.geometry("200x200")
window.title("Test")

"""
Label
Entry
Button
Text

"""

label1 = tk.Label(
    text="Moje applikace",
    background="black",
    foreground="white"
)

label1.grid(row=0, column=1, columnspan=2, sticky="W")


entry1 = tk.Entry(
    width=20,
)
entry1.grid(row=1, column=1)

button1 = tk.Button(
    text="Klik!",
    bg="green",
    fg="purple",
    width=20,
    height=5,
    command=get_user_input
)

button1.grid(row=1, column=2)


window.mainloop()
