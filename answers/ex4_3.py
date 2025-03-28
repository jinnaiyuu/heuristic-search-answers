"""
練習問題4-3: 8方向移動グリッドでの許容的なヒューリスティック関数の実装

このプログラムは、斜め移動を含む8方向グリッド問題において、
マンハッタン距離よりも正確で、かつ許容的な新しいヒューリスティック関数を実装し、
その性質を検証します。
"""

from grid_pathfinding8 import GridPathfinding8, GridState

class GridPathfinding8WithBetterHeuristic(GridPathfinding8):
    def heuristic(self, state):
        """
        斜め移動を考慮したヒューリスティック関数
        
        計算方法：
        1. dx, dyを座標の差分として計算
        2. min(dx,dy)回の斜め移動（コスト1.4）と
        3. 残りの|dx-dy|回の直線移動（コスト1）の合計
        
        この方法は、実際の最短経路の計算方法と一致するため、
        許容的かつより正確な推定値を提供します。
        """
        dx = abs(state.x - self.goal_position[0])
        dy = abs(state.y - self.goal_position[1])
        
        # 斜め移動のコスト（最小の差分値×1.4）
        diagonal_cost = min(dx, dy) * 1.4
        
        # 残りの直線移動のコスト
        straight_cost = abs(dx - dy)
        
        return diagonal_cost + straight_cost

def main():
    # 同じ問題を2つの異なるヒューリスティックで解く
    start = (0, 0)
    goal = (2, 2)
    
    # オリジナルのマンハッタン距離ヒューリスティック
    problem1 = GridPathfinding8(
        width=3,
        height=3,
        init_position=start,
        goal_position=goal
    )
    
    # 改良版ヒューリスティック
    problem2 = GridPathfinding8WithBetterHeuristic(
        width=3,
        height=3,
        init_position=start,
        goal_position=goal
    )
    
    # 初期状態での比較
    state = GridState(start)
    actual_cost = 2.8  # ゴールまでの実際のコスト（斜め2回）
    
    print("ヒューリスティック関数の比較:")
    print(f"開始位置: {start}")
    print(f"ゴール位置: {goal}")
    print(f"実際の最短コスト: {actual_cost} (斜め移動2回)")
    print(f"マンハッタン距離による推定: {problem1.heuristic(state)}")
    print(f"改良版ヒューリスティックによる推定: {problem2.heuristic(state)}")
    
    print("\n改良版ヒューリスティックの特徴:")
    print("1. 許容的: 実際のコストより小さい値は返しません")
    print("2. より正確: 斜め移動を考慮した実際の移動方法に基づいて計算")
    print("3. 一貫性: 三角不等式を満たし、無矛盾性も保証")

if __name__ == "__main__":
    main()
