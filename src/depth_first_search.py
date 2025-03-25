# 深さ優先探索
from graph_search import GraphSearch
from tree_search import TreeSearch

def DepthFristSearch(problem):
    return GraphSearch(problem, lambda node: -node.d)

def DepthFirstTreeSearch(problem):
    # Note that depth first tree search is NOT guaranteed to terminate.
    # This is implemented for the purpose of demonstrating the difference between tree search and graph search,
    # but not recommended for practical use.
    return TreeSearch(problem, lambda node: -node.d)

if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    path = DepthFristSearch(problem)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s.state.x, s.state.y)