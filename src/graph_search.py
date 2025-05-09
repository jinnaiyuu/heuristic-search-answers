# グラフ探索
from search_node import SearchNode
from util import SearchLogger

def is_explored(node, closed_list):
    for n in closed_list:
        if (n.state == node.state) and (n.g <= node.g):
            return True
    return False

def GraphSearch(problem, priority_f=None):
    open = []
    closed = []

    init_state = problem.get_init_state()
    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)

    logger = SearchLogger()
    logger.start()

    open.append(init_node)
    closed.append(init_node)

    while (len(open) > 0):
        open.sort(key=lambda node: priority_f(node), reverse=True)

        node = open.pop()
        logger.expanded += 1

        if problem.is_goal(node.state):
            logger.end()
            logger.print()
            return node.get_path()
        else:
            actions = problem.get_available_actions(node.state)

            for a in actions:
                next_state = problem.get_next_state(node.state, a)

                next_node = SearchNode(next_state)
                next_node.set_g(node.g + problem.get_action_cost(node.state, a))
                next_node.set_d(node.d + 1)
                if not is_explored(next_node, closed):
                    next_node.set_prev_n(node)
                    open.append(next_node)
                    closed.append(next_node)
                    logger.generated += 1
                else:
                    logger.pruned += 1
    logger.end()
    logger.print()
    return None


if __name__ == "__main__":
    from grid_pathfinding import GridPathfinding

    problem = GridPathfinding()
    priority_f = lambda node: node.g
    path = GraphSearch(problem, priority_f)

    print(problem.init_state.x, problem.init_state.y)
    for s in reversed(path):
        print(s)