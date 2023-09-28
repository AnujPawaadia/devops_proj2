import tkinter as tk
import string


    
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

about_window.mainloop()
