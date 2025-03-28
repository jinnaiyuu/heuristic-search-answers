# 山登り法と強制山登り法の実装
from collections import deque
from state_space_problem import StateSpaceProblem
from search_node import SearchNode

def HillClimbing(problem: StateSpaceProblem):
    """
    通常の山登り法
    現在の状態から評価値が改善する遷移先だけを選択
    改善する遷移先がなければ終了
    """
    current = SearchNode(problem.get_init_state())
    current_value = problem.heuristic(current.state)
    path = [current]

    while True:
        best_neighbor = None
        best_value = current_value

        # 現在の状態から遷移可能な状態を評価
        for action in problem.get_available_actions(current.state):
            next_state = problem.get_next_state(current.state, action)
            next_value = problem.heuristic(next_state)

            if next_value < best_value:
                best_value = next_value
                best_neighbor = SearchNode(next_state)
                best_neighbor.set_prev_n(current)

        # 改善する状態がなければ終了
        if best_neighbor is None:
            break

        # 改善する状態があれば移動
        current = best_neighbor
        current_value = best_value
        path.append(current)

        # ゴールに到達したら終了
        if problem.is_goal(current.state):
            return path

    # ゴールに到達できなかった場合
    return None

def EnforcedHillClimbing(problem: StateSpaceProblem):
    """
    強制山登り法
    現在の状態から評価値が改善するノードを見つけるまで幅優先探索
    改善するノードが見つかれば、そのノードに移動
    """
    current = SearchNode(problem.get_init_state())
    current_value = problem.heuristic(current.state)
    path = [current]

    while not problem.is_goal(current.state):
        # 評価値が改善するノードを幅優先探索で探す
        better_node = find_better_node(problem, current, current_value)

        # 改善するノードが見つからなければ終了
        if better_node is None:
            break

        # 改善するノードへの経路を追加
        path += [better_node]
        # path.extend(get_path_to_node(better_node)[1:])
        current = better_node
        current_value = problem.heuristic(current.state)

        if problem.is_goal(current.state):
            return path

    # ゴールに到達できなかった場合
    return None

def find_better_node(problem, start_node, current_value):
    """
    深さを徐々に増やしながら評価値が改善するノードを探す
    各深さで幅優先探索を行い、改善するノードが見つかった時点で返す
    """
    max_depth = 100  # 安全のための最大深さ制限
    
    for depth in range(1, max_depth + 1):
        # 深さdでの幅優先探索
        queue = deque([(start_node, 0)])  # (ノード, 深さ)のペア
        visited = {start_node.state}
        
        while queue:
            node, node_depth = queue.popleft()
            
            if node_depth >= depth:
                continue
                
            # 遷移可能な状態を調べる
            # デバッグ情報を追加
            actions = problem.get_available_actions(node.state)
            print(f"\n深さ {node_depth} で探索中:")
            print(f"現在のノード: {node.state}")
            print(f"現在の評価値: {current_value}")
            print(f"利用可能なアクション: {actions}")
            
            for action in actions:
                next_state = problem.get_next_state(node.state, action)
                next_value = problem.heuristic(next_state)
                print(f"アクション {action} -> 状態 {next_state} (評価値: {next_value})")
                
                if next_state in visited:
                    print("  [訪問済み]")
                    continue
                    
                visited.add(next_state)
                next_node = SearchNode(next_state)
                next_node.set_prev_n(node)
                
                # 評価値が改善するノードが見つかれば即座に返す
                if next_value < current_value:
                    print(f"  [改善ノード発見]")
                    return next_node
                
                print("  [キューに追加]")
                queue.append((next_node, node_depth + 1))
    
    return None  # 改善するノードが見つからなかった

def get_path_to_node(node):
    """
    指定されたノードまでの経路を取得
    """
    path = []
    current = node
    while current is not None:
        path.append(current)
        if hasattr(current, 'prev_n'):
            current = current.prev_n
        else:
            current = None
    return list(reversed(path))

if __name__ == "__main__":
    # テスト用の問題を作成
    from grid_pathfinding import GridPathfinding
    
    # シンプルな例：3x3グリッド
    problem = GridPathfinding(
        width=3,
        height=3,
        init_position=(0, 0),
        goal_position=(2, 2)
    )
    
    print("通常の山登り法での探索:")
    path = HillClimbing(problem)
    if path:
        print("解が見つかりました")
        print("パスの長さ:", len(path))
        for node in path:
            print(f"({node.state.x}, {node.state.y})")
    else:
        print("解が見つかりませんでした")
    
    print("\n強制山登り法での探索:")
    path = EnforcedHillClimbing(problem)
    if path:
        print("解が見つかりました")
        print("パスの長さ:", len(path))
        for node in path:
            print(f"({node.state.x}, {node.state.y})")
    else:
        print("解が見つかりませんでした")
