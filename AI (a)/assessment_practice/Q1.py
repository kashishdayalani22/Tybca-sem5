import heapq
import random

# Define Goal State in Column-Major Order
# 'a' 'd' 'g'
# 'b' 'e' 'h'
# 'c' 'f' ' '
GOAL_GRID = (
    ('a', 'd', 'g'),
    ('b', 'e', 'h'),
    ('c', 'f', ' ')
)

# Precompute target coordinates for each tile in column-major goal state
GOAL_POS = {
    'a': (0, 0), 'b': (1, 0), 'c': (2, 0),
    'd': (0, 1), 'e': (1, 1), 'f': (2, 1),
    'g': (0, 2), 'h': (1, 2)
}

def manhattan_distance(state):
    """Calculates total Manhattan Distance heuristic h(n) for column-major goal."""
    h = 0
    for r in range(3):
        for c in range(3):
            tile = state[r][c]
            if tile != ' ':
                target_r, target_c = GOAL_POS[tile]
                h += abs(r - target_r) + abs(c - target_c)
    return h

def get_blank_pos(state):
    """Finds the (row, col) position of the blank tile (' ')."""
    for r in range(3):
        for c in range(3):
            if state[r][c] == ' ':
                return r, c

def get_neighbors(state):
    """Generates valid next states by sliding adjacent tiles into the blank space."""
    r, c = get_blank_pos(state)
    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            # Create a mutable copy of grid
            new_grid = [list(row) for row in state]
            # Swap blank with target tile
            new_grid[r][c], new_grid[nr][nc] = new_grid[nr][nc], new_grid[r][c]
            neighbors.append(tuple(tuple(row) for row in new_grid))
            
    return neighbors

def is_solvable(state):
    """Checks if a generated 8-puzzle configuration is solvable."""
    flat_state = [tile for row in state for tile in row if tile != ' ']
    # Goal sequence in flattened row order:
    # row 0: 'a', 'd', 'g' | row 1: 'b', 'e', 'h' | row 2: 'c', 'f'
    # We count inversions relative to goal ordering
    goal_order = ['a', 'd', 'g', 'b', 'e', 'h', 'c', 'f']
    pos_map = {tile: i for i, tile in enumerate(goal_order)}
    
    inversions = 0
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if pos_map[flat_state[i]] > pos_map[flat_state[j]]:
                inversions += 1
    return inversions % 2 == 0

def generate_random_start():
    """Generates a random solvable initial state."""
    tiles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' ']
    while True:
        random.shuffle(tiles)
        state = tuple(tuple(tiles[i:i+3]) for i in range(0, 9, 3))
        if is_solvable(state) and state != GOAL_GRID:
            return state

def solve_8_puzzle():
    start_state = generate_random_start()
    
    # Priority queue stores tuples of (f_score, g_score, state, path)
    pq = []
    initial_h = manhattan_distance(start_state)
    heapq.heappush(pq, (0 + initial_h, 0, start_state, [start_state]))
    
    visited = {start_state: 0}
    
    while pq:
        f, g, current, path = heapq.heappop(pq)
        
        if current == GOAL_GRID:
            # Output state progression
            print("=" * 45)
            print("  8-PUZZLE SOLVER (COLUMN-MAJOR ORDER)")
            print("=" * 45)
            
            for step_idx, state in enumerate(path):
                h_val = manhattan_distance(state)
                print(f"\nStep {step_idx} | Heuristic h(n) = {h_val} | Path Cost g(n) = {step_idx}")
                print("-" * 30)
                for row in state:
                    print(f"  | {' | '.join(row)} |")
                print("-" * 30)
                
            print(f"\nGoal state reached successfully in {len(path) - 1} moves!")
            return
            
        for neighbor in get_neighbors(current):
            tentative_g = g + 1
            if neighbor not in visited or tentative_g < visited[neighbor]:
                visited[neighbor] = tentative_g
                h = manhattan_distance(neighbor)
                heapq.heappush(pq, (tentative_g + h, tentative_g, neighbor, path + [neighbor]))

# Run Assignment 1
solve_8_puzzle()