# %%
import pickle
import tkinter as tk
from tkinter import messagebox

open_users = open("users.pickle", "rb")
users = pickle.load(open_users)
open_users.close()

open_categories = open("categories.pickle", "rb")
categories = pickle.load(open_categories)
open_categories.close()


# %%


class MainApplication:
    def __init__(self, master):
        self.master = master
        self.show_login_window()

    def show_login_window(self):
        login(self.master)


class login:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Application")
        self.frame = tk.Frame(self.master, bd=100)
        self.label1 = tk.Label(self.frame, text="Already Registered?", font=("Open Sans", 14, "bold"))
        self.label2 = tk.Label(self.frame, text="Name", font=("Open Sans", 12))
        self.input1 = tk.Entry(self.frame)
        self.label3 = tk.Label(self.frame, text="Reg No", font=("Open Sans", 12))
        self.input2 = tk.Entry(self.frame)

        self.button1 = tk.Button(self.frame, text="Login")
        self.button1.bind("<Button-1>", self.login)
        self.button2 = tk.Button(self.frame, text="Skip")
        self.button2.bind("<Button-1>", self.skip)

        self.grid_all()

    def grid_all(self):
        self.label1.grid(sticky='W')
        self.label2.grid(row=2, column=0, sticky="W")
        self.input1.grid(row=2, column=0, sticky="E", padx=(50, 0))
        self.label3.grid(row=3, column=0, sticky='W')
        self.input2.grid(row=3, column=0, sticky='E')
        self.button1.grid(row=4, column=0, sticky='W', pady=(10, 0))
        self.button2.grid(row=4, column=0, sticky='E')
        self.frame.grid()

    def login(self, e):
        self.current_username = self.input1.get()
        self.current_regno = self.input2.get()
        if self.current_username in users:
            if int(self.current_regno) == users[self.current_username][0]:
                self.destroy_login_window()
                category_window(self.master, self.current_username)
            else:
                self.label1.config(text="ERROR!")
        else:
            self.label1.config(text="Not Registered! Press Skip!")

    def skip(self, e):
        self.current_username = "Guest"
        self.destroy_login_window()
        category_window(self.master, self.current_username)

    def destroy_login_window(self):
        self.frame.destroy()


class category_window:
    def __init__(self, master, username):
        self.username = username
        self.master = master
        self.master.title("Select Quiz")
        self.master.geometry("190x300")
        self.frame = tk.Frame(self.master)
        self.label = tk.Label(self.frame, text="Hey " + self.username + "!", font=("Open Sans", 13, "bold"))
        self.label1 = tk.Label(self.frame, text="Please select the category:", font=("Open Sans", 12))
        self.list = tk.Listbox(self.frame, font=("Open Sans", 12))
        self.insert_into_list()
        self.button = tk.Button(self.frame, text="GO!")
        self.button.bind("<Button-1>", self.move_to_quiz)
        self.grid_all()

    def grid_all(self):
        self.label.grid(pady=(10,0),padx=(10,0),sticky="W")
        self.label1.grid(padx=(10,0),sticky="W")
        self.list.grid(pady=(30,0))
        self.button.grid(pady=(10,0))
        self.frame.grid()

    def move_to_quiz(self, e):    
        try:
            self.selection_index = self.list.curselection()[0]
        except:
            self.selection_index = 0

        self.frame.destroy()
        quiz_window(
            self.master, categories["names"][self.selection_index], self.username)

    def insert_into_list(self):
        for i in range(0, categories["count"]):
            self.list.insert(i, categories["names"][i])


class quiz_window:
    def __init__(self, master, category, username):
        self.var = tk.IntVar()
        self.username = username
        self.master = master
        self.category = category
        self.master.title(category.title() + " Quiz")
        self.master.geometry("800x380")
        self.frame = tk.Frame(self.master, bd=100)
        self.listbox = tk.Listbox(self.frame, font=("Open Sans", 12))
        self.insert_into_listbox()
        self.listbox.bind("<ButtonRelease-1>", self.select_question)
        self.label = tk.Label(self.frame, font=("Open Sans", 14))
        self.r0 = tk.Radiobutton(self.frame, variable=self.var, value=0,font=("Open Sans", 12,"bold"))
        self.r1 = tk.Radiobutton(self.frame, variable=self.var, value=1,font=("Open Sans", 12,"bold"))
        self.r2 = tk.Radiobutton(self.frame, variable=self.var, value=2,font=("Open Sans", 12,"bold"))
        self.r3 = tk.Radiobutton(self.frame, variable=self.var, value=3,font=("Open Sans", 12,"bold"))
        self.button = tk.Button(self.frame, bg="grey",
                                text="Save", command=self.submit)
        self.button1 = tk.Button(
            self.frame, bg="grey", text="Exit", command=self.move_to_categories)
        self.button2 = tk.Button(
            self.frame, bg="grey", text="Clear", command=self.clear)
        self.grid_all()
        self.select_question("position")

    def grid_all(self):
        self.listbox.grid(row=0, column=0, sticky="W", padx=10, pady=10)
        self.label.grid(row=0, column=1, sticky="N" ,pady=(10,0))
        self.r0.grid(row=0, column=1, sticky="NW", pady=(40, 0))
        self.r1.grid(row=0, column=1, sticky="NW", pady=(60, 0))
        self.r2.grid(row=0, column=1, sticky="NW", pady=(80, 0))
        self.r3.grid(row=0, column=1, sticky="NW", pady=(100, 0))
        self.button.grid(row=0, column=1, sticky="NW", pady=(150, 0))
        self.button2.grid(row=0, column=1, sticky="N", pady=(150, 0))
        self.button1.grid(row=0, column=1, sticky="NE", pady=(150, 0))
        self.frame.grid()

    def clear(self):
        self.answers[self.current_question_index] = None
        self.button.config(text="Save", bg="grey", state="normal")

    def select_question(self, e):
        if e == "position":
            self.current_question_index = 0
        else:
            self.current_question_index = self.listbox.curselection()[0]
            if(self.answers[self.current_question_index] != None):
                self.button.config(text="Saved Option "+str(
                    self.answers[self.current_question_index] + 1)+"!", bg="green", state="disabled")
            else:
                self.button.config(text="Save", bg="grey", state="normal")

        self.label.config(
            text=self.questions[self.current_question_index]["question"])
        for i in range(0, 4):
            self.r0.config(
                text=self.questions[self.current_question_index]["options"][0])
            self.r1.config(
                text=self.questions[self.current_question_index]["options"][1])
            self.r2.config(
                text=self.questions[self.current_question_index]["options"][2])
            self.r3.config(
                text=self.questions[self.current_question_index]["options"][3])

    def submit(self):
        self.radio_selection = self.var.get()
        self.answers[self.current_question_index] = self.radio_selection
        self.button.config(
            text="Saved Option "+str(self.radio_selection + 1)+"!", bg="green", state="disabled")

    def insert_into_listbox(self):
        open_category = open(self.category+".pickle", "rb")
        self.questions = pickle.load(open_category)
        open_category.close()
        self.answers = [None]*len(self.questions)
        for i in range(0, len(self.questions)):
            self.listbox.insert(i, "Question "+str(i+1))

    def move_to_categories(self):
        self.score = 0
        self.attempted = 0
        for i in range(0, len(self.questions)):
            if(self.answers[i] != None):
                self.attempted += 1
                if(self.answers[i] == self.questions[i]["answer"]):
                    self.score += 1
        messagebox.showinfo("Score", "You got "+str(self.score) +
                            "/"+str(self.attempted)+" correct!")
        self.frame.destroy()
        category_window(self.master, self.username)

# class stats_screen:

# %%


def main():
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()



# %%
