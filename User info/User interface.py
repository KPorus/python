import tkinter as tk
from tkinter import messagebox
import mysql.connector

root = tk.Tk()
root.geometry("800x500")
root.title("Home Page")
root.config(bg='#000000')

# ================================ neccessary function =============================
# create a table for users
def create_table():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")
    conn.commit()
    conn.close()

# taking input from sign up
def insert_user(username, email, password):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    conn.commit()
    conn.close()

# For checking the duplicate entry
def check_duplicate_entry(username, email, password):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
    result = c.fetchone()
    conn.close()
    return result is not None
# ========================== pages =============================================

# Login page==========
def login():
    loginRoot = tk.Toplevel(root)
    loginRoot.geometry("800x500")
    loginRoot.config(bg='#000000')
    loginRoot.title("Login Form")

    def goBack():
        loginRoot.destroy()  # Close the login window
        root.deiconify()  # Show the home page
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
                loginRoot.withdraw()
                profile(username)
            else:
                messagebox.showerror(title="Invalid Credentials", message="Invalid username or password")

    title = tk.Label(loginRoot, text="Login form", fg='#ffffff', bg='#000000', font=("Ariel", 18))
    title.pack(pady=10)

    userNameInput = tk.Entry(loginRoot)
    userNameInput.insert('0', 'User name')
    userNameInput.bind('<FocusIn>', clearDefaultText)
    userNameInput.bind('<FocusOut>',
                       lambda e: userNameInput.insert('0', 'User name') if userNameInput.get() == '' else None)
    userNameInput.pack(pady=10)

    userPassword = tk.Entry(loginRoot, show="")
    userPassword.insert('0', 'Enter your password')
    userPassword.bind('<FocusIn>', clearDefaultText)
    userPassword.bind('<FocusOut>',
                      lambda e: userPassword.insert('0', 'Enter your password') if userPassword.get() == '' else None)
    userPassword.bind('<Key>', lambda e: userPassword.config(show="*"))
    userPassword.pack(pady=10)

    login = tk.Button(loginRoot, text="Log in", fg='#ffffff', bg='#000000', pady=7, padx=18, command=userInput)
    login.pack(pady=5)


    back = tk.Button(loginRoot, text="Go Back", fg='#ffffff', bg='#000000', pady=7, padx=18, command=goBack)
    back.pack(pady=5)

    loginRoot.protocol("WM_DELETE_WINDOW", goBack)  # Handle window close event
    loginRoot.mainloop()

# sign up page ========
def signUp():
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
            sign.withdraw()  # Hide the sign-up window
            login()

    def clearDefaultText(event):
        if event.widget == userNameInput and userNameInput.get() == 'User Name':
            userNameInput.delete('0', 'end')
        elif event.widget == userEmailInput and userEmailInput.get() == 'Enter your email':
            userEmailInput.delete('0', 'end')
        elif event.widget == userPassword and userPassword.get() == 'Enter your password':
            userPassword.delete('0', 'end')
            userPassword.config(show="*")
    def goBack():
        sign.destroy()  # Close the sign-up window
        root.deiconify()  # Show the home page

    sign = tk.Toplevel(root)
    sign.geometry("800x500")
    sign.title("Sign Up Form")
    sign.config(bg='#000000')

    title = tk.Label(sign, text="Sign Up Form", bg='#000000', fg='#ffffff', font=("San", 18))
    title.pack(pady=10)

    userNameInput = tk.Entry(sign)
    userNameInput.insert('0', 'User Name')
    userNameInput.bind('<FocusIn>', clearDefaultText)
    userNameInput.bind('<FocusOut>',
                       lambda e: userNameInput.insert('0', 'User Name') if userNameInput.get() == '' else None)
    userNameInput.pack(pady=10)

    userEmailInput = tk.Entry(sign)
    userEmailInput.insert('0', 'Enter your email')
    userEmailInput.bind('<FocusIn>', clearDefaultText)
    userEmailInput.bind('<FocusOut>', lambda e: userEmailInput.insert('0',
                                                                      'Enter your email') if userEmailInput.get() == '' else None)
    userEmailInput.pack(pady=10)

    userPassword = tk.Entry(sign, show="")
    userPassword.insert('0', 'Enter your password')
    userPassword.bind('<FocusIn>', clearDefaultText)
    userPassword.bind('<FocusOut>',
                      lambda e: userPassword.insert('0', 'Enter your password') if userPassword.get() == '' else None)
    userPassword.bind('<Key>', lambda e: userPassword.config(show="*"))
    userPassword.pack(pady=10)

    signup = tk.Button(sign, text="Sign up", fg='#ffffff', bg='#000000', pady=8, padx=15, command=userInput)
    signup.pack(pady=5)

    create_table()  # Create the database table if it doesn't exist
    back = tk.Button(sign, text="Go Back", fg='#ffffff', bg='#000000', pady=7, padx=18, command=goBack)
    back.pack(pady=5)

    sign.protocol("WM_DELETE_WINDOW", goBack)  # Handle window close event
    sign.mainloop()

# User profile page
def profile(name):
    def userInfo():
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = %s", (name,))
        result = c.fetchone()
        conn.close()
        return result

    profile = tk.Tk()
    profile.geometry("800x500")
    profile.title("User profile")
    profile.config(bg='#000000')

    title = tk.Label(profile,text=f"Welcome {name}", bg='#000000', fg='#ffffff', font=("San", 18))
    title.pack(pady=10)
    res= userInfo()
    print(res)
    profile.mainloop()

# =========================== buttons function =============================================
# for going to login page
def goToLogin():
    root.withdraw()  # Hide the home page
    login()  # Show the login page

# For going to sign up page
def goToSignUp():
    root.withdraw()  # Hide the home page
    signUp()  # Show the sign-up page

# button of going back to login page
loginButton = tk.Button(root, text="Go To login page", fg='#ffffff', bg='#000000', pady=8, padx=15, command=goToLogin)
loginButton.pack(pady=5)

# button of going back to sign up page
signupButton = tk.Button(root, text="Go to Sign up page", fg='#ffffff', bg='#000000', pady=8, padx=15, command=goToSignUp)
signupButton.pack(pady=5)

create_table()  # Create the database table if it doesn't exist

root.mainloop()