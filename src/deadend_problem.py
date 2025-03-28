# デッドエンドを含む単純な状態空間問題
from state_space_problem import StateSpaceProblem

class DeadEndState:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value
    
    def __str__(self):
        return str(self.value)

class DeadEndProblem(StateSpaceProblem):
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
    """
    state_type = DeadEndState

    def __init__(self):
        self.init_state = DeadEndState(1)

    def get_init_state(self):
        return self.init_state
    
    def is_goal(self, state):
        return state.value == 3

    def get_available_actions(self, state):
        if state.value == 1:
            # 評価値の良い順にアクションを返す
            h_values = {2: self.heuristic(DeadEndState(2)),
                       4: self.heuristic(DeadEndState(4))}
            sorted_actions = sorted([('to2', h_values[2]), ('to4', h_values[4])],
                                 key=lambda x: x[1])
            return [action for action, _ in sorted_actions]
        elif state.value == 2:
            return ['to3']
        elif state.value == 3:
            return []
        else:
            return ['to4']  # 状態3と4からは遷移できない

    def get_next_state(self, state, action):
        if action == 'to2':
            return DeadEndState(2)
        elif action == 'to3':
            return DeadEndState(3)
        elif action == 'to4':
            return DeadEndState(4)
        else:
            raise Exception("Invalid action")
        
    def get_action_cost(self, state, action):
        return 1.0

    def heuristic(self, state):
        # 状態4（デッドエンド）の評価値を状態2より魅力的に
        h_values = {1: 2.0, 2: 1.5, 3: 0.0, 4: 0.8}
        return h_values[state.value]
