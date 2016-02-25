from blessed import Terminal
from time import sleep

term = Terminal()

class Display():
    hide_cursor = term.hidden_cursor
    height = term.height
    width = term.width

    def __init__(self, delay=0.05):
        self.delay = delay
        print(term.clear)

    def draw(self, points):
        for point in points:
            print(term.move(point.y_pos, point.x_pos) + '*')
        sleep(self.delay)
        print(term.clear)
