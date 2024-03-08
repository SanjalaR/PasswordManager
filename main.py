from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pw_sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pw_nos = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pw_list = pw_letters + pw_sym + pw_nos
    random.shuffle(pw_list)
    password = "".join(pw_list)
    en3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = en1.get()
    em = en2.get()
    pw = en3.get()

    if len(web) == 0 or len(pw) == 0:
        err = messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        ok = messagebox.askokcancel(title=web,
                                    message=f"These are the details entered: \nEmail: {em} \nPassword: {pw} \nIs it ok to save?")
        if ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{web} | {em} | {pw}\n")
            en1.delete(0, END)
            en3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

lab1 = Label(text="Website:")
lab1.grid(column=0, row=1)

lab2 = Label(text="Email/Username:")
lab2.grid(column=0, row=2)

lab3 = Label(text="Password:")
lab3.grid(column=0, row=3)

en1 = Entry(width=35)
en1.grid(column=1, row=1, columnspan=2)  # Website
en1.focus()

en2 = Entry(width=35)
en2.grid(column=1, row=2, columnspan=2)  # Email
en2.insert(0, "sanjalaramesh27@gmail.com")

en3 = Entry(width=20)
en3.grid(column=1, row=3)  # Pw

but1 = Button(text="Generate Password", command=generate)
but1.grid(column=2, row=3)

but2 = Button(text="Add", width=36, command=save)
but2.grid(column=1, row=4, columnspan=2)

window.mainloop()
