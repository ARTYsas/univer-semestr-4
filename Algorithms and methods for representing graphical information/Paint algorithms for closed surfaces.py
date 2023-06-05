import math
import tkinter as tk
from tkinter import colorchooser

class AffineTransformationsGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("fill shape")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        center_x = 250
        center_y = 250
        side_length = 200
        self.pentagon = self.calculate_equilateral_pentagon(center_x, center_y, side_length)

        self.draw_pentagon()

        self.create_buttons()

    def calculate_equilateral_pentagon(self, center_x, center_y, side_length):
        pentagon = []
        angle_deg = 270
        angle_rad = math.radians(angle_deg)
        for i in range(5):
            x = center_x + side_length * math.cos(angle_rad)
            y = center_y + side_length * math.sin(angle_rad)
            pentagon.append((x, y))
            angle_rad += (2 * math.pi / 5)

        return pentagon

    def draw_pentagon(self):
        self.canvas.delete("pentagon")
        self.canvas.create_polygon(self.pentagon, fill="white", outline="black", tags="pentagon")


    def fill_pentagon(self, x, y, fill_color):
        stack = [(x, y)]
        visited = set()

        while stack:
            x, y = stack.pop()

            if (x, y) not in visited:
                visited.add((x, y))
                current_color = self.canvas.itemcget(self.canvas.find_closest(x, y), 'fill')

                if current_color != fill_color:
                    self.canvas.itemconfigure(self.canvas.find_closest(x, y), fill=fill_color)

                    if self.is_valid_pixel(x + 1, y, fill_color):
                        stack.append((x + 1, y))
                    if self.is_valid_pixel(x - 1, y, fill_color):
                        stack.append((x - 1, y))
                    if self.is_valid_pixel(x, y + 1, fill_color):
                        stack.append((x, y + 1))
                    if self.is_valid_pixel(x, y - 1, fill_color):
                        stack.append((x, y - 1))

    def is_valid_pixel(self, x, y, fill_color):
        current_color = self.canvas.itemcget(self.canvas.find_closest(x, y), 'fill')

        # Проверка находится ли пиксель внутри пятиугольника
        if current_color == "black":
            return False

        # Проверка, не является ли пиксель уже закрашенным
        if current_color == fill_color:
            return False

        return True

    def create_buttons(self):

        fill_button = tk.Button(self.root, text="Fill", command=self.prompt_fill_color)
        fill_button.pack(side=tk.LEFT)

        clear_color_button = tk.Button(self.root, text="Clear Color", command=self.clear_fill_color)
        clear_color_button.pack(side=tk.LEFT)

    def prompt_fill_color(self):
        fill_color = colorchooser.askcolor()[1]
        x, y = self.pentagon[0]  # Затравка - берем первую вершину пятиугольника
        self.fill_pentagon(int(x), int(y), fill_color)

    def clear_fill_color(self):
        for item in self.canvas.find_withtag("pentagon"):
            self.canvas.itemconfigure(item, fill="")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = AffineTransformationsGUI()
    gui.run()
