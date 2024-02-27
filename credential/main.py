import pickle
import re
from tkinter import *
import json
import os
import time


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


class login_page(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("600x400")
        self.title("register")
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" % (x - 10, y - 10))
        self.password = StringVar()
        self.user_name = StringVar()
        self.page = self.create()

    def create(self):
        Label(self, text="login_page", font=("calibre", 25), bg="grey").pack()
        Label(self, text=" ", height="4").pack()
        Label(self, text="user_name ", font=("calibre", 20)).pack()
        self.entry_user_name = Entry(self, textvariable=self.user_name).pack()
        self.good_username = Label(self, text="", fg='#f00')
        self.good_username.pack()
        Label(self, text=" ", height="1", width="30").pack()
        Label(self, text="password", font=("calibre", 20)).pack()
        self.entry_password = Entry(self, textvariable=self.password).pack()
        self.good_password = Label(self, text="", fg="#f00")
        self.good_password.pack()
        Button(self, text="login", command=self.check_username).pack()

    def check_username(self):
        if not re.search(".*@.*[.]", self.user_name.get()) or self.user_name.get() not in info:
            self.good_username.config(text="provide a valid email please / exist email")
        else:
            self.good_username.config(text="")
            self.check_password()

    def check_password(self):
        if self.password.get() != info[self.user_name.get()]:
            self.good_password.config(text="wrong password")
        else:
            self.good_password.config(text="")
            self.login_success()

    def login_success(self):
        Label(self, text="login successful!", fg="green").pack()
        self.update()
        time.sleep(2)
        self.close()

    def close(self):
        self.destroy()
        self.update()


class register_page(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("600x400")
        self.title("register")
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" % (x - 10, y - 10))

        # Keep the toplevel window in front of the root window
        self.wm_transient(root)
        self.password = StringVar()
        self.user_name = StringVar()
        self.Page = self.create()

    def create(self):

        Label(self, text="register page", font=("calibre", 25), bg="grey").pack()
        Label(self, text=" ", height="4").pack()
        Label(self, text="user_name ", font=("calibre", 20)).pack()
        self.entry_user_name = Entry(self, textvariable=self.user_name).pack()
        self.good_username = Label(self, text="", fg='#f00')
        self.good_username.pack()
        Label(self, text=" ", height="1", width="30").pack()
        Label(self, text="password", font=("calibre", 20)).pack()
        self.entry_password = Entry(self, textvariable=self.password).pack()
        self.good_password = Label(self, text="", fg="#f00")
        self.good_password.pack()
        Button(self, text="register", command=self.create_username).pack()

    def create_username(self):
        if not re.search(".*@.*[.]", self.user_name.get()):
            self.good_username.config(text="provide a valid email please")
        else:
            self.good_username.config(text="")
            self.create_password()

    def create_password(self):
        if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', self.password.get()):
            self.good_password.config(text="provide a good password please")
        elif self.password.get() in info.values():
            self.temp = "bruh"
            for key, value in info.items():
                if str(value) == str(self.password.get()):
                    self.temp = str(key) + "has already took the password lol"
            self.good_password.config(text=self.temp)
        else:
            self.good_password.config(text="")
            self.save_password()

    def save_password(self):
        info[self.user_name.get()] = self.password.get()
        with open(filename, "wb") as f:
            pickle.dump(info, f)
        Label(self, text="register successful!", fg="green").pack()
        self.update()
        time.sleep(2)
        self.close()

    def close(self):
        self.destroy()
        self.update()


class Main_Page(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        center(self)
        self.title("credential")
        Label(text=" ", height="2", width="600", bg="grey").pack()
        register_button = Button(text="register", height="5", width="15", command=self.create_register)
        register_button.place(x=240, y=220)
        login_button = Button(text="login", height="5", width="15", command=self.create_login)
        login_button.place(x=240, y=100)
        close_button = Button(text="close", height="1", width="7", command=self.close)
        close_button.place(x=270, y=325)

    def create_register(self):
        self.register = register_page(self)

    def create_login(self):
        self.login = login_page(self)

    def close(self):
        self.destroy()
        self.update()
        with open("output.txt", "w") as f:
            for user_name, password in info.items():
                f.write("user_name: %s \npassword: %s\n\n" % (user_name, password))


def main():
    global filename
    global info
    filename = 'info.json'
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            info = pickle.load(f)
    else:
        info = {}
    global root
    root = Main_Page()
    root.mainloop()


if __name__ == "__main__":
    main()
