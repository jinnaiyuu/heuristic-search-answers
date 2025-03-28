"""
練習問題4-1: グリッド経路探索問題におけるA*探索の実装と評価

このプログラムは以下を行います：
1. 10x10グリッドでの経路探索問題を設定
2. 幅優先探索とA*探索の両方で解を求める
3. 展開ノード数を比較
4. 見つかった経路を可視化
"""

from grid_pathfinding import GridPathfinding
from breadth_first_search import BreadthFirstSearch
from astar_search import AstarSearch
import os

def main():
    # 問題の設定：10x10グリッド
    problem = GridPathfinding(
        width=10,
        height=10,
        init_position=(0, 0),
        goal_position=(9, 9)
    )

    # 幅優先探索による解法
    print("幅優先探索を実行中...")
    bfs_path = BreadthFirstSearch(problem)
        
    # A*探索による解法
    print("\nA*探索を実行中...")
    astar_path = AstarSearch(problem)

    # パスの可視化（BFS）
    if bfs_path:
        # パスを(state, action)のペアに変換
        path_with_actions = []
        for i in range(len(bfs_path)-1):
            current_state = bfs_path[i].state
            next_state = bfs_path[i+1].state
            # アクションを決定（簡易的な方法）
            if next_state.x > current_state.x:
                action = 'r'
            elif next_state.x < current_state.x:
                action = 'l'
            elif next_state.y > current_state.y:
                action = 'd'
            else:
                action = 'u'
            path_with_actions.append((current_state, action))
        # 最後の状態を追加（アクションなし）
        path_with_actions.append((bfs_path[-1].state, None))
        
        problem.generate_path_image(path_with_actions, "bfs_path.png")
        print("\n幅優先探索のパスを bfs_path.png に保存しました")

    # パスの可視化（A*）
    if astar_path:
        # パスを(state, action)のペアに変換
        path_with_actions = []
        for i in range(len(astar_path)-1):
            current_state = astar_path[i].state
            next_state = astar_path[i+1].state
            # アクションを決定（簡易的な方法）
            if next_state.x > current_state.x:
                action = 'r'
            elif next_state.x < current_state.x:
                action = 'l'
            elif next_state.y > current_state.y:
                action = 'd'
            else:
                action = 'u'
            path_with_actions.append((current_state, action))
        # 最後の状態を追加（アクションなし）
        path_with_actions.append((astar_path[-1].state, None))
        
        problem.generate_path_image(path_with_actions, "astar_path.png")
        print("A*探索のパスを astar_path.png に保存しました")

if __name__ == "__main__":
    main()
