"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant variable
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    # Lives to live
    lives = NUM_LIVES
    # Init BreakoutGraphics
    graphics = BreakoutGraphics(lives=lives)

    # All bricks are clear or not
    while True:
        if graphics.activate:
            graphics.refresh()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
