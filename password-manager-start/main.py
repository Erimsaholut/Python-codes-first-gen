from random import randint, choice, shuffle
from tkinter import messagebox
from tkinter import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    password = password_entry.get()
    website = website_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty !")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data
                data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving new data
                json.dump(data, data_file, indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    with open("data.json", "r") as data_file:
        website = website_entry.get()
        data_file = json.load(data_file)

        if len(website) == 0:
            messagebox.showinfo(message="Please don't leave any fields empty !")
        elif website in data_file:
            email = data_file[website]["email"]
            password = data_file[website]["password"]
            messagebox.showinfo(message=f"Website: {website}\nEmail:{email}\nPassword:{password} ")
        else:
            messagebox.showinfo(message="You made typo or there is no such website in Data")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passaword Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

mail = Label(text="Website")
mail.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

email_username = Label(text="Email/Username")
email_username.grid(column=0, row=2)

email_entry = Entry(width=38)
email_entry.insert(0, "erimsaholut@hotmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate = Button(text="Generate Password", width=13, command=generate_password)
generate.grid(column=2, row=3)

generate = Button(text="Add", width=36, command=save)
generate.grid(column=1, row=4, columnspan=2)

window.mainloop()
