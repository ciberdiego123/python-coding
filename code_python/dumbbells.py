class Position:
    def __init__(self, i, j):
        self.i = i
        self.j = j


class DumbbellComplement:
    bar_position = Position(-1, -1)
    opposite_weight_position = Position(-1, -1)


class Board:
    VOID = 0
    BAR_H = 1
    BAR_V = 2
    WEIGHT_NOT_COMPLETED = 3
    WEIGHT_COMPLETED = 4
    SYMBOLS = ['.', '-', '|', 'o', 'x']

    boxes = [[]]

    def __init__(self, boxes):
        self.boxes = boxes.copy()

    def get_number_of_dumbbells(self):
        r = 0
        for i in range(len(self.boxes)):
            for j in range(len(self.boxes[i])):
                if self.boxes[i][j] == self.SYMBOLS[self.BAR_H] or self.boxes[i][j] == self.SYMBOLS[self.BAR_V]:
                    r += 1
        return r

    def contains_weight_not_completed(self):
        for i in range(len(self.boxes)):
            for j in range(len(self.boxes[i])):
                if self.boxes[i][j] == self.SYMBOLS[self.WEIGHT_NOT_COMPLETED]:
                    return True
        return False


n = int(input())
h, w = [int(i) for i in input().split()]
for i in range(h):
    line = input()
for i in range(h):

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print("o=o")