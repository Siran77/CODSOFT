import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json

class ContactApp:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

        self.root = tk.Tk()
        self.root.title("Contact App")

        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack()

        self.contacts_listbox = tk.Listbox(self.main_frame, width=50, height=15, font=("Arial", 12))
        self.contacts_listbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.load_contacts_to_listbox()

        self.add_button = tk.Button(self.main_frame, text="Add Contact", command=self.add_contact, font=("Arial", 12))
        self.add_button.grid(row=1, column=0, padx=5, pady=5)

        self.view_button = tk.Button(self.main_frame, text="View Contact", command=self.view_contact, font=("Arial", 12))
        self.view_button.grid(row=1, column=1, padx=5, pady=5)

        self.search_entry = tk.Entry(self.main_frame, font=("Arial", 12))
        self.search_entry.grid(row=2, column=0, padx=5, pady=5)

        self.search_button = tk.Button(self.main_frame, text="Search Contact", command=self.search_contact, font=("Arial", 12))
        self.search_button.grid(row=2, column=1, padx=5, pady=5)

        self.root.mainloop()

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f, indent=4)

    def load_contacts_to_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for name in self.contacts:
            self.contacts_listbox.insert(tk.END, name)

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter Name:")
        if name:
            if name in self.contacts:
                messagebox.showerror("Error", "Contact already exists.")
                return
            phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
            email = simpledialog.askstring("Add Contact", "Enter Email:")
            address = simpledialog.askstring("Add Contact", "Enter Address:")
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            self.save_contacts()
            self.load_contacts_to_listbox()

    def view_contact(self):
        selected_contact_index = self.contacts_listbox.curselection()
        if selected_contact_index:
            selected_contact_name = self.contacts_listbox.get(selected_contact_index)
            contact_details = self.contacts[selected_contact_name]
            messagebox.showinfo(selected_contact_name, f"Phone: {contact_details['Phone']}\nEmail: {contact_details['Email']}\nAddress: {contact_details['Address']}")
        else:
            messagebox.showerror("Error", "No contact selected.")

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        if search_term:
            search_results = [name for name in self.contacts if search_term in name.lower()]
            if search_results:
                messagebox.showinfo("Search Results", "\n".join(search_results))
            else:
                messagebox.showinfo("Search Results", "No contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

if __name__ == "__main__":
    ContactApp()
