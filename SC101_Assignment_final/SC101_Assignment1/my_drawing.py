"""
File: 
Name:
----------------------
TODO:
"""
import random
from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow( width = 1200, height = 800)

def main():
    """
    TODO:
    """
    """
    #olivedrab, sage for leaves/ saddlebrown,burlywood  for trunck
    teal for sea potentially
    moccasin for sand
    """
    background()
    island()
    sand()
    leafOne()
    leafTwo()
    leafThree()
    sun()

def background():
    sky = GRect(width = 1200, height = 350)
    sky.color = 'lightblue'
    sky.filled = True
    sky.fill_color = 'lightblue'
    window.add(sky)

    sea = GRect(1200, 450, x = 0, y = 350)
    sea.color = 'steelblue'
    sea.filled = True
    sea.fill_color = 'steelblue'
    window.add(sea)

    for i in range(500):
        xcord = random.randint(0, 1200)
        ycord = random.randint(350, 800)
        sand = GOval(5, 5, x = xcord, y = ycord)
        sand.color = 'royalblue'
        sand.filled = True
        sand.fill_color = 'royalblue'
        window.add(sand)

def island():
    treeTrunck = GRect(50, 300, x = 575, y = 400)
    treeTrunck.color = 'saddlebrown'
    treeTrunck.filled = True
    treeTrunck.fill_color = 'saddlebrown'
    window.add(treeTrunck)

    for i in range(10):
        ycord = random.randint(420, 700)
        line = GRect(50, 1, x = 575, y = ycord)
        line.color = 'beige'
        line.filled = True
        line.fill_color = 'beige'
        window.add(line)

    sand = GPolygon()
    sand.add_vertex((450, 700)) #set up the polygon
    sand.add_vertex((350, 800))
    sand.add_vertex((850, 800))
    sand.add_vertex((750, 700))
    sand.color = 'moccasin'  # depend on feeling
    sand.filled = True
    sand.fill_color = 'moccasin'
    window.add(sand)


def sand():
    for i in range(40):
        xcord = random.randint(450, 750)
        ycord = random.randint(700, 800)
        sand = GOval(3, 3, x = xcord, y = ycord)
        sand.color = 'burlywood'
        sand.filled = True
        sand.fill_color = 'burlywood'
        window.add(sand)
def leafOne():
    leaf = GPolygon()
    leaf.add_vertex((600, 400))
    leaf.add_vertex((550, 350))
    leaf.add_vertex((450, 300))
    leaf.add_vertex((350, 350))
    leaf.add_vertex((300, 400))
    leaf.add_vertex((400, 375))
    leaf.add_vertex((450, 450))
    leaf.add_vertex((500, 375))
    leaf.color = 'olivedrab'
    leaf.filled = True
    leaf.fill_color = 'olivedrab'
    window.add(leaf)


def leafTwo():
    leaf = GPolygon()
    leaf.add_vertex((900, 400))
    leaf.add_vertex((850, 350))
    leaf.add_vertex((750, 300))
    leaf.add_vertex((650, 350))
    leaf.add_vertex((600, 400))
    leaf.add_vertex((700, 375))
    leaf.add_vertex((750, 450))
    leaf.add_vertex((800, 375))
    leaf.color = 'olivedrab'
    leaf.filled = True
    leaf.fill_color = 'olivedrab'
    window.add(leaf)


def leafThree():
    leaf = GPolygon()
    leaf.add_vertex((750, 300))
    leaf.add_vertex((700, 250))
    leaf.add_vertex((600, 200))
    leaf.add_vertex((500, 250))
    leaf.add_vertex((450, 300))
    leaf.add_vertex((550, 275))
    leaf.add_vertex((600, 350))
    leaf.add_vertex((650, 275))
    leaf.color = 'olivedrab'
    leaf.filled = True
    leaf.fill_color = 'olivedrab'
    window.add(leaf)


def sun():
    sun = GOval(175, 175)
    sun.color = 'gold'
    sun.filled = True
    sun.fill_color = 'gold'
    window.add(sun, x = 20, y = 0)

if __name__ == '__main__':
    main()
