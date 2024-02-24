import re
from tkinter import *
import os
import time

lay=[]

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

class register_page(Toplevel):
    
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("register")
        x = root.winfo_x()
        y = root.winfo_y()
        self.geometry("+%d+%d" % (x - 10, y - 10))
        
        # Keep the toplevel window in front of the root window
        self.wm_transient(root)
        self.good_password = True
        self.good_username = True
        self.password = StringVar()
        self.user_name = StringVar()
        Page = self.create()
        
    def create(self):    

        Label(self, text="register page", font=("calibre", 25), bg="grey").pack()
        Label(self, text=" ", height="4").pack()
        Label(self, text="user_name ", font=("calibre", 20)).pack()
        entry_user_name = Entry(self, textvariable=self.user_name).pack()
        if not self.good_username:
            Label(self, text="provide a valid email please", fg='#f00').pack()
            
        Label(self, text=" ", height="2", width="30").pack()
        Label(self, text="password", font=("calibre", 20)).pack()
        entry_password = Entry(self, textvariable=self.password).pack()
        if not self.good_password:
            Label(self, text="provide a good password please", fg="#f00").pack()
        Button(self, text="register", command= self.create_username).pack()
        
    def create_username(self):
        if not re.search(".*@.*[.]", self.user_name.get()):
            self.good_username = False
            
        else:
            self.good_username = True
            self.create_password()
        self.clean()

    def create_password(self):
        if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', self.password.get()):
            self.good_password = False
        else:
            self.good_password = True
            self.save_password()
        self.clean()
            
    def save_password(self):
        with open("output.txt", "a") as f:
            f.write("user_name: %s \npassword: %s \n"%(self.user_name.get(), self.password.get()))
        Label(self, text = "register successful!", fg = "green").pack()
        self.update()
        time.sleep(2)
        self.close()
    
    def clean(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create()
        
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
        register_button = Button(text="register", height="5", width="15", command = self.create_register)
        register_button.place(x=240, y=100)
        close_button = Button(text = "close", height="1", width="7", command = self.close)
        close_button.place(x = 270, y = 325)
        
    def create_register(self):
        register = register_page()
        
    def close(self):
        self.destroy()
        self.update()
        
        
def main():
    global root
    root = Main_Page()
    root.mainloop()


if __name__ == "__main__":
   main()





