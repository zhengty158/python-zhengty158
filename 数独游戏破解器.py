# -*- coding:utf-8 -*-

# 我预想的逻辑结构是：
# 用一个字典写出每个格子对应的数字，并改写每一行、每一列、每一个九宫格的列表，使其体现出跟其他行、列、格的逻辑关系
# 让每一行、每一列、每一个九宫格都循环增加1-9
# 直到它们都成为包含1-9的列表，而且确保每一行、每一列、每一个九宫格
# 都只包含唯一的1-9（用sort和if进行判断）
# 再按原始顺序打印每一行、每一列

# 以下列表分别代表行、列、九宫格
# 列表中的数字是随便找了一局数独游戏录入的
line_1 = [2, 1]
line_2 = [1, 5, 6, 9]
line_3 = [8, 1, 3]
line_4 = [7, 9, 5]
line_5 = [5, 6, 4, 7, 3]
line_6 = [8, 4, 5, 9, 6]
line_7 = [2, 3]
line_8 = [5, 7, 2, 8, 3]
line_9 = [8, 6, 2, 4]
line = [line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9]

row_1 = [8, 5]
row_2 = [7, 5, 8]
row_3 = [1, 8, 6, 4, 2, 7]
row_4 = [2]
row_5 = [1, 9, 5, 3]
row_6 = [2, 5, 3, 8, 6]
row_7 = [1, 6, 4, 9, 3, 2]
row_8 = [9, 7, 6]
row_9 = [5, 3, 4]
row = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]

sudoku_1 = [1, 8]
sudoku_2 = [2, 5, 1, 3]
sudoku_3 = [1, 6, 9]
sudoku_4 = [7, 5, 6, 8, 4]
sudoku_5 = [9, 5]
sudoku_6 = [5, 4, 7, 3, 9, 6]
sudoku_7 = [2, 5, 7, 8]
sudoku_8 = [2, 3, 8, 6]
sudoku_9 = [3, 2, 4]
sudoku = [sudoku_1, sudoku_2, sudoku_3, sudoku_4, sudoku_5, sudoku_6, sudoku_7, sudoku_8, sudoku_9]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [a, a, a, a, a, a, a, a, a]

# 逻辑想出来了，但是语法总是报错………
for x in line:
    for y in row:
        for z in sudoku:
            for c in b:
                for d in range(0, 9):
                    if c[d] not in sorted(x[d] or y[d] or z[d]):
                        x.append(c[d])
                        y.append(c[d])
                        z.append(c[d])
                        if sorted(x[d]) == b[d] and sorted(y[d]) == b[d] and sorted(z[d]) == b[d]:
                            print(x)
                            print(y)
