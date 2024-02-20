import re
from tkinter import *
import bcrypt
import json

user_info = {}
def main():
    root = Tk()
    root.geometry("3000x2000")
    root.title("credential")

    
    label = Label(root, text="register page", font = ("calibre", 25) , bg = "grey", width = "300", height = "8").pack()
    Label(text = " ", height = "4").pack()
    Label(text = "user_name ", font = ("calibre", 20)).pack()
    Entry(textvariable = user_name).pack()
    Label(text = " ", height = "4").pack()
    Label(text = "password", font = ("calibre", 20)).pack()
    Entry(textvariable = password)

    root.mainloop()
    with open("output.txt", "a") as f:
        create_username()
        create_password()
        save_password()
    f.close

def create_username():
    s = input("gmail: ")
    while not re.search(".*@.*[.]", s):
        s = input("please provide a valid gmail: ")

def create_password():
    return

def save_password():
    return

if __name__ == "__main__":
    main()
