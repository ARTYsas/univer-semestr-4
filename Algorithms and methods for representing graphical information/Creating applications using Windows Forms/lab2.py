import tkinter as tk
from tkinter import messagebox


class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("lab2")

        # Create a label for line type
        self.line_type_label = tk.Label(self.root, text="Line Type:", font=("Arial", 12))
        self.line_type_label.pack(pady=10, padx=10)

        # Create a text box for line type input
        self.line_type_entry = tk.Entry(self.root, font=("Arial", 12))
        self.line_type_entry.pack(pady=10, padx=10)

        # Create a label for geometric figure
        self.figure_label = tk.Label(self.root, text="Geometric Figure:", font=("Arial", 12))
        self.figure_label.pack(pady=10, padx=10)

        # Create a menu for geometric figure selection
        self.figure_var = tk.StringVar()
        self.figure_menu = tk.OptionMenu(self.root, self.figure_var, "Circle", "Square", "Triangle")
        self.figure_menu.config(font=("Arial", 12), width=10, fg="black")
        self.figure_menu.pack(pady=5, padx=10)

        self.figure_var.set("choose...")  # Default shape type

        # Create a button to display the result
        self.result_button = tk.Button(self.root, text="Display Result", command=self.display_result, font=("Arial", 12))
        self.result_button.pack(pady=10, padx=10)

        # Create a label to display the result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10, padx=10)

    def run(self):
        self.root.mainloop()

    def display_result(self):
        line_type = self.line_type_entry.get()
        figure = self.figure_var.get()

        if line_type and figure:
            result = f"Line Type: {line_type}, Geometric Figure: {figure}"
            self.result_label.config(text=result)
        else:
            messagebox.showwarning("Error", "Please enter the line type and select a geometric figure.")


app = Application()
app.run()
