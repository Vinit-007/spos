
import heapq

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = [(0, start)]
    heapq.heapify(open_set)
    visited = set()

    while open_set:
        g_score, current = heapq.heappop(open_set)

        if current == goal:
            return g_score

        visited.add(current)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r, c = current[0] + dr, current[1] + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and (r, c) not in visited:
                heapq.heappush(open_set, (g_score + 1 + abs(r - goal[0]) + abs(c - goal[1]), (r, c)))

    return -1

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
shortest_path_length = astar(grid, start, goal)
if shortest_path_length != -1:
    print("Shortest path length from", start, "to", goal, ":", shortest_path_length)
else:
    print("No path found from", start, "to", goal)
