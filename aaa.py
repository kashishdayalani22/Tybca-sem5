import heapq

initial_state = [['F', 'B', 'E', 'H'],
                 ['A', 'I', 'D', 'G'],
                 ['R', 'O', 'S', ' ']]

goal_state = [['F', 'I', 'S', 'H'],
              ['B', 'E', 'A', 'R'],
              ['D', 'O', 'G', ' ']]

goal_board = {
    'F': (0, 0), 'I': (0, 1), 'S': (0, 2), 'H': (0, 3),
    'B': (1, 0), 'E': (1, 1), 'A': (1, 2), 'R': (1, 3),
    'D': (2, 0), 'O': (2, 1), 'G': (2,2)}

def mahhattan_distance(board):
    distance = 0
    for row in range(3):
        for col in range(4):
            tile = board[row][col]
            if tile != ' ':
                t_row, t_col = goal_state[tile]
                distance += abs(row - t_row) + abs(col - t_col)
    return distance

def find_empty(board):
  for row in range(len(board)):
    for col in range(len(row)):
      if board[row][col] == " ":
        return row, col

def find_neighbors(board):
  er, ec = find_empty(board)
  neighbors = []
  for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    new_r = er + dr
    new_c = ec + dc

    if 0 <= new_r < 3 and 0 <= new_c < 3:
        grid = [list(r) for r in board]
        grid[er][ec], grid[new_r][new_c] = grid[new_r][new_c], grid[er][ec]
        neighbors.append(tuple(tuple(r) for r in grid))

    return neighbors

def solve_puzzle(start_board):
  board = []
  goal = []
  for i in range(3):
    for j in range(4):
      board.append(start_board[i][j])
      goal.append(goal_state[i][j])
  print(board)
  print(goal)

  map = {}
  for i in range(len(goal)):
      map[goal[i]] = i

  inversions = 0
  for i in range(len(board)):
      for j in range(i + 1, len(board)):
          if map[board[i]] > map[board[j]]:
              inversions += 1
  if inversions % 2 != 0:
      print("Not solvable as inversion is: ", inversions)
      return

  open_list = []
  heuristic = mahhattan_distance(start_board)
  heapq.heappush(open_list, (heuristic, 0, start_board, [start_board]))
  visited = set()

  while len(open_list) > 0:
      f, g, current_board, path = heapq.heappop(open_list)

      if current_board in visited:
          continue
      visited.add(current_board)
      if current_board == goal:
        for i in range(len(path)):
            state = path[i]
            h_val = mahhattan_distance(state)
            print(f"Step {i}  g(n) = {i}  h(n) = {h_val}")
            print()
            for row in state:
                print(f"   {'  '.join(row)} ")
            print()

            print(f"Puzzle solved in {len(path) - 1} moves!")
            return

      for neighbor in find_neighbors(current_board):
          if neighbor not in visited:
              t_g = g + 1
              t_h = mahhattan_distance(neighbor)
              heapq.heappush(open_list, (t_g + t_h, t_g, neighbor, path + [neighbor]))
      
solve_puzzle(initial_state)
