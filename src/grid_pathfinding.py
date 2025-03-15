# グリッド経路探索問題
from state_space_problem import StateSpaceProblem
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class GridState:
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    def __str__(self):
        return "(" + self.x.__str__() + ", " + self.y.__str__() + ")"

class GridPathfinding(StateSpaceProblem):
    state_type = GridState

    def __init__(self, 
                 width=5, 
                 height=5, 
                 init_position=(0, 0), 
                 goal_position=(4, 4)):
        
        self.width = width
        self.height = height
        self.init_position = init_position
        self.goal_position = goal_position

        self.init_state = GridState(self.init_position)

    def get_init_state(self):
        return self.init_state
    
    def is_goal(self, state):
        return (state.x == self.goal_position[0]) and (state.y == self.goal_position[1])

    def get_available_actions(self, state):
        actions = []
        if state.x > 0:
            actions.append('l')
        if state.x < self.width - 1:
            actions.append('r')
        if state.y > 0:
            actions.append('u')
        if state.y < self.height - 1:
            actions.append('d')
        return actions

    def get_next_state(self, state, action):
        if action == 'l':
            return GridState((state.x - 1, state.y))
        elif action == 'r':
            return GridState((state.x + 1, state.y))
        elif action == 'u':
            return GridState((state.x, state.y - 1))
        elif action == 'd':
            return GridState((state.x, state.y + 1))
        else:
            raise Exception("Invalid action: " + action)
        
    def get_action_cost(self, state, action):
        return 1

    # マンハッタン距離ヒューリスティック - グリッド経路探索
    def heuristic(self, state):
        return abs(state.x - self.goal_position[0]) + abs(state.y - self.goal_position[1])
    
    def generate_path_image(self, path_with_actions, filename="path.png"):
        """
        Generate an image of the path the agent took.
        
        Args:
            path_with_actions: A list of (state, action) pairs representing the path.
            filename: The filename to save the image to.
            
        Returns:
            The path to the saved image.
        """
        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Set the limits of the plot
        ax.set_xlim(-0.5, self.width - 0.5)
        ax.set_ylim(-0.5, self.height - 0.5)
        
        # Invert y-axis to match grid coordinates (0,0 at top-left)
        ax.invert_yaxis()
        
        # Draw grid lines
        for i in range(self.width + 1):
            ax.axvline(i - 0.5, color='gray', linestyle='-', alpha=0.5)
        for i in range(self.height + 1):
            ax.axhline(i - 0.5, color='gray', linestyle='-', alpha=0.5)
        
        # Draw start and goal positions
        ax.add_patch(patches.Rectangle(
            (self.init_position[0] - 0.5, self.init_position[1] - 0.5),
            1, 1, facecolor='green', alpha=0.3))
        ax.add_patch(patches.Rectangle(
            (self.goal_position[0] - 0.5, self.goal_position[1] - 0.5),
            1, 1, facecolor='red', alpha=0.3))
        
        # Extract states from path_with_actions
        states = [state for state, _ in path_with_actions]
        
        # Draw the path
        x_coords = [state.x for state in states]
        y_coords = [state.y for state in states]
        
        # Plot the path
        ax.plot(x_coords, y_coords, 'b-', linewidth=2, alpha=0.7)
        
        # Add markers for each step
        ax.scatter(x_coords, y_coords, color='blue', s=100, zorder=3)
        
        # Add step numbers
        for i, (x, y) in enumerate(zip(x_coords, y_coords)):
            ax.text(x, y, str(i), color='white', ha='center', va='center', fontweight='bold')
        
        # Add arrows to show direction of movement
        for i in range(len(path_with_actions) - 1):
            state, action = path_with_actions[i]
            next_state = states[i + 1]
            
            # Calculate the midpoint for the arrow
            mid_x = (state.x + next_state.x) / 2
            mid_y = (state.y + next_state.y) / 2
            
            # Calculate the direction vector
            dx = next_state.x - state.x
            dy = next_state.y - state.y
            
            # Add an arrow
            ax.arrow(mid_x - 0.3 * dx, mid_y - 0.3 * dy, 0.6 * dx, 0.6 * dy,
                    head_width=0.2, head_length=0.2, fc='blue', ec='blue', zorder=4)
        
        # Set grid
        ax.grid(True, linestyle='-', alpha=0.7)
        
        # Set title and labels
        ax.set_title('Grid Pathfinding Solution')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        
        # Add a legend
        start_patch = patches.Patch(color='green', alpha=0.3, label='Start')
        goal_patch = patches.Patch(color='red', alpha=0.3, label='Goal')
        path_line = plt.Line2D([0], [0], color='blue', linewidth=2, label='Path')
        ax.legend(handles=[start_patch, goal_patch, path_line], loc='upper right')
        
        # Save the figure
        plt.tight_layout()
        plt.savefig(filename, dpi=300)
        plt.close(fig)
        
        return filename
