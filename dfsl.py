def topological_sort(graph):
    visited = set()
    stack = []
    result = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    while stack:
        result.append(stack.pop())

    return result

def main():
    graph = {
    1: [2, 3],
    2: [4, 5],
    3: [5],
    4: [],
    5: []
}
    print(topological_sort(graph))

if __name__ == '__main__':
    main()