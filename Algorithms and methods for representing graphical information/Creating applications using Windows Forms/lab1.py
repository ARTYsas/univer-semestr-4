import tkinter as tk
from tkinter import messagebox


class Application:
    def __init__(self):
        # Initialize the Tkinter window
        self.root = tk.Tk()
        self.root.title("Lab1")

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)

        # Create the File menu and its sub-items
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Edit", command=self.edit_action)
        self.file_menu.add_command(label="Exit", command=self.exit_action)

        # Create the Help menu and its sub-items
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Author of the program", command=self.author_action)
        self.help_menu.add_command(label="About the program", command=self.about_action)

        # Add the menus to the menu bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # Configure the root window to use the menu bar
        self.root.config(menu=self.menu_bar)

        # Create a label to display the author's name
        self.author_label = tk.Label(self.root, text="Author: ", font=("Arial", 14))
        self.author_label.pack(pady=10, padx=10)

        # Create an entry widget to enter the author's name
        self.author_entry = tk.Entry(self.root, font=("Arial", 14))
        self.author_entry.pack(pady=10, padx=10)

        # Create a button to update the author's name
        self.update_button = tk.Button(self.root, text="Update", command=self.update_author)
        self.update_button.pack(pady=10, padx=10)

    def run(self):
        # Run the Tkinter event loop
        self.root.mainloop()

    def edit_action(self):
        # Handle the "Edit" menu action
        messagebox.showinfo("File", "Edit action triggered")

    def exit_action(self):
        # Handle the "Exit" menu action
        self.root.quit()

    def author_action(self):
        # Handle the "Author of the program" menu action
        author = self.author_entry.get()
        messagebox.showinfo("Author", f"Author of the program: {author}")

    def about_action(self):
        # Handle the "About the program" menu action
        messagebox.showinfo("About", "Lab1")

    def update_author(self):
        # Update the author's name when the button is clicked
        author = self.author_entry.get()
        self.author_label.config(text=f"Author: {author}")


# Create an instance of the Application class and run the program
app = Application()
app.run()
