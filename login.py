import tkinter as tk
from tkinter import messagebox
import volcontrol as vc

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.title("Login Page")
window.configure(bg="lightblue")  


title_font = ("Arial", 20, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 14, "bold")


label_title = tk.Label(window, text="Login Page", font=title_font, bg="lightblue")
label_title.pack(pady=20)


label_username = tk.Label(window, text="Username:", font=label_font, bg="lightblue")
label_username.pack()
entry_username = tk.Entry(window, font=label_font)
entry_username.pack(pady=5)


label_password = tk.Label(window, text="Password:", font=label_font, bg="lightblue")
label_password.pack()
entry_password = tk.Entry(window, show="*", font=label_font)
entry_password.pack(pady=5)


def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful!")
        vc.main()
    else:
        messagebox.showerror("Login", "Invalid username or password")


button_login = tk.Button(window, text="Login", font=button_font, command=login)
button_login.pack(pady=20)

window.mainloop()
