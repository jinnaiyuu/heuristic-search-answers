#!/usr/bin/env python3
# Test script for the path visualization functionality

from grid_pathfinding import GridPathfinding
from wastar_search import WAstarSearch

def main():
    # Create a grid pathfinding problem
    problem = GridPathfinding(
        width=10,
        height=10,
        init_position=(0, 0),
        goal_position=(9, 9)
    )
    
    # Run the search algorithm to find a path
    path_nodes = WAstarSearch(problem, w=1.0)
    
    if path_nodes is None:
        print("No path found!")
        return
    
    # Convert the path to a list of (state, action) pairs
    path_with_actions = []
    
    # Reverse the path to get it in the correct order (start to goal)
    path_nodes = list(reversed(path_nodes))
    
    # For each node in the path (except the last one), determine the action taken
    for i in range(len(path_nodes) - 1):
        current_state = path_nodes[i].state
        next_state = path_nodes[i + 1].state
        
        # Determine the action taken to go from current_state to next_state
        if next_state.x < current_state.x:
            action = 'l'  # left
        elif next_state.x > current_state.x:
            action = 'r'  # right
        elif next_state.y < current_state.y:
            action = 'u'  # up
        elif next_state.y > current_state.y:
            action = 'd'  # down
        else:
            action = None  # Should not happen
        
        path_with_actions.append((current_state, action))
    
    # Add the goal state with None action
    path_with_actions.append((path_nodes[-1].state, None))
    
    # Generate the path image
    image_path = problem.generate_path_image(path_with_actions, "grid_path.png")
    
    print(f"Path visualization saved to: {image_path}")
    print(f"Path length: {len(path_with_actions)}")
    
    # Print the path
    print("\nPath:")
    for i, (state, action) in enumerate(path_with_actions):
        action_str = action if action is not None else "GOAL"
        print(f"Step {i}: ({state.x}, {state.y}) -> {action_str}")

if __name__ == "__main__":
    main()
