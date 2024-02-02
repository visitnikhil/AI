import heapq


class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != goal_state[i][j]:
                    count += 1
        return count

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def get_user_input():
    print("Enter the initial configuration for the 8 puzzle problem row by row (separate each number by space):")
    puzzle_input = []
    for i in range(3):
        while True:
            row = input(f"Enter numbers for row {i + 1}: ").strip().split()
            if len(row) == 3 and all(num.isdigit() for num in row):
                puzzle_input.append([int(num) for num in row])
                break
            else:
                print("Invalid input. Please enter 3 space-separated numbers.")
    return puzzle_input


def get_possible_moves(node):
    moves = []
    empty_space = None
    for i in range(3):
        for j in range(3):
            if node.state[i][j] == 0:
                empty_space = (i, j)
                break

    for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_position = (empty_space[0] + move[0], empty_space[1] + move[1])
        if 0 <= new_position[0] < 3 and 0 <= new_position[1] < 3:
            new_state = [row.copy() for row in node.state]
            new_state[empty_space[0]][empty_space[1]], new_state[new_position[0]][new_position[1]] = \
                new_state[new_position[0]][new_position[1]], new_state[empty_space[0]][empty_space[1]]
            moves.append(PuzzleNode(new_state, parent=node, move=move, cost=node.cost + 1))
    return moves


def get_path(node):
    path = []
    while node.parent:
        path.append(node.move)
        node = node.parent
    path.reverse()
    return path


def a_star_search(initial_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, PuzzleNode(initial_state))
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == goal_state:
            return get_path(current_node)
        closed_set.add(tuple(map(tuple, current_node.state)))
        for neighbor in get_possible_moves(current_node):
            if tuple(map(tuple, neighbor.state)) not in closed_set:
                heapq.heappush(open_list, neighbor)
    return None


if __name__ == '__main__':
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    initial_state = get_user_input()
    print("Initial State:")
    for row in initial_state:
        print(row)

    solution = a_star_search(initial_state)

    if solution:
        print("Moves to reach the goal state:")
        for move in solution:
            print(move)
    else:
        print("No solution found for the given input.")
