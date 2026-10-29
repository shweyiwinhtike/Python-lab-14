
import pickle
import tkinter as tk
from tkinter import filedialog

contacts = {}

root = tk.Tk()
root.withdraw()

while True:
    print("\nPhonebook Manager")
    print('Press "a" to add a new contact.')
    print('Press "-" to delete a contact.')
    print('Press "f" to find a contact.')
    print('Press "s" to save all contacts to a file.')
    print('Press "l" to load contacts from a file.')
    print('Press "p" to print all contacts.')
    print('Press "q" to quit.')

    choice = input("Enter your choice: ").lower().strip()

    if choice == "a":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == "-":
        name = input("Enter name to delete: ")
        try:
            del contacts[name]
            print("Contact deleted.")
        except KeyError:
            print("Contact not found.")

    elif choice == "f":
        name = input("Enter name to find: ")
        try:
            print(name, ":", contacts[name])
        except KeyError:
            print("Contact not found.")

    elif choice == "s":
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pkl",
            filetypes=[("Pickle files", "*.pkl")]
        )

        if file_path:
            try:
                with open(file_path, "xb") as file:
                    pickle.dump(contacts, file)
                print("Contacts saved.")
            except FileExistsError:
                print("File already exists. Choose another filename.")

    elif choice == "l":
        file_path = filedialog.askopenfilename(
            filetypes=[("Pickle files", "*.pkl")]
        )

        if file_path:
            try:
                with open(file_path, "rb") as file:
                    contacts = pickle.load(file)
                print("Contacts loaded.")
            except (FileNotFoundError, pickle.UnpicklingError, EOFError):
                print("Unable to load the file.")

    elif choice == "p":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "q":
        break

    else:
        print("Invalid choice.")

root.destroy()
