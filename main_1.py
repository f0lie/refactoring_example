grid = [[0]*5 for i in range(5)]

x_1 = 0
y_1 = 0
y_velo_1 = 1

x_2 = 4
y_2 = 0
y_velo_2 = 1

for i in range(15):
    grid[y_1][x_1] = 1
    grid[y_2][x_2] = 1

    for row in grid:
        print(row)

    grid[y_1][x_1] = 0
    grid[y_2][x_2] = 0

    y_1 += y_velo_1
    y_2 += y_velo_2

    if y_1 < 0 or y_1 > 4:
        y_velo_1 *= -1
        y_1 += y_velo_1

    if y_2 < 0 or y_2 > 4:
        y_velo_2 *= -1
        y_2 += y_velo_2

    print()
