import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    open_list = []
    closed_list = set()
    start_node = Node(start)
    end_node = Node(end)

    open_list.append(start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return the path in reverse order

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for neighbor in neighbors:
            new_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if (
                new_position[0] < 0
                or new_position[0] >= len(maze)
                or new_position[1] < 0
                or new_position[1] >= len(maze[0])
            ):
                continue

            if maze[new_position[0]][new_position[1]] == 1:
                continue

            if new_position in closed_list:
                continue

            new_node = Node(new_position, current_node)
            new_node.g = current_node.g + 1
            new_node.h = (
                (new_position[0] - end_node.position[0]) ** 2
                + (new_position[1] - end_node.position[1]) ** 2
            )
            new_node.f = new_node.g + new_node.h

            if any(node.position == new_node.position for node in open_list):
                for node in open_list:
                    if node.position == new_node.position and node.f > new_node.f:
                        node = new_node
                        break
            else:
                open_list.append(new_node)

    return None  # No path found

# Example usage
maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = astar(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found")
