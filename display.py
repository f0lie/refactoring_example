from blessed import Terminal
from time import sleep

term = Terminal()

class Display():
    hide_cursor = term.hidden_cursor
    height = term.height
    width = term.width

    def __init__(self, point_list=None, delay=0.05):
        if point_list is None:
            self.points = []
        else:
            self.points = point_list
        self.delay = delay
        print(term.clear)

    def draw(self):
        for point in self.points:
            print(term.move(point.y_pos, point.x_pos) + '*')
        sleep(self.delay)
        print(term.clear)

    def __enter__(self):
        print(term.hide_cursor)
        return this

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(term.normal_cursor)
