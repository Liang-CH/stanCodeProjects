"""
File: babygraphics.py
Name: Ryan
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # Return value in a ratio of year_index to # of YEARS in width
    return (width//len(YEARS))*year_index


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    returns the y coordinate where the rank should be drawn.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The y coordinate of the rank.
    """
    # Return value in a ratio of rank to MAX_RANK in height
    return height*int(rank)//MAX_RANK if 0 < int(rank) <= MAX_RANK else height


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Left boundary
    canvas.create_line(0, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE, fill='black')
    # Right boundary
    canvas.create_line(0, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, fill='black')

    # Years vertical lines
    for year_index, year in enumerate(YEARS):
        x = get_x_coordinate(CANVAS_WIDTH, year_index)+GRAPH_MARGIN_SIZE
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, anchor=tkinter.NW, text=str(year))


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for index, name in enumerate(lookup_names):
        points = []
        if name in name_data:
            for year_index, year in enumerate(YEARS):
                x = get_x_coordinate(CANVAS_WIDTH, year_index)+GRAPH_MARGIN_SIZE
                # If there is no data in `year`, give a default value MAX_RANK to get `y`
                rank = name_data[name][str(year)] if str(year) in name_data[name] else MAX_RANK
                y = get_y_coordinate(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE, rank)+GRAPH_MARGIN_SIZE
                # Rank label
                rank_label = rank if str(year) in name_data[name] else '*'
                # Create text of name and its rank
                canvas.create_text(x + TEXT_DX, y, anchor=tkinter.SW, text=f'{name} {rank_label}',
                                   fill=COLORS[index % len(COLORS)])
                # Record point
                points.append((x, y))
            # Draw run chart with `points`
            run_chart(canvas, points, color=COLORS[index % len(COLORS)])


def run_chart(canvas, points, color='black'):
    """
    Given a list of points, draw the line from point to point onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        points (list[(int, int)]): A list of points to be linked.
        color (str): A color of those line.

    Returns:
        This function does not return any value.
    """
    # At least two points to draw a line
    if len(points) > 1:
        for index in range(len(points)-1):
            x1, y1 = points[index]
            x2, y2 = points[index+1]
            canvas.create_line(x1, y1, x2, y2, fill=color, width=LINE_WIDTH)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
