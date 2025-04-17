# Implement an 'eraser' on a canvas.
import tkinter as tk    #graphics library for buttons, drawings etc
CANVAS_WIDTH = 400        # Constants
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase(event):
    # Erase the squares when the eraser touches them
    x, y = event.x, event.y  # Get mouse position
    overlapping = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)  # Find objects under eraser
    
    for obj in overlapping:
        canvas.itemconfig(obj, fill="white")  # Change the square color to white (erase effect)

# main window
root = tk.Tk()
root.title("Grid Eraser")

# canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Draw the grid of blue squares
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        cell = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

# Bind mouse movement with left click to the erase function
canvas.bind("<B1-Motion>", erase)
root.mainloop()


    
    
