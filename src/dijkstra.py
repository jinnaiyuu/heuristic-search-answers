# ダイクストラ法
from graph_search import GraphSearch

def DijkstraSearch(problem):
    return GraphSearch(problem, lambda node: node.g)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='ダイクストラ法の実験')
    parser.add_argument('domain', choices=['grid', 'tsp'], help='問題ドメイン (grid: グリッド経路探索, tsp: 巡回セールスマン問題)')
    args = parser.parse_args()

    if args.domain == 'grid':
        from grid_pathfinding import GridPathfinding
        print("グリッド経路探索問題 (10x10):")
        problem = GridPathfinding(width=10, height=10, init_position=(0, 0), goal_position=(9, 9))
        path = DijkstraSearch(problem)
        print("解パス:")
        for s in reversed(path):
            print(f"({s.state.x}, {s.state.y})")
    else:  # tsp
        from tsp import Tsp
        print("巡回セールスマン問題 (4都市):")
        cities = [(0, 0), (1, 0), (0, 1), (1, 1)]
        problem = Tsp(cities)
        path = DijkstraSearch(problem)
        print("解パス:")
        for s in reversed(path):
            print(f"現在地: {s.state.cur_city}, 訪問済み: {s.state.visited}")
