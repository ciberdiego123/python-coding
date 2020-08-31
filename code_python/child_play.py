moves = ('U', 'R', 'D', 'L')


def find_initial_position(tab):
    for i in range(h):
        for j in range(w):
            if tab[i][j] == 'O':
                return i, j


def make_move(pos, index_mov):
    if moves[index_mov] == 'U':
        next_pos = (pos[0] - 1, pos[1])
    if moves[index_mov] == 'R':
        next_pos = (pos[0], pos[1] + 1)
    if moves[index_mov] == 'D':
        next_pos = (pos[0] + 1, pos[1])
    if moves[index_mov] == 'L':
        next_pos = (pos[0], pos[1] - 1)
    return next_pos


def get_next_index_move(tab, pos, index_mov):
    next_pos = make_move(pos, index_mov)
    if tab[next_pos[0]][next_pos[1]] == '#':
        return (index_mov + 1) % 4
    else:
        return index_mov


# Main Code
w, h = [int(i) for i in input().split()]
n = int(input())
tab = []
for i in range(h):
    line = input()
    tab.append([])
    for c in line:
        tab[i].append(c)
ini_i, ini_j = find_initial_position(tab)
ini_p = (ini_i, ini_j)
index_mov = 0
current_p = ini_p
possible_positions = [(ini_p, index_mov)]
for i in range(n):
    current_p = make_move(current_p, index_mov)
    index_mov = get_next_index_move(tab, current_p, index_mov)
    if possible_positions.__contains__((current_p, index_mov)):
        break
    else:
        possible_positions.append((current_p, index_mov))

n_possible_positions = len(possible_positions)
the_point = possible_positions[n % n_possible_positions][0]
print(str(the_point[1]) + ' ' + str(the_point[0]))
