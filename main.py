import heapq


def heuristic(node, end):
    # Calculate the Manhattan distance as the heuristic
    return abs(node[0] - end[0]) + abs(node[1] - end[1])


def reconstruct_path(came_from, end):
    path = [end]
    current_node = end
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    path.reverse()
    return path


def shortest_path_astar(maze, start, end):
    rows, cols = len(maze), len(maze[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

    # Define possible moves (up, down, left, right)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited = set()
    heap = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while heap:
        current_cost, current_node = heapq.heappop(heap)
        print(current_node)
        # Check if the next node to be added is adjacent to the current node
        if current_node != start:
            dx, dy = current_node[0] - came_from[current_node][0], current_node[1] - came_from[current_node][1]
            if (dx, dy) not in moves:
                continue

        if current_node == end:
            path = reconstruct_path(came_from, end)
            return "Shortest path found:", path, "Length:", len(path) - 1

        visited.add(current_node)

        for dx, dy in moves:
            new_x, new_y = current_node[0] + dx, current_node[1] + dy
            new_node = (new_x, new_y)

            if is_valid(new_x, new_y) and new_node not in visited:
                new_cost = cost_so_far[current_node] + 1
                if new_node not in cost_so_far or new_cost < cost_so_far[new_node]:
                    cost_so_far[new_node] = new_cost
                    priority = new_cost + heuristic(new_node, end)
                    heapq.heappush(heap, (priority, new_node))
                    came_from[new_node] = current_node

    return "No path found!"


# Example usage:
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0]
]

start = (0, 0)
end = (8, 8)

result = shortest_path_astar(maze, start, end)
print(result)
