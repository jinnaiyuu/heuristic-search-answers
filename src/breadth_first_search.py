# 幅優先探索
from graph_search import GraphSearch
from tree_search import TreeSearch

def BreadthFirstSearch(problem):
    return GraphSearch(problem, lambda node: node.d)

def BreadthFirstTreeSearch(problem):
    return TreeSearch(problem, lambda node: node.d)

if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    path = BreadthFirstSearch(problem)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s.state.x, s.state.y)