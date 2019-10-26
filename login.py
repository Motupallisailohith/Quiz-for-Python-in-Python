# %%
import tkinter as tk


def print_selection(e):
    groot.destroy()


groot = tk.Tk()
root = tk.Frame(groot)
list1 = tk.Listbox(root, selectmode="Single")
list1.insert(0, "vjlkajlkfda")
list1.insert(1, "gjkladjlkgadjsg")

button1 = tk.Button(root, text="GO!", bg="red")
button1.bind("<Button-1>", print_selection)


list1.pack()
button1.pack()
root.pack()

root.mainloop()

# %%
root.destroy()

# %%
