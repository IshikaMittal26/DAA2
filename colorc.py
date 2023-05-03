
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}

def min_colors(graph):
    colors = {}

    for vertex in graph:
        adjacent_colors = set()

        for adjacent_vertex in graph[vertex]:
            if adjacent_vertex in colors:
                adjacent_colors.add(colors[adjacent_vertex])

        for color in range(len(graph)):
            if color not in adjacent_colors:
                colors[vertex] = color
                break

    return len(set(colors.values()))

print(min_colors(graph))