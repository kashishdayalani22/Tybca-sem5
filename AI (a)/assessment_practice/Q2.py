import heapq

START_STATE = (('D', 'A', 'C', 'B'), (), (), ())
GOAL_STACK = ('A', 'B', 'C', 'D')

def blocks_world_heuristic(state):
    """
    Evaluates Blocks World state.
    +1 for each block on correct structure from bottom up.
    -1 for each incorrect/misplaced block.
    """
    score = 0
    for stack in state:
        if not stack:
            continue
        for idx, block in enumerate(stack):
            # Check if this block matches the goal state at the same position
            if idx < len(GOAL_STACK) and block == GOAL_STACK[idx]:
                # Verify that all blocks underneath are also correct
                if stack[:idx] == GOAL_STACK[:idx]:
                    score += 1
                else:
                    score -= 1
            else:
                score -= 1
    return score

def get_block_neighbors(state):
    """Generates all valid moves by moving top block of one stack to another."""
    neighbors = []
    num_stacks = len(state)
    
    for i in range(num_stacks):
        if not state[i]:
            continue  # Stack is empty, nothing to move
            
        # Top block from stack i
        block = state[i][-1]
        new_source_stack = state[i][:-1]
        
        for j in range(num_stacks):
            if i == j:
                continue
            
            # Place onto stack j
            new_target_stack = state[j] + (block,)
            
            # Construct new state configuration
            new_state_list = list(state)
            new_state_list[i] = new_source_stack
            new_state_list[j] = new_target_stack
            
            # Clean up empty non-primary stacks to maintain clean canonical state representation
            neighbors.append(tuple(new_state_list))
            
    return neighbors

def display_state(state):
    """Formats and prints stacks clearly."""
    non_empty = [s for s in state if s]
    for idx, stack in enumerate(non_empty, 1):
        print(f"   Stack {idx}: Bottom -> {' -> '.join(stack)} (Top)")

def solve_blocks_world():
    # Priority Queue stores (-heuristic, path_cost, state, path)
    # Priority uses negative heuristic to turn min-heap into max-heuristic selection
    pq = []
    initial_h = blocks_world_heuristic(START_STATE)
    heapq.heappush(pq, (-initial_h, 0, START_STATE, [START_STATE]))
    
    visited = set([START_STATE])
    
    while pq:
        neg_h, g, current, path = heapq.heappop(pq)
        current_h = -neg_h
        
        # Check if any stack matches the goal state
        if any(stack == GOAL_STACK for stack in current):
            print("=" * 45)
            print("      BLOCKS WORLD PROBLEM SOLVER")
            print("=" * 45)
            
            for step_idx, state in enumerate(path):
                h_val = blocks_world_heuristic(state)
                print(f"\nStep {step_idx} | Heuristic Value h(n) = {h_val}")
                print("-" * 35)
                display_state(state)
                print("-" * 35)
                
            print(f"\nGoal state reached successfully in {len(path) - 1} moves!")
            return
            
        for neighbor in get_block_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                h = blocks_world_heuristic(neighbor)
                heapq.heappush(pq, (-h, g + 1, neighbor, path + [neighbor]))

# Run Assignment 2
solve_blocks_world()