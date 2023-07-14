import tkinter as tk
from tkinter import messagebox
import mysql.connector

def create_table():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")
    conn.commit()
    conn.close()

def insert_user(username, email, password):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    conn.commit()
    conn.close()

def check_duplicate_entry(username, email, password):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
    result = c.fetchone()
    conn.close()
    return result is not None

def userInput():
    # Get the input values
    username = userNameInput.get()
    email = userEmailInput.get()
    password = userPassword.get()

    if username == 'User Name':
        messagebox.showerror(title="Username Missing", message="Please enter your username")
    elif email == 'Enter your email':
        messagebox.showerror(title="Email Missing", message="Please enter your email")
    elif password == 'Enter your password':
        messagebox.showerror(title="Password Missing", message="Please enter your password")
    elif check_duplicate_entry(username, email, password):
        messagebox.showerror(title="Duplicate Entry", message="User with the same username or email already exists")
    else:
        insert_user(username, email, password)
        messagebox.showinfo(title="User Sign up", message="User successfully signed up!")

def clearDefaultText(event):
    if event.widget == userNameInput and userNameInput.get() == 'User Name':
        userNameInput.delete('0', 'end')
    elif event.widget == userEmailInput and userEmailInput.get() == 'Enter your email':
        userEmailInput.delete('0', 'end')
    elif event.widget == userPassword and userPassword.get() == 'Enter your password':
        userPassword.delete('0', 'end')
        userPassword.config(show="*")

root = tk.Tk()
root.geometry("800x500")
root.title("Sign Up Form")
root.config(bg='#000000')

title = tk.Label(root, text="Sign Up Form", bg='#000000', fg='#ffffff', font=("San", 18))
title.pack(pady=10)

userNameInput = tk.Entry(root)
userNameInput.insert('0', 'User Name')
userNameInput.bind('<FocusIn>', clearDefaultText)
userNameInput.bind('<FocusOut>', lambda e: userNameInput.insert('0', 'User Name') if userNameInput.get() == '' else None)
userNameInput.pack(pady=10)

userEmailInput = tk.Entry(root)
userEmailInput.insert('0', 'Enter your email')
userEmailInput.bind('<FocusIn>', clearDefaultText)
userEmailInput.bind('<FocusOut>', lambda e: userEmailInput.insert('0', 'Enter your email') if userEmailInput.get() == '' else None)
userEmailInput.pack(pady=10)

userPassword = tk.Entry(root, show="")
userPassword.insert('0', 'Enter your password')
userPassword.bind('<FocusIn>', clearDefaultText)
userPassword.bind('<FocusOut>', lambda e: userPassword.insert('0', 'Enter your password') if userPassword.get() == '' else None)
userPassword.bind('<Key>', lambda e: userPassword.config(show="*"))
userPassword.pack(pady=10)

signup = tk.Button(root, text="Sign up", fg='#ffffff', bg='#000000', pady=8, padx=15, command=userInput)
signup.pack(pady=5)

create_table()  # Create the database table if it doesn't exist

root.mainloop()
