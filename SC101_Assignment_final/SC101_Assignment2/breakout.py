"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import random as r


FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts
graphics = BreakoutGraphics() # create a BreakoutGraphics object


def main():
    """
    This program run a breakout game by object constructed by BreakoutGraphics class
    """
    num = NUM_LIVES
    animation(num)


def animation(n):
    """start to move the ball

     a series of conditional statements make sure the program run within the constrain

     deviation increase the difficulty by randomly change the dx and dy

    :param n: trace the number of attempts left
    """
    num = n
    while True:
        pause(FRAME_RATE)
        if graphics.t and num >0:
            # move the ball
            graphics.ball.move(graphics.getter_dx(), graphics.getter_dy())

            # check if the ball go off the boundary
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                num = num - 1
                reset(num)

            # collision check
            col = check_collision(graphics.ball.x, graphics.ball.y)
            if col:
                # include deviation so that the ball won't follow the original trajectory
                deviation = r.randint(-2, 3)
                deviation_y = r.randint(-1, 2)
                graphics.setter_dx(-1, dev=deviation)
                graphics.setter_dy(-1, dev=deviation_y)

            # wall rebound check-x
            if (graphics.ball.x + graphics.ball.width >= graphics.window.width
                    or graphics.ball.x <= 0):
                graphics.setter_dx(-1)

            # wall rebound check-y
            if graphics.ball.y <= 0:
                graphics.setter_dy(-1)

            # paddle rebound check
            if (graphics.ball.y + graphics.ball.height >= graphics.paddle.y
                    and graphics.paddle.x <= graphics.ball.x <= graphics.paddle.x + graphics.paddle.width):
                graphics.setter_dy(-1)


def check_collision(xcord, ycord):
    """check if the collision occur

    boolean det determine if collision occur

    double for loops traverse the position around the ball

    r*0.5 interval sets more sensor around the ball

    :param xcord: pass the x-coordinate of the ball
    :param ycord: pass the y-coordinate of the ball
    """
    r = graphics.ball.r
    default_xcord = int(xcord - r)
    default_ycord = int(ycord - r)
    det = False
    for i in range(-r, r + 1, int(r*0.5)):
        for j in range(-r, r + 1, int(r*0.5)):
            target_object = graphics.window.get_object_at(default_xcord + i, default_ycord + j)
            if target_object is not None and target_object is not graphics.attempt_label:
                graphics.window.remove(target_object)
                det = True
                break
            else:
                continue
    return det


def reset(num):
    """reset the ball to the original position and inactivate the graphics.t

    reset the graphics.t, so that the program would start after the mouse click

    animation() functionpull the program back to the while loop

    :param num: pass the attempts left
    """
    graphics.window.add(graphics.ball, x=(graphics.window_width - graphics.ball.r * 2) / 2, y=(
                            graphics.window_height - graphics.ball.r * 2) / 2)
    graphics.t = False
    graphics.reset_speed()
    graphics.attempt_label.text = 'Turns left: ' + str(num)
    animation(num)


if __name__ == '__main__':
    main()

