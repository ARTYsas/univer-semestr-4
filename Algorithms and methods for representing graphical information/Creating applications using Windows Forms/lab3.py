import tkinter as tk
from tkinter import colorchooser, simpledialog

class GraphicsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lab3")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()
        self.current_shape = None
        self.start_x = None
        self.start_y = None

        # Create a context menu
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Change Color", command=self.change_color)
        self.context_menu.add_command(label="Change Line Thickness", command=self.change_line_thickness)
        self.context_menu.add_command(label="Change Line Type", command=self.change_line_type)
        self.context_menu.add_command(label="Change Background Color", command=self.change_background_color)

        # Bind the context menu to the canvas
        self.canvas.bind("<Button-3>", self.show_context_menu)

        self.shape = self.canvas.create_rectangle(50, 50, 150, 150, fill="red")
        self.move_enabled = True
        self.move_start_x = None
        self.move_start_y = None

        # Bind the left mouse button to enable shape movement
        self.canvas.tag_bind(self.shape, "<ButtonPress-1>", self.enable_move)

    def run(self):
        self.root.mainloop()

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)

    def change_color(self):
        color = tk.colorchooser.askcolor(title="Select Color")
        if color[1]:
            self.canvas.itemconfig(self.shape, outline=color[1])

    def change_line_thickness(self):
        thickness = tk.simpledialog.askinteger("line", "Enter Line Thickness")
        if thickness:
            self.canvas.itemconfig(self.shape, width=thickness)

    def change_line_type(self):
        self.canvas.itemconfig(self.shape, dash=(4, 4))

    def change_background_color(self):
        color = tk.colorchooser.askcolor(title="Select Color")
        if color[1]:
            self.canvas.itemconfig(self.shape, fill=color[1])

    def enable_move(self, event=None):
        self.move_enabled = True
        self.move_start_x = event.x
        self.move_start_y = event.y
        self.canvas.bind("<B1-Motion>", self.move_shape)
        self.canvas.bind("<ButtonRelease-1>", self.disable_move)

    def move_shape(self, event):
        if self.move_enabled:
            dx = event.x - self.move_start_x
            dy = event.y - self.move_start_y
            self.canvas.move(self.shape, dx, dy)
            self.move_start_x = event.x
            self.move_start_y = event.y

    def disable_move(self, event):
        self.move_enabled = False
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")


app = GraphicsApp()
app.run()
