"""
File: draw_line.py
Name: Elvis
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
circle = GOval(SIZE, SIZE)
count = 0

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(draw)


def draw(m):
    """ declare variable count to trace the number of click

        while loop make the program keep running

        var vy determine the vertical speed

        conditional statement within while loop chnage sthe status as count increase
    """
    global count
    if count % 2 == 0:
        circleCreate(m)
    else:
        lineCreate(m)
    count += 1


def circleCreate(m):
    xcord = m.x - SIZE/2
    ycord = m.y - SIZE/2
    window.add(circle, xcord, ycord)
    return xcord


def lineCreate(m):
    xcordfir = circle.x + SIZE/2 #access the corrdination of the center of circle
    ycordfir = circle.y + SIZE/2
    xcordsec = m.x
    ycordsec = m.y
    line = GLine(xcordfir, ycordfir, xcordsec, ycordsec)
    window.add(line)


if __name__ == "__main__":
    main()
