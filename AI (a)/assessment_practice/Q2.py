import heapq

START_STATE = (('D', 'A', 'C', 'B'), (), (), ())
GOAL_STACK = ('A', 'B', 'C', 'D')

def blocks_world_heuristic(state):
    score = 0
    for stack in state:
        if not stack:
            continue
        for idx in range(len(stack)):
            block = stack[idx]
            if idx < len(GOAL_STACK) and block == GOAL_STACK[idx]:
                if stack[:idx] == GOAL_STACK[:idx]:
                    score += 1
                else:
                    score -= 1
            else:
                score -= 1
    return score

def get_block_neighbors(state):
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
    for idx in range(len(non_empty)):
        stack = non_empty[idx]
        print(f"   Stack {idx + 1}: Bottom -> {' -> '.join(stack)} (Top)")

def solve_blocks_world():
    pq = []
    initial_h = blocks_world_heuristic(START_STATE)
    heapq.heappush(pq, (-initial_h, 0, START_STATE, [START_STATE]))
    
    visited = set([START_STATE])
    
    while pq:
        neg_h, g, current, path = heapq.heappop(pq)
        
        if any(stack == GOAL_STACK for stack in current):           
            for step_idx in range(len(path)):
                state = path[step_idx]
                h_val = blocks_world_heuristic(state)
                print(f"\nStep {step_idx} | Heuristic Value h(n) = {h_val}")
                print()
                display_state(state)
                print()
                
            print(f"\nGoal state reached successfully in {len(path) - 1} moves!")
            return
            
        for neighbor in get_block_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                h = blocks_world_heuristic(neighbor)
                heapq.heappush(pq, (-h, g + 1, neighbor, path + [neighbor]))

solve_blocks_world()