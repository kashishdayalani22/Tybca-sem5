import heapq

START_STATE = (('D', 'A', 'C', 'B'), (), (), ())    # 4 element, 4 tuple
GOAL_STACK = ('A', 'B', 'C', 'D')

def heuristic(state):
    score = 0
    for stack in state:
        if not stack:
            continue
        for i in range(len(stack)):
            block = stack[i]
            if i < len(GOAL_STACK) and block == GOAL_STACK[i]:
                if stack[:i] == GOAL_STACK[:i]:
                    score += 1
                else:
                    score -= 1
            else:
                score -= 1
    return score

def neighbors(state):
    neighbors = []
    num_stacks = len(state)
    
    for i in range(num_stacks):
        if not state[i]:
            continue
            
        block = state[i][-1]
        new_source_stack = state[i][:-1]
        
        for j in range(num_stacks):
            if i == j:
                continue
            
            new_target_stack = state[j] + (block,)
            new_state_list = list(state)
            new_state_list[i] = new_source_stack
            new_state_list[j] = new_target_stack
            neighbors.append(tuple(new_state_list))
            
    return neighbors

def display_state(state):
    non_empty = [s for s in state if s]
    for i in range(len(non_empty)):
        stack = non_empty[i]
        print(f"   Stack {i + 1}: {' -> '.join(stack)}")

def solve_blocks_world():
    pq = []
    initial_h = heuristic(START_STATE)
    heapq.heappush(pq, (-initial_h, 0, START_STATE, [START_STATE]))
    
    visited = set([START_STATE])
    
    while pq:
        neg_h, g, current, path = heapq.heappop(pq)
        
        if any(stack == GOAL_STACK for stack in current):           
            for i in range(len(path)):
                state = path[i]
                h_val = heuristic(state)
                print(f"Step {i} , h(n) = {h_val}")    #h(n) = heuristic value
                print()
                display_state(state)
                print()
                
            print(f"Goal state reached successfully in {len(path) - 1} moves!")
            return
            
        for neighbor in neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                h = heuristic(neighbor)
                heapq.heappush(pq, (-h, g + 1, neighbor, path + [neighbor]))

solve_blocks_world()