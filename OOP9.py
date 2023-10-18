import tkinter as tk
class circle(object):
    def __init__(self, center, radius ):
        self.center = center
        self.radius = radius

    def draw(self, canvas):
        rad = self.radius
        x1 = self.center[0] - rad
        y1 = self.center[1] - rad
        x2 = self.center[0] + rad
        y2 = self.center[1] + rad

        canvas.create_oval(x1, y1, x2, y2, fill = "green")
    def move(self, x, y):
        self.center = [x, y]
window = tk.Tk()
window.title("The Circle Shape")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Creating an instance of the Circle class
shape = circle([200, 200], 50)
shape.draw(canvas)

window.mainloop()



 



