"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(activate)


def activate(m):
    """ Activate the bouncing ball stimulation

        tracking count to know how many times the ball pass the window
        if count >= 3, then set the ball to (START_X, START_Y)
    """
    global count
    if count < 3:
        if ball.x == START_X and ball.y == START_Y: #second check which make sure the we can't alter the ball as it move
            move()
    else:
        ball.x = START_X
        ball.y = START_Y


def move():
    """ Move the ball form  (START_X, START_Y)

        while loop make the ball move constantly

        var vy determine the vertical speed

        conditional statement within while loop chnage sthe status as ball hit window boundary
        """
    global count
    vy = 0
    count += 1
    while True:
        ball.move(VX, vy)
        vy = vy + GRAVITY
        if ball.x <= 0 or ball.y + ball.height / 2 > window.height:
            vy = - REDUCE * vy
        elif ball.x > window.width:
            ball.x = START_X
            ball.y = START_Y
            break
        pause(DELAY)


if __name__ == "__main__":
    main()
