import heapq

Goal_state = (
    ('a', 'd', 'g'),
    ('b', 'e', 'h'),
    ('c', 'f', ' ')
)
Goal_board = {
    'a': (0, 0), 'b': (1, 0), 'c': (2, 0),
    'd': (0, 1), 'e': (1, 1), 'f': (2, 1),
    'g': (0, 2), 'h': (1, 2)
}
Start_Board = (
    ('b', 'a', 'g'),
    ('c', 'd', 'h'),
    ('e', 'f', ' ')
)

def calculate_manhattan(board):
    distance = 0
    for row in range(3):
        for col in range(3):
            tile = board[row][col]
            if tile != ' ':
                target_row, target_col = Goal_board[tile]
                distance += abs(row - target_row) + abs(col - target_col)
    return distance

def get_blank_pos(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return row, col

def get_neighbors(board):
    blank_row, blank_col = get_blank_pos(board)
    neighbors = []

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row = blank_row + dr
        new_col = blank_col + dc
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            grid = [list(r) for r in board]
            grid[blank_row][blank_col], grid[new_row][new_col] = grid[new_row][new_col], grid[blank_row][blank_col]
            neighbors.append(tuple(tuple(r) for r in grid))

    return neighbors

def solve_puzzle(start_board):
    flat_board = [tile for row in start_board for tile in row if tile != ' ']
    goal_order = ['a', 'd', 'g', 'b', 'e', 'h', 'c', 'f']
    
    pos_map = {}
    for idx in range(len(goal_order)):
        pos_map[goal_order[idx]] = idx

    inversions = 0
    for i in range(len(flat_board)):
        for j in range(i + 1, len(flat_board)):
            if pos_map[flat_board[i]] > pos_map[flat_board[j]]:
                inversions += 1

    if inversions % 2 != 0:
        print("This initial state is not solvable.")
        return

    open_list = []
    initial_h = calculate_manhattan(start_board)
    heapq.heappush(open_list, (initial_h, 0, start_board, [start_board]))
    visited = set()

    while len(open_list) > 0:
        f_cost, g_cost, current_board, path = heapq.heappop(open_list)

        if current_board in visited:
            continue
        visited.add(current_board)

        if current_board == Goal_state:

            for step_idx in range(len(path)):
                state = path[step_idx]
                h_val = calculate_manhattan(state)
                print(f"\nStep {step_idx} | g(n) = {step_idx} | h(n) = {h_val}")
                print()
                for row in state:
                    print(f"   {'  '.join(row)} ")
                print()

            print(f"Puzzle solved in {len(path) - 1} moves!")
            return

        for neighbor in get_neighbors(current_board):
            if neighbor not in visited:
                tentative_g = g_cost + 1
                tentative_h = calculate_manhattan(neighbor)
                heapq.heappush(open_list, (tentative_g + tentative_h, tentative_g, neighbor, path + [neighbor]))

solve_puzzle(Start_Board)