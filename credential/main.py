import re
from tkinter import *
import bcrypt
import json

user_info = {}
def main():
    root = Tk()
    root.geometry("500x300")
    root.title("credential")

    label = Label(root, text="credential project").pack()

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
