# routine to solve the Cracker Barrel triangle puzzle.
import random

# There are 36 possible moves. Each hole had indexes
# 0 through 14 left to right and top to bottom
moves = [[0, 1, 3], [0, 2, 5], [1, 3, 6], [1, 4, 8],
         [2, 4, 7], [2, 5, 9], [3, 1, 0], [3, 4, 5],
         [3, 6, 10], [3, 7, 12], [4, 7, 11], [4, 8, 13],
         [5, 2, 0], [5, 4, 3], [5, 8, 12], [5, 9, 14],
         [6, 3, 1], [6, 7, 8], [7, 4, 2], [7, 8, 9],
         [8, 4, 1], [8, 7, 6], [9, 5, 2], [9, 8, 7],
         [10, 6, 3], [10, 11, 12], [11, 7, 4], [11, 12, 13],
         [12, 7, 3], [12, 8, 5], [12, 11, 10], [12, 13, 14],
         [13, 8, 4], [13, 12, 11], [14, 9, 5], [14, 13, 12]]

while True:
    # start with the following configuration
    pegs = [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # keep track of the moves in case we hit upon a solution
    stored_moves = []
    # select 500 random moves. Not all will be valid.
    for x in range(500):
        r = random.randint(0, 35)
        # perform a jump if possible
        if pegs[moves[r][0]] == 1 and \
           pegs[moves[r][1]] == 1 and \
           pegs[moves[r][2]] == 0:
            pegs[moves[r][0]] = 0
            pegs[moves[r][1]] = 0
            pegs[moves[r][2]] = 1
            stored_moves.append(moves[r])
    # we've hit a solution
    if sum(pegs) == 1:
        print(stored_moves)
        break
    else:
        stored_moves.clear()