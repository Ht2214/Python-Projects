"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random as r

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
attempts = 3


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):



        # Create a graphical window, with some extra space
        self.window_width = BRICK_COLS * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (BRICK_ROWS * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width= self.window_width, height= self.window_height, title=title)

        # Create brick
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = (self.window_width + brick_spacing) / self.brick_cols
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.brick_offset = brick_offset

        #create label
        self.turns_left = 3
        self.attempt_label = GLabel('Turns left: ' + str(self.turns_left))
        self.attempt_label.font = '-20'
        self.window.add(self.attempt_label, x=0, y=self.window.height - self.attempt_label.height)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width - paddle_width) / 2,
                            y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=(self.window_width - ball_radius * 2) / 2,
                          y=(self.window_height - ball_radius * 2) / 2)
        self.ball.r = ball_radius
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = r.randint(1, MAX_X_SPEED + 1)
        if r.randint(0, 1) > 0.5:
            self.setter_dx(-1)
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        self.t = False
        onmouseclicked(self.activate)
        onmousemoved(self.mouse_paddle)

        # Draw bricks
        self.draw_brick()

    def activate(self, event):
        """ activate the object as the mouseclick
            var self.t determine whether the mouse click
        """
        self.t = True

    def draw_brick(self):
        """ draw bricks by double for loops
        var self.t determine whether the mouse click
        """
        # row influence x cord of brick
        for i in range(0, self.brick_cols):
            xcord = i * (self.brick_width + self.brick_spacing)

            # check if xcord exceed the boundary
            if xcord > self.window.width:
                continue
            for j in range(0, self.brick_rows):
                ycord = j * (self.brick_height + self.brick_spacing) + self.brick_offset

                # check if ycord exceed the boundary
                if ycord + self.brick_height > self.window.height:
                    continue

                # To make sure 2 rows would have the same color
                key = 1 + int(j / 2)
                self.color_generator(key, xcord, ycord)

    def color_generator(self, k, xcord, ycord):
        """ draw bricks by double for loops

        by using modulus % to maintain the color sequence

        :param k: key to determine the color of brick by number of row
        :param xcord: pass the x-coordinate to constructor
        :param ycord: pass the y-coordinate to constructor
        """
        brick = GRect(self.brick_width, self.brick_height, x=xcord, y=ycord)
        brick.filled = True
        key = k
        # try to make it not a magic number, change color according to the line
        if key % 5 == 1:
            brick.fill_color = "red"
        if key % 5 == 2:
            brick.fill_color = "orange"
        if key % 5== 3:
            brick.fill_color = "yellow"
        if key % 5 == 4:
            brick.fill_color = "green"
        if key % 5 == 0:
            brick.fill_color = "blue"
        self.window.add(brick)

    # throw the mouse info to the paddle in order to let it move
    def mouse_paddle(self, event):
        """ pull the mouse information to the coordinate of paddle

        Conditional statement make sure the paddle would stay in the window

        :param event: mouse information
        """
        self.paddle.x = event.x - self.paddle.width/2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif self.paddle.x >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        self.window.add(self.paddle)

    def getter_dx(self):
        return self.__dx

    def getter_dy(self):
        return self.__dy

    def setter_dx(self, var, dev=0):
        self.__dx = var * self.__dx + dev

    def setter_dy(self, var, dev=0):
        self.__dy = var * self.__dy + dev

    def reset_speed(self):
        """ reset the speed
        public method allow the client reset the modified speed to the original one
        """
        self.__dx = r.randint(1, MAX_X_SPEED + 1)
        self.__dy = INITIAL_Y_SPEED

    def attempts(self, var):
        """ update the attempts on GLabel
        public method allow the client update the attempts on
        """
        self.turns_left += var
        self.attempt_label.text('Turns left: ' + str(self.turns_left))
        return self.turns_left