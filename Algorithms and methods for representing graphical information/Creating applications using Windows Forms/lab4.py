import tkinter as tk

class DrawingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lab4")
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()
        self.current_shape = None
        self.start_x = None
        self.start_y = None

        self.canvas.bind("<Button-1>", self.on_mouse_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

        self.shape_type_var = tk.StringVar()
        self.shape_type_var.set("point")  # Default shape type

        shape_type_menu = tk.OptionMenu(self.root, self.shape_type_var, "point", "line", "rectangle", "ellipse")
        shape_type_menu.config(font=("Arial", 12), width=10, bg="lightgray", fg="black")
        shape_type_menu["menu"].config(bg="lightgray", fg="black", font=("Arial", 12))
        shape_type_menu.pack(pady=10)

    def run(self):
        self.root.mainloop()

    def on_mouse_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_drag(self, event):
        if self.current_shape:
            self.canvas.delete(self.current_shape)
        self.current_shape = self.draw_shape(event.x, event.y)

    def on_mouse_release(self, event):
        if self.current_shape:
            self.canvas.delete(self.current_shape)
        self.draw_shape(event.x, event.y)
        self.current_shape = None

    def draw_shape(self, end_x, end_y):
        if self.start_x is None or self.start_y is None:
            return

        shape_type = self.get_shape_type()
        if shape_type == "point":
            return self.canvas.create_oval(self.start_x, self.start_y, self.start_x, self.start_y, fill="black", width=2)
        elif shape_type == "line":
            return self.canvas.create_line(self.start_x, self.start_y, end_x, end_y, width=2, fill="blue")
        elif shape_type == "rectangle":
            return self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline="red", width=2)
        elif shape_type == "ellipse":
            return self.canvas.create_oval(self.start_x, self.start_y, end_x, end_y, outline="green", width=2)

    def get_shape_type(self):
        return self.shape_type_var.get()

DrawingApp().run()
