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
        if self.x_pos < 0 or self.x_pos > grid_size - 1:
            self.x_velo *= -1
            self.x_pos += self.x_velo

        if self.y_pos < 0 or self.y_pos > grid_size - 1:
            self.y_velo *= -1
            self.y_pos += self.y_velo

class Grid():
    def __init__(self, point_list=None, grid_size=5):
        self.grid = [[0]*grid_size for i in range(grid_size)]
        self.grid_size = grid_size

        if point_list is None:
            point_list = []
        self.points = point_list

    def step(self):
        for point in self.points:
            self.grid[point.y_pos][point.x_pos] = 1

        for row in self.grid:
            print(row)
        print()

        for point in self.points:
            self.grid[point.y_pos][point.x_pos] = 0

        for point in self.points:
            point.move()
            point.bounce(self.grid_size)

GRID = Grid([Point(0, 0, 1, 1),
             Point(0, 0, 0, 1),
             Point(4, 4, -1, -1),
             Point(4, 4, 0, -1)],
            grid_size=5)

for i in range(5):
    GRID.step()
