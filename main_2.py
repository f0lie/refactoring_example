class Point():
    def __init__(self, x_pos=0, y_pos=0, x_velo=0, y_velo=0):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.x_velo = x_velo
        self.y_velo = y_velo

    def move(self):
        self.x_pos += self.x_velo
        self.y_pos += self.y_velo

    def bounce(self, grid_size):
        if self.x_pos < 0 or self.x_pos > grid_size - 1:
            self.x_velo *= -1
            self.x_pos += self.x_velo

        if self.y_pos < 0 or self.y_pos > grid_size - 1:
            self.y_velo *= -1
            self.y_pos += self.y_velo

GRID_SIZE = 5
grid = [[0]*GRID_SIZE for i in range(GRID_SIZE)]

point = Point(x_pos=0, y_pos=0, x_velo=0, y_velo=1)
point_1 = Point(x_pos=4, y_pos=0, x_velo=0, y_velo=1)

for i in range(5):
    grid[point.y_pos][point.x_pos] = 1
    grid[point_1.y_pos][point_1.x_pos] = 1

    for row in grid:
        print(row)
    print()

    grid[point.y_pos][point.x_pos] = 0
    grid[point_1.y_pos][point_1.x_pos] = 0

    point.move()
    point.bounce(GRID_SIZE)

    point_1.move()
    point_1.bounce(GRID_SIZE)
