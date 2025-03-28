# 練習問題4-7の解答
# デッドエンドを含む単純な状態空間問題で、強制山登り法が解けない例を示す
from hill_climbing import HillClimbing, EnforcedHillClimbing
from deadend_problem import DeadEndProblem

def main():
    """
    状態空間：1 -> 2 -> 3
                 -> 4 (デッドエンド)
    
    初期状態：1
    ゴール状態：3
    状態4はデッドエンド（ゴールに到達できない）

    各状態のヒューリスティック値：
    1: 2.0
    2: 1.0
    3: 0.0 (ゴール)
    4: 0.5 (デッドエンド、2よりも良く見える)

    状態4は評価値が状態2よりも良く見えるため、
    強制山登り法は状態4を選択してしまい、デッドエンドに陥る。
    """
    problem = DeadEndProblem()

    print("通常の山登り法での探索:")
    path = HillClimbing(problem)
    if path:
        print("解が見つかりました")
        print("パスの長さ:", len(path))
        for node in path:
            print(f"状態: {node.state.value}")
    else:
        print("解が見つかりませんでした")

    print("\n強制山登り法での探索:")
    path = EnforcedHillClimbing(problem)
    if path:
        print("解が見つかりました")
        print("パスの長さ:", len(path))
        for node in path:
            print(f"状態: {node.state.value}")
    else:
        print("解が見つかりませんでした")

if __name__ == "__main__":
    main()
