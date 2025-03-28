# 幅優先探索
from graph_search import GraphSearch
from tree_search import TreeSearch

def BreadthFirstSearch(problem):
    return GraphSearch(problem, lambda node: node.d)

def BreadthFirstTreeSearch(problem):
    return TreeSearch(problem, lambda node: node.d)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='幅優先探索の実験')
    parser.add_argument('domain', choices=['grid', 'tsp'], help='問題ドメイン (grid: グリッド経路探索, tsp: 巡回セールスマン問題)')
    parser.add_argument('--tree', action='store_true', help='木探索を使用 (グラフ探索がデフォルト)')
    args = parser.parse_args()

    search_fn = BreadthFirstTreeSearch if args.tree else BreadthFirstSearch

    if args.domain == 'grid':
        from grid_pathfinding import GridPathfinding
        print("グリッド経路探索問題 (10x10):")
        problem = GridPathfinding(width=10, height=10, init_position=(0, 0), goal_position=(9, 9))
        path = search_fn(problem)
        print("解パス:")
        for s in reversed(path):
            print(f"({s.state.x}, {s.state.y})")
    else:  # tsp
        from tsp import Tsp
        print("巡回セールスマン問題 (4都市):")
        cities = [(0, 0), (1, 0), (0, 1), (1, 1)]
        problem = Tsp(cities)
        path = search_fn(problem)
        print("解パス:")
        for s in reversed(path):
            print(f"現在地: {s.state.cur_city}, 訪問済み: {s.state.visited}")
