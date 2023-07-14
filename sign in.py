import tkinter as tk
import mysql.connector
from tkinter import messagebox

root = tk.Tk()
root.geometry("800x500")
root.config(bg='#000000')
root.title("Login Form")

def clearDefaultText(event):
    if event.widget == userNameInput and userNameInput.get() == 'User name':
        userNameInput.delete('0', 'end')
    elif event.widget == userPassword and userPassword.get() == 'Enter your password':
        userPassword.delete('0', 'end')
        userPassword.config(show="*")

def checkuser(username, password):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

def userInput():
    username = userNameInput.get()
    password = userPassword.get()

    if username == 'User name':
        messagebox.showerror(title="Missing Field", message="Username is missing")
    elif password == 'Enter your password':
        messagebox.showerror(title="Missing Field", message="Please enter your password")
    else:
        if checkuser(username, password):
            messagebox.showinfo(title="Login Successful", message="User logged in successfully!")
        else:
            messagebox.showerror(title="Invalid Credentials", message="Invalid username or password")

title = tk.Label(root,text="Login form", fg='#ffffff',bg='#000000', font=("Ariel",18))
title.pack(pady=10)

userNameInput = tk.Entry(root)
userNameInput.insert('0','User name')
userNameInput.bind('<FocusIn>', clearDefaultText)
userNameInput.bind('<FocusOut>',lambda e: userNameInput.insert('0','User name')  if userNameInput.get() == '' else None)
userNameInput.pack(pady=10)

userPassword = tk.Entry(root, show="")
userPassword.insert('0','Enter your password')
userPassword.bind('<FocusIn>', clearDefaultText)
userPassword.bind('<FocusOut>', lambda e: userPassword.insert('0','Enter your password') if userPassword.get()=='' else None)
userPassword.bind('<Key>', lambda e: userPassword.config(show="*"))
userPassword.pack(pady=10)

login = tk.Button(root, text="Log in", fg='#ffffff', bg='#000000', pady=7, padx=18, command=userInput)
login.pack(pady=5)

root.mainloop()
