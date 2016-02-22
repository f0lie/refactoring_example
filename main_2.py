from namedlist import namedlist

class Point(namedlist("Point", "x y x_velo y_velo", default = 0)):
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

grid_size = 5
grid = [[0]*grid_size for i in range(grid_size)]

point = Point(x=0, y=0,
              x_velo=0, y_velo=1)
point_1 = Point(x=4, y=0,
                x_velo=0, y_velo=1)

for i in range(5):
    grid[point.y][point.x] = 1
    grid[point_1.y][point_1.x] = 1

    for row in grid:
        print(row)
    print()

    grid[point.y][point.x] = 0
    grid[point_1.y][point_1.x] = 0

    point.move()
    point.bounce(grid_size)

    point_1.move()
    point_1.bounce(grid_size)