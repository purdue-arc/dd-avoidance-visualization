from tkinter import *
import numpy as np

INITIAL_ROWS = 15
INITIAL_COLS = 15
grid = np.zeros((INITIAL_ROWS, INITIAL_COLS))

window = Tk()
window.title("DStar Visualization")
window.geometry("{}x{}".format(800, 700))

# create all the main containers
# top_frame = Frame(window, bg="white", width=800, height=50, pady=3)
center = Frame(window, bg="white", width=50, height=40, padx=3, pady=3)
details_frame = Frame(window, bg="white", width=50, height=40)

center.place(relx=0.5, rely=0.5, anchor=CENTER)
details_frame.grid(row=1, column=1, sticky="nsew")


# function wrapper to modify grid's dimensions
def modifyGrid(is_col, is_increasing):
    def resize():
        global grid

        old_rows = len(grid)
        old_cols = len(grid[0])
        new_rows = old_rows + (1 if is_increasing else -1) if not is_col else 0
        new_cols = old_cols + (1 if is_increasing else -1) if is_col else 0

        new_grid = np.zeros((new_rows, new_cols))

        for existing_x in range(min(old_rows, new_rows)):
            for existing_y in range(min(old_cols, new_cols)):
                new_grid[existing_x][existing_y] = grid[existing_x][existing_y]

        grid = new_grid
        # refresh()

    return resize


# initialize buttons
add_columns_btn = Button(details_frame, text="+", command=modifyGrid(True, True))
remove_columns_btn = Button(details_frame, text="-", command=modifyGrid(True, False))
add_rows_btn = Button(details_frame, text="+", command=modifyGrid(False, True))
remove_rows_btn = Button(details_frame, text="-", command=modifyGrid(False, False))

# pack buttons
add_columns_btn.pack()
remove_columns_btn.pack()
add_rows_btn.pack()
remove_rows_btn.pack()

colors = ["black", "white", "pink"]
for x in range(len(grid)):
    center.columnconfigure(x)
    center.rowconfigure(x)
    for y in range(len(grid[x])):
        boxWidth = 100
        boxHeight = 100
        box = Frame(center, bg=colors[0], width=boxWidth, height=boxHeight, borderwidth=2, relief="solid")
        box.grid(row=x, column=y, padx=4, pady=4)

        def toggleColors(toggled_box):
            def onClick(e):
                box_color = toggled_box.cget("bg")
                new_index = colors.index(box_color) + 1
                toggled_box.configure(bg=colors[new_index % len(colors)])
                grid[x][y] = new_index % len(colors)

            return onClick

        box.bind("<Button-1>", toggleColors(box))

window.mainloop()
