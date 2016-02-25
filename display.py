from blessed import Terminal
from time import sleep

class Display():
    term = Terminal()
    hide_cursor = term.hidden_cursor
    height = term.height
    width = term.width
    print(term.clear)

    @classmethod
    def draw(cls, points, delay=0.05):
        for point in points:
            print(cls.term.move(point.y_pos, point.x_pos) + '*')
        sleep(delay)
        print(cls.term.clear)
