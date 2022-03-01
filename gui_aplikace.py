import tkinter as tk

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
label1.pack()

window.mainloop()
