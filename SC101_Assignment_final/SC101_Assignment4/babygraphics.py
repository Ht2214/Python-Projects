"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
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
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
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
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # set the width between each vertical line
    width = (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    xcord = GRAPH_MARGIN_SIZE + year_index * width
    return xcord

def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    index = 0
    for t in range(0, len(YEARS)):
        xcord = get_x_coordinate(CANVAS_WIDTH, index)
        canvas.create_line(xcord, GRAPH_MARGIN_SIZE, xcord, CANVAS_HEIGHT)
        canvas.create_text(xcord, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text= str(YEARS[index]), anchor=tkinter.NW)
        index += 1


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

    # Write your code below this line
    #################################
    scale = float(CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000
    n = 0
    for name in lookup_names:
        index = len(YEARS)
        # extract the year from the name_data dictionary
        year_list = [year[0] for year in name_data.get(name).items()]
        color = COLORS[n]
        n += 1
        for interval in range(0, index - 1):
            # find the rank in the name_data dictionary
            if str(YEARS[interval]) not in year_list:
                rank = " * "  # means that the rank is over 1000
                ycord = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                rank = int(name_data.get(name)[str(YEARS[interval])])
                ycord = GRAPH_MARGIN_SIZE + scale * (rank - 1)
            # find the information in the next index
            if str(YEARS[interval + 1]) not in year_list:
                next_ycord = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                rank_next = int(name_data.get(name)[str(YEARS[interval + 1])])
                next_ycord = GRAPH_MARGIN_SIZE + scale * (rank_next - 1)

            text = name + " " + str(rank)
            # create line segment
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, interval), ycord, get_x_coordinate(CANVAS_WIDTH, interval + 1),
                               next_ycord, width=LINE_WIDTH, fill=color)
            # create text
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, interval) + TEXT_DX, ycord, text=text,
                               fill=color, anchor=tkinter.SW)
            # if it's the last segment, it would put the text on the end of the line segment
            if interval == index - 2:
                next_rank = int(name_data.get(name)[str(YEARS[interval + 1])])
                text = name + " " + str(next_rank)
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, interval + 1) + TEXT_DX, next_ycord, text=text,
                                   fill=color, anchor=tkinter.SW)


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
