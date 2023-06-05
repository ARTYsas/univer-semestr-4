import tkinter as tk

class SplineGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Spline by de Casteljau")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        self.points = []
        self.curve = None

        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Button-3>", self.remove_point)
        self.create_buttons()

    def add_point(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.draw_point(x, y)

        self.draw_spline()

    def remove_point(self, event):
        x, y = event.x, event.y
        for point in self.points:
            px, py = point
            if abs(px - x) <= 5 and abs(py - y) <= 5:
                self.points.remove(point)
                self.redraw_canvas()
                self.draw_spline()
                break

    def redraw_canvas(self):
        self.canvas.delete("all")
        for point in self.points:
            x, y = point
            self.draw_point(x, y)

    def draw_point(self, x, y):
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")

    def draw_spline(self):
        if self.curve:
            self.canvas.delete(self.curve)

        if len(self.points) > 1:
            curve_points = self.calculate_spline_points()
            self.curve = self.canvas.create_line(curve_points, fill="green")

    def calculate_spline_points(self):
        n = len(self.points)
        t_values = [t / 100 for t in range(101)]  # 101 points on the curve

        curve_points = []
        for t in t_values:
            q = self.points.copy()
            for r in range(1, n):
                for i in range(n - r):
                    x_i = (1 - t) * q[i][0] + t * q[i + 1][0]
                    y_i = (1 - t) * q[i][1] + t * q[i + 1][1]
                    q[i] = (x_i, y_i)
            curve_points.extend(q[0])

        return curve_points

    def clear_points(self):
        self.canvas.delete("all")
        self.points = []
        self.curve = None

    def create_buttons(self):
        clear_button = tk.Button(self.root, text="Clear Points", command=self.clear_points)
        clear_button.pack(side=tk.LEFT)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = SplineGUI()
    gui.run()
