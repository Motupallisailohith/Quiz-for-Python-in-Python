#%%
import tkinter as tk
import time
import sys



# %%


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = int(time.time())
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()
    

# %%

timey
# %%
