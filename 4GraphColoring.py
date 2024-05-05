def is_safe(graph, vertex, color, color_assignment):
    for neighbor in graph[vertex]:
        if color_assignment[neighbor] == color:
            return False
    return True

def graph_coloring_backtracking(graph, colors, vertex, color_assignment):
    if vertex == len(graph):
        return True
    for color in colors:
        if is_safe(graph, vertex, color, color_assignment):
            color_assignment[vertex] = color
            if graph_coloring_backtracking(graph, colors, vertex + 1, color_assignment):
                return True
            color_assignment[vertex] = None
    return False

def graph_coloring(graph, colors):
    color_assignment = [None] * len(graph)
    if graph_coloring_backtracking(graph, colors, 0, color_assignment):
        return color_assignment
    else:
        return "No solution found"

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
colors = ['Red', 'Green', 'Blue']
color_assignment = graph_coloring(graph, colors)
print("Color assignment for vertices:", color_assignment)
