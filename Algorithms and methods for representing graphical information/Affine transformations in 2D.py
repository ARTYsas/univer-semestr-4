import math
import tkinter as tk

class AffineTransformationsGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Affine transformations in 2D")
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
        self.canvas.create_polygon(self.pentagon, fill="", outline="black", tags="pentagon")

    def move_pentagon(self, dx, dy):
        self.pentagon = [(x + dx, y + dy) for x, y in self.pentagon]
        self.draw_pentagon()

    def move_up(self):
        self.move_pentagon(0, -10)

    def move_down(self):
        self.move_pentagon(0, 10)

    def rotate_pentagon(self, angle):
        cx = sum(x for x, _ in self.pentagon) / 5
        cy = sum(y for _, y in self.pentagon) / 5

        angle_rad = math.radians(angle)
        cos_val = math.cos(angle_rad)
        sin_val = math.sin(angle_rad)

        self.pentagon = [
            (
                cx + (x - cx) * cos_val - (y - cy) * sin_val,
                cy + (x - cx) * sin_val + (y - cy) * cos_val
            )
            for x, y in self.pentagon
        ]

        self.draw_pentagon()

    def stretch_pentagon(self, factor):
        cx = sum(x for x, _ in self.pentagon) / 5
        cy = sum(y for _, y in self.pentagon) / 5

        self.pentagon = [
            (
                cx + (x - cx) * factor,
                cy + (y - cy) * factor
            )
            for x, y in self.pentagon
        ]

        self.draw_pentagon()

    def create_buttons(self):
        move_up_button = tk.Button(self.root, text="Move Up", command=self.move_up)
        move_up_button.pack(side=tk.LEFT)

        move_down_button = tk.Button(self.root, text="Move Down", command=self.move_down)
        move_down_button.pack(side=tk.LEFT)

        move_left_button = tk.Button(self.root, text="Move Left", command=lambda: self.move_pentagon(-10, 0))
        move_left_button.pack(side=tk.LEFT)

        move_right_button = tk.Button(self.root, text="Move Right", command=lambda: self.move_pentagon(10, 0))
        move_right_button.pack(side=tk.LEFT)

        rotate_button = tk.Button(self.root, text="Rotate 45°", command=lambda: self.rotate_pentagon(45))
        rotate_button.pack(side=tk.LEFT)

        stretch_button = tk.Button(self.root, text="Stretch", command=lambda: self.stretch_pentagon(1.2))
        stretch_button.pack(side=tk.LEFT)

        compress_button = tk.Button(self.root, text="Compress", command=lambda: self.stretch_pentagon(0.8))
        compress_button.pack(side=tk.LEFT)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = AffineTransformationsGUI()
    gui.run()
