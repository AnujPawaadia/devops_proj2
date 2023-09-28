import tkinter as tk
import string
import clipboard
from tkinter import ttk
import random

    
about_window = tk.Tk()
about_window.title("About")
about_window.geometry("700x600")
about_label = tk.Label(about_window, text=""" 

------------------------------------------
        Welcome to SecurePass Generator
-------------------------------------------

SecurePass Generator is a powerful tool designed to create secure and unique passwords for all your online accounts.
Whether you need a password for your email, social media, or any other online service, SecurePass Generator has you covered.

Key Features:

- Choose Password Complexity:
Customize your password by selecting options such as uppercase letters, lowercase letters, numbers, and special characters.
- Clipboard Integration:
Your generated password is automatically copied to your clipboard for easy and quick pasting into registration forms.
- Password Management: 
SecurePass Generator can also save your generated passwords in a password.txt file for future reference.

Usage Instructions:
1. Select the desired password complexity options.
2. Click the "Generate Password" button.
3. Your new password will be displayed on the terminal for easy copying.
4. The password is also copied to your clipboard automatically.
5. You can find all your generated passwords in the "password.txt" file.

Keep your online accounts safe and secure with strong, 
randomly generated passwords created by SecurePass Generator.
Never worry about weak passwords again!
-------------------------------------------
                       
                       """,font=("Times New Roman", 10))
about_label.pack()

def open_new_window():
    about_window.destroy()
    global root
    
button = tk.Button(about_window, text="Generate Password", command=open_new_window,font=("Arial", 15))
button.pack()

=======
#creating new window
def open_new_window():
    about_window.destroy()
    global root
    
button = tk.Button(about_window, text="Generate Password", command=open_new_window,font=("Arial", 15))
button.pack()

# Create the main window

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x500+700+300")

def generate_password():
    length = int(length_entry.get())
    use_upper = uppercase_var.get()
    use_lower = lowercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()_+=-[]{}|:;<>,.?/\\"

    if not characters:
        result_label.config(text="Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    clipboard.copy(password)
    result_label.config(text="Password copied to clipboard.")

def save_password():
    password = password_entry.get()
    with open("saved_passwords.txt", "a") as file:
        file.write(password + "\n")
    result_label.config(text="Password saved to 'saved_passwords.txt'.")

# Create widgets
length_label = tk.Label(root, text="Password Length:",font=("Arial", 15))
length_entry = tk.Entry(root,width=15)
uppercase_var = tk.IntVar()
lowercase_var = tk.IntVar()
digits_var = tk.IntVar()
special_var = tk.IntVar()
uppercase_cb = tk.Checkbutton(root, text="Uppercase", variable=uppercase_var,font=("Arial", 10))
lowercase_cb = tk.Checkbutton(root, text="Lowercase", variable=lowercase_var,font=("Arial", 10))
digits_cb = tk.Checkbutton(root, text="Digits", variable=digits_var,font=("Arial", 10))
special_cb = tk.Checkbutton(root, text="Special Symbols", variable=special_var,font=("Arial", 10))
generate_button = tk.Button(root, text="Generate Password", command=generate_password,font=("Arial", 10))
password_entry = tk.Entry(root,width=30)
regenerate_button = tk.Button(root, text="Regenerate", command=generate_password,font=("Arial", 10))
save_button = tk.Button(root, text="Copy and Save", command=save_password,font=("Arial", 10))
result_label = tk.Label(root, text="",font=("Arial", 10))

# Arrange widgets using grid layout
length_label.grid(row=0, column=0,columnspan=2,pady=20,)
length_entry.grid(row=0, column=2,padx=25)
uppercase_cb.grid(row=1, column=0,columnspan=3,pady=10)
lowercase_cb.grid(row=2, column=0,columnspan=3,pady=10)
digits_cb.grid(row=3, column=0,columnspan=3,pady=10)
special_cb.grid(row=4, column=0,columnspan=3,pady=10)
generate_button.grid(row=5, column=0, columnspan=3,pady=10)
password_entry.grid(row=6, column=0, columnspan=3,pady=10)
regenerate_button.grid(row=7, column=0,columnspan=2,pady=20)
save_button.grid(row=7, column=1,columnspan=2,pady=20)
result_label.grid(row=8, column=0, columnspan=3,pady=30)

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)


about_window.mainloop()
