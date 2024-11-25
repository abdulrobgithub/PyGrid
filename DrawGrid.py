import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    # Create the main window and canvas
    root = tk.Tk()
    root.title("Row of Boxes")
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    # Draw the boxes
    for i in range(N_BOXES + 1):
        canvas.create_rectangle(
            BOX_SIZE * i, 
            CANVAS_HEIGHT / 2, 
            (BOX_SIZE * i) - BOX_SIZE, 
            CANVAS_HEIGHT, 
            fill="white", 
            outline="black"
        )

    # Start the main event loop
    root.mainloop()

if __name__ == '__main__':
    main()
