"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

File: extension/breakoutgraphics.py
Name: Ryan

This is my breakoutgraphics extension class. My OOP learning outcome.
"""

from functools import reduce
from campy.graphics.gcolor import GColor
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GObject
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
UP = '1'               # Mapping of direction `UP`
RIGHT = '2'            # Mapping of direction `RIGHT`
DOWN = '3'             # Mapping of direction `DOWN`
LEFT = '4'             # Mapping of direction `LEFT`


class Brick(GRect):
    def __init__(self, width, height, graphic=None, x=0, y=0, fill_color=None, physical=True):
        super().__init__(width, height, x=x, y=y)
        self._physical = physical
        if fill_color is not None:
            self.filled = True
            self.fill_color = fill_color
        self.__graphic = graphic
        if self.__graphic is not None:
            self.__graphic.add(self)
        # 是否被移除
        self.__removed = False

    @property
    def physical(self):
        return self._physical

    def touch(self):
        """
        從window中移除
        並將__removed設定為True
        """
        self.__graphic.remove(self)
        self.__removed = True

    @property
    def removed(self):
        return self.__removed


class Paddle(GRect):
    def __init__(self, width, height, graphic=None, x=0, y=0, fill_color='black', physical=True):
        super().__init__(width, height, x=x, y=y)
        self._physical = physical
        if fill_color is not None:
            self.filled = True
            self.fill_color = fill_color
        self.__graphic = graphic
        if self.__graphic is not None:
            self.__graphic.add(self)

    @property
    def physical(self):
        return self._physical

    def motion(self, mouse):
        if (self.__graphic.width - self._width//2) < mouse.x:
            new_paddle_x = self.__graphic.width - self._width
        elif mouse.x < self._width//2:
            new_paddle_x = 0
        else:
            new_paddle_x = mouse.x - self._width//2
        self.__graphic.add(self, x=new_paddle_x, y=self._y)

    def touch(self):
        # do nothing
        pass


class Ball(GOval):
    def __init__(self, graphic=None, 
                 ball_radius=BALL_RADIUS, 
                 x=0, y=0,
                 dx=0, dy=0,
                 physical=True,
                 delay=0,
                 fill_color='black'):
        super().__init__(ball_radius*2, ball_radius*2, x=x, y=y)
        self._physical = physical
        self.__graphic = graphic
        self._x_direction = 1
        self._y_direction = 1
        self._dx = dx
        self._dy = dy
        self.__ball_radius = ball_radius
        self.filled = True
        self.fill_color = fill_color
        if self.__graphic is not None:
            self.__graphic.add(self)
        self.__delay = delay

    def reset_direction(self):
        self._x_direction = 1
        self._y_direction = 1

    @property
    def physical(self):
        return self._physical

    def physics_engine(self):
        if self.__delay > 0:
            self.__delay -= 1
            return
        # x-asis move
        # Ball beyond the right boundary
        if self._dx * self._x_direction + self._x + self._width > self.__graphic.width:
            next_move_x = self.__graphic.width - (self._x + self._width)
            self._x_direction *= -1
        # Ball beyond the left boundary
        elif self._dx * self._x_direction + self._x < 0:
            next_move_x = self._x
            self._x_direction *= -1
        # Moving as usual
        else:
            next_move_x = self._dx * self._x_direction

        # y-asis move
        # Ball beyond the bottom boundary
        if self._dy * self._y_direction + self._y + self._height > self.__graphic.height:
            next_move_y = self._dy * self._y_direction  # self.__graphic.height - (self._y + self._height)
            self._y_direction *= -1

        # Ball beyond the top boundary
        elif self._dy * self._y_direction + self._y < 0:
            next_move_y = self._y
            self._y_direction *= -1
        # Moving as usual
        else:
            next_move_y = self._dy * self._y_direction
        # Move
        self.move(next_move_x, next_move_y)

        # Collision corner
        ball_upper_left = self.__graphic.get_object_at(self._x, self._y)
        ball_upper_right = self.__graphic.get_object_at(self._x + self._width, self._y)
        ball_lower_left = self.__graphic.get_object_at(self._x, self._y + self._height)
        ball_lower_right = self.__graphic.get_object_at(self._x + self._width, self._y + self._height)

        # 左上 右上
        if (ball_upper_left is not None and ball_upper_left.physical) and \
                (ball_upper_right is not None and ball_upper_right.physical):
            # 朝下運動
            if self._dy > 0:
                self._y_direction = 1
            else:
                self._y_direction = -1
        # 左上而已
        elif (ball_upper_left is not None and ball_upper_left.physical) and ball_upper_right is None:
            r = BreakoutObject.collision(ball_upper_left, self._x + self._width // 2, self._y + self._height // 2)
            for v in r:
                if BreakoutObject.on_left(v):
                    self._x_direction *= 1
                    print('左上不該在磚塊左碰撞')
                elif BreakoutObject.on_right(v):
                    if self._dx > 0:
                        self._x_direction = 1
                    else:
                        self._x_direction = -1

                if BreakoutObject.on_up(v):
                    self._y_direction *= 1
                    print('左上不該在磚塊上碰撞')
                elif BreakoutObject.downward(v):
                    if self._dy > 0:
                        self._y_direction = 1
                    else:
                        self._y_direction = -1

        # 左上 左下
        if (ball_upper_left is not None and ball_upper_left.physical) and \
                (ball_lower_left is not None and ball_lower_left.physical):
            # 朝右運動
            if self._dx > 0:
                self._x_direction = 1
            else:
                self._x_direction = -1
        # 左下
        elif (ball_lower_left is not None and ball_lower_left.physical) and ball_upper_left is None:
            r = BreakoutObject.collision(ball_lower_left, self._x + self._width // 2, self._y + self._height // 2)
            for v in r:
                if BreakoutObject.on_left(v):
                    self._x_direction *= 1
                    print('左下不該在磚塊左碰撞')
                elif BreakoutObject.on_right(v):
                    if self._dx > 0:
                        self._x_direction = 1
                    else:
                        self._x_direction = -1

                if BreakoutObject.on_up(v):
                    if self._dy > 0:
                        self._y_direction = -1
                    else:
                        self._y_direction = 1
                elif BreakoutObject.downward(v):
                    print('左下角不該在磚塊下碰撞')
        # 右下 右上
        if (ball_lower_right is not None and ball_lower_right.physical) and \
                (ball_upper_right is not None and ball_upper_right.physical):
            # 朝左運動
            if self._dx > 0:
                self._x_direction = -1
            else:
                self._x_direction = 1
        # 右上而已
        elif (ball_upper_right is not None and ball_upper_right.physical) and ball_lower_right is None:
            r = BreakoutObject.collision(ball_upper_right, self._x + self._width // 2, self._y + self._height // 2)
            for v in r:
                if BreakoutObject.on_left(v):
                    if self._dx > 0:
                        self._x_direction = -1
                    else:
                        self._x_direction = 1
                elif BreakoutObject.on_right(v):
                    print('右上角不該在磚塊右碰撞')

                if BreakoutObject.on_up(v):
                    print('右上角不該在磚塊上碰撞')
                elif BreakoutObject.downward(v):
                    if self._dy > 0:
                        self._y_direction = 1
                    else:
                        self._y_direction = -1
        # 右下 左下
        if (ball_lower_right is not None and ball_lower_right.physical) and \
                (ball_lower_left is not None and ball_lower_left.physical):
            # 朝上運動
            if self._dy > 0:
                self._y_direction = -1
            else:
                self._y_direction = 1
        # 右下
        elif (ball_lower_right is not None and ball_lower_right.physical) and ball_upper_left is None:
            r = BreakoutObject.collision(ball_lower_right, self._x + self._width // 2, self._y + self._height // 2)
            for v in r:
                if BreakoutObject.on_left(v):
                    if self._dx > 0:
                        self._x_direction = -1
                    else:
                        self._x_direction = 1
                elif BreakoutObject.on_right(v):
                    print('右下角不該在磚塊右碰撞')

                if BreakoutObject.on_up(v):
                    if self._dy > 0:
                        self._y_direction = -1
                    else:
                        self._y_direction = 1
                elif BreakoutObject.downward(v):
                    print('右下角不該在磚塊下碰撞')

        # Number of collision object
        num_collision = 0
        if ball_upper_left is not None and ball_upper_left.physical:
            num_collision += 1
        if ball_upper_right is not None and ball_upper_right.physical:
            num_collision += 1
        if ball_lower_left is not None and ball_lower_left.physical:
            num_collision += 1
        if ball_lower_right is not None and ball_lower_right.physical:
            num_collision += 1

        # Number larger than 2
        if num_collision > 2:
            if (ball_upper_left is not None and ball_upper_left.physical) and \
                    (ball_upper_right is not None and ball_upper_right.physical) and \
                    (ball_lower_left is not None and ball_lower_left.physical):
                ball_upper_right.touch()
                ball_lower_left.touch()

            elif (ball_upper_left is not None and ball_upper_left.physical) and \
                    (ball_upper_right is not None and ball_upper_right.physical) and \
                    (ball_lower_right is not None and ball_lower_right.physical):
                ball_upper_left.touch()
                ball_lower_right.touch()

            elif (ball_upper_left is not None and ball_upper_left.physical) and \
                    (ball_lower_left is not None and ball_lower_left.physical) and \
                    (ball_lower_right is not None and ball_lower_right.physical):
                ball_upper_left.touch()
                ball_lower_right.touch()

            elif (ball_upper_right is not None and ball_upper_right.physical) and \
                    (ball_lower_left is not None and ball_lower_left.physical) and \
                    (ball_lower_right is not None and ball_lower_right.physical):
                ball_upper_right.touch()
                ball_lower_left.touch()

        else:
            collision_obj = None
            # Find the closest object
            closest = -float('inf')
            # 左上角碰撞且physical is True
            if ball_upper_left is not None and ball_upper_left.physical:
                collision_obj = ball_upper_left
                closest = BreakoutObject.distance_sqr(ball_upper_left, self._x + self._width // 2,
                                                      self._y + self._height // 2)

            # 右上角碰撞且physical is True
            if ball_upper_right is not None and ball_upper_right.physical:

                if closest < BreakoutObject.distance_sqr(ball_upper_right,
                                                         self._x + self._width // 2,
                                                         self._y + self._height // 2):
                    collision_obj = ball_upper_right
            # 左下角碰撞且physical is True
            if ball_lower_left is not None and ball_lower_left.physical:
                if closest < BreakoutObject.distance_sqr(ball_lower_left,
                                                         self._x + self._width // 2,
                                                         self._y + self._height // 2):
                    collision_obj = ball_lower_left
            # 右下角碰撞且physical is True
            if ball_lower_right is not None and ball_lower_right.physical:
                if closest < BreakoutObject.distance_sqr(ball_lower_right,
                                                         self._x + self._width // 2,
                                                         self._y + self._height // 2):
                    collision_obj = ball_lower_right
            # 有碰撞物件
            if collision_obj is not None and collision_obj.physical:
                # 移除物件
                collision_obj.touch()
                # self.__graphic.remove(collision_obj)

    @property
    def dx(self):
        return self._dx

    @dx.setter
    def dx(self, new_dx):
        self._dx = new_dx

    @property
    def dy(self):
        return self._dy

    @dy.setter
    def dy(self, new_dy):
        self._dy = new_dy

    @property
    def ball_radius(self):
        return self.__ball_radius

    def touch(self):
        pass


class BreakoutGraphics:

    def __init__(self,
                 ball_radius=BALL_RADIUS,
                 paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout',
                 lives=3):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # First ball in this window
        self._ball = Ball(graphic=self.window, ball_radius=ball_radius,
                          x=self.window.width // 2 - ball_radius, y=self.window.height // 2 - ball_radius)

        # Create a paddle
        self.__paddle = Paddle(graphic=self.window,
                               x=(self.window.width - paddle_width) // 2,
                               y=self.window.height - paddle_offset - paddle_height,
                               width=paddle_width, height=paddle_height)

        # # Bricks
        # # Original Code
        # self.__bricks_list = []
        # Draw bricks
        # for row in range(brick_rows-brick_rows+1):
        #     for col in range(brick_cols-brick_cols+1):
        #         self.__bricks_list.append(Brick(graphic=self.window,
        #                       x=row * (brick_width + brick_spacing),
        #                       y=col * (brick_height + brick_spacing) + brick_offset,
        #                       width=brick_width, height=brick_height,
        #                       fill_color=GColor(255 * (brick_cols - col*2) // brick_cols if (brick_cols - col) > brick_cols//2 else 0,
        #                                         255 * col // (brick_cols//2) if col <= brick_cols//2 else 255 * (brick_cols - col) // (brick_cols//2),
        #                                         255 * col // brick_cols if col >= brick_cols//2 else 0)))
        # List comprehension
        self.__bricks_list = list(
            Brick(graphic=self.window,
                  x=row * (brick_width + brick_spacing),
                  y=col * (brick_height + brick_spacing) + brick_offset,
                  width=brick_width, height=brick_height,
                  fill_color=GColor(255 * (brick_cols - col*2) // brick_cols if (brick_cols - col) > brick_cols//2 else 0,
                                    255 * col // (brick_cols//2) if col <= brick_cols//2 else 255 * (brick_cols - col) // (brick_cols//2),
                                    255 * col // brick_cols if col >= brick_cols//2 else 0))
            for col in range(brick_cols)
            for row in range(brick_rows))

        # Initialize our mouse listeners
        self.__onmousemoved_events = []
        self.__onmousemoved_events.append(self.__paddle.motion)
        self.__onmouseclicked_events = []
        self.__onmouseclicked_events.append(self.start)

        onmousemoved(self.onmousemoved_registry)
        onmouseclicked(self.onmouseclicked_registry)

        # Lives
        self.__lives = lives
        # Game started
        self.__activate = False
        self.__gifts = []

    def onmousemoved_registry(self, mouse):
        for event in self.__onmousemoved_events:
            event(mouse)

    def onmouseclicked_registry(self, mouse):
        for event in self.__onmouseclicked_events:
            event(mouse)

    def start(self, mouse):
        """
        param mouse: Function of on mouse click event
        """
        if self.__activate is False and self.__lives > 0:
            self._ball.dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self._ball.dx = -self._ball.dx
            self._ball.dy = INITIAL_Y_SPEED
            self.__activate = True

    def refresh(self):
        self._ball.physics_engine()
        if self._ball.y+self._ball.height >= self.window.height:
            self.dead()
        if reduce(lambda x, y: x & y, list(ele.removed for ele in self.__bricks_list)):
            self.complete()
        if random.randint(1, 1000) > 996:
            self.__gifts.append(self.gift())
        for gift in self.__gifts:
            gift.physics_engine()

    @property
    def activate(self):
        return self.__activate

    def complete(self):
        self.__activate = False
        game_over_text = GLabel('Congratulations！')
        game_over_text.font = '-40'
        self.window.add(game_over_text,
                        x=self.window.width // 2 - game_over_text.width // 2,
                        y=self.window.height // 2 + game_over_text.height // 2)

    def dead(self):
        """
        Reset the position and speed of ball
        """
        # Animate stop
        self.__activate = False
        # Subtract one life
        self.__lives -= 1
        if self.__lives > 0:
            self.window.add(self._ball, x=self.window.width // 2 - self._ball.ball_radius,
                            y=self.window.height // 2 - self._ball.ball_radius)
            self._ball.dx = 0
            self._ball.dy = 0
            self._ball.reset_direction()
        else:
            game_over_text = GLabel('Game Over')
            game_over_text.font = '-70'
            self.window.add(game_over_text,
                            x=self.window.width // 2 - game_over_text.width // 2,
                            y=self.window.height // 2 + game_over_text.height // 2)

    def gift(self):
        return Ball(graphic=self.window, ball_radius=BALL_RADIUS,
                    x=self.window.width // 2 - BALL_RADIUS, y=self.window.height // 2 - BALL_RADIUS,
                    dx=random.randint(1, MAX_X_SPEED), dy=INITIAL_Y_SPEED,
                    delay=50, physical=False,
                    fill_color=GColor(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                    )

class BreakoutObject:
    """
    Some methods. Position of obj and given x, y
    """
    @staticmethod
    def collision(obj, x, y):
        """
        Collision direction of obj for given (x, y)
        :param obj: Target GObject
        :param x: Coordinate of x-asis
        :param y: Coordinate of y-asis
        :return: A string to check the collision direction
        """
        x_center = obj.x + obj.width // 2
        y_center = obj.y + obj.height // 2
        x_dif = x_center - x
        y_dif = y_center - y
        if x_dif == 0:
            if y_dif > 0:
                theta = float('inf')
            else:
                theta = -float('inf')
        else:
            theta = y_dif / x_dif
        brick_tan = obj.height / obj.width
        r = ''
        if brick_tan >= theta >= -brick_tan:
            if x > x_center:
                r += RIGHT
            else:
                r += LEFT
        if brick_tan <= theta or theta <= -brick_tan:
            if y < y_center:
                r += UP
            else:
                r += DOWN
        return r

    @staticmethod
    def on_left(direction):
        """
        Check direction is left or not
        :param direction: char mapping of direction
        :return: Direction is left or not
        """
        return direction == LEFT

    @staticmethod
    def on_right(direction):
        """
        Check direction is right or not
        :param direction: char mapping of direction
        :return: Direction is right or not
        """
        return direction == RIGHT

    @staticmethod
    def on_up(direction):
        """
        Check direction is up or not
        :param direction: char mapping of direction
        :return: Direction is up or not
        """
        return direction == UP

    @staticmethod
    def downward(direction):
        """
        Check direction is down or not
        :param direction: char mapping of direction
        :return: Direction is down or not
        """
        return direction == DOWN

    @staticmethod
    def distance_sqr(obj, x, y):
        """
        Calculate distance of the brick and (x, y)
        :param brick: Target brick
        :param x: Coordinate of x-axis
        :param y: Coordinate of y-axis
        :return: Square of distance
        """
        return (obj.x + obj._width//2 - x)**2 + (obj.y + obj._height//2 - y)**2

