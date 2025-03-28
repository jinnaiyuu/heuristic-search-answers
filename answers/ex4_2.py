"""
練習問題4-2: 8方向移動グリッドでのマンハッタン距離ヒューリスティックの検証

このプログラムは、斜め移動を含む8方向グリッド問題において、
マンハッタン距離が許容的なヒューリスティック関数でないことを示す反例を提示します。
"""

from grid_pathfinding8 import GridPathfinding8

def main():
    # 2x2のグリッドで反例を示す
    problem = GridPathfinding8(
        width=2,
        height=2,
        init_position=(0, 0),
        goal_position=(1, 1)
    )

    # 開始状態からゴールまでの実際の最短コスト（斜め移動で1.4）
    state = problem.get_init_state()
    h_value = problem.heuristic(state)  # マンハッタン距離: |1| + |1| = 2
    
    print("反例の提示:")
    print(f"開始位置: (0, 0)")
    print(f"ゴール位置: (1, 1)")
    print(f"実際の最短コスト: 1.4 (斜め移動)")
    print(f"マンハッタン距離による推定コスト: {h_value}")
    print(f"\n結論: マンハッタン距離（{h_value}）> 実際のコスト（1.4）")
    print("従って、マンハッタン距離は許容的なヒューリスティック関数ではありません。")
    print("\n解説:")
    print("8方向移動が可能な場合、斜め移動のコストは√2 ≈ 1.4です。")
    print("しかし、マンハッタン距離は常に直交座標上の距離（この場合2）を返します。")
    print("これは実際のコストよりも大きな値を見積もることになり、")
    print("許容的なヒューリスティック関数の条件「h(n) ≤ h*(n)」に違反します。")

if __name__ == "__main__":
    main()
