class Point():
    def __init__(self, x=0, y=0, x_velo=0, y_velo=0):
        self.x = x
        self.y = y

        self.x_velo = x_velo
        self.y_velo = y_velo

    def move(self):
        self.x += self.x_velo
        self.y += self.y_velo

    def bounce(self, grid_size):
        if self.x < 0 or self.x > grid_size - 1:
            self.x_velo *= -1
            self.x += self.x_velo

        if self.y < 0 or self.y > grid_size - 1:
            self.y_velo *= -1
            self.y += self.y_velo

class Grid():
    def __init__(self, point_list=[], grid_size=5):
        self.grid_size = grid_size
        self.grid = [[0]*grid_size for i in range(grid_size)]
        self.points = point_list

    def step(self):
        for point in self.points:
            self.grid[point.y][point.x] = 1

        for row in self.grid:
            print(row)
        print()

        for point in self.points:
            self.grid[point.y][point.x] = 0

        for point in self.points:
            point.move()
            point.bounce(self.grid_size)

grid = Grid([Point(0, 0, 1, 1),
             Point(0, 0, 0, 1),
             Point(4, 4, -1, -1),
             Point(4, 4, 0, -1)],
             grid_size=5)

for i in range(5):
    grid.step()