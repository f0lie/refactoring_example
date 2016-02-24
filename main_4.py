from collections import namedtuple
from random import randrange

from display import Display

class Point():
    def __init__(self, y_pos=0, x_pos=0, y_velo=0, x_velo=0):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.x_velo = x_velo
        self.y_velo = y_velo

    def move(self):
        self.x_pos += self.x_velo
        self.y_pos += self.y_velo

    def bounce(self, grid_size):
        if self.x_pos < 0 or self.x_pos > grid_size.width - 1:
            self.x_velo *= -1
            self.x_pos += self.x_velo

        if self.y_pos < 0 or self.y_pos > grid_size.height - 1:
            self.y_velo *= -1
            self.y_pos += self.y_velo

GridSize = namedtuple('GridSize', 'height width')

def main():
    display = Display(delay=0.05)

    for _ in range(100):
        display.points.append(Point(randrange(display.height - 1),
                            randrange(display.width),
                            randrange(-1,2),
                            randrange(-1,2)
                            )
                            )

    grid_size = GridSize(display.height - 1, display.width)

    for _ in range(250):
        display.draw()
        for point in display.points:
            point.move()
            point.bounce(grid_size)

if __name__ == '__main__':
    with Display.hide_cursor():
        main()
