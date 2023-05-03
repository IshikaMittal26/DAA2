def topological_sort(adj_matrix):
    graph = {}
    num_nodes = len(adj_matrix)
    for i in range(num_nodes):
        neighbors = []
        for j in range(num_nodes):
            if adj_matrix[i][j] != 0:
                neighbors.append(j)
        graph[i] = neighbors

    def dfs(node, visited, stack):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(node)

    visited = [False] * num_nodes
    stack = []
    for node in range(num_nodes):
        if not visited[node]:
            dfs(node, visited, stack)

    return stack[::-1]

def main():
    adj_matrix = [
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
    print(topological_sort(adj_matrix))

if __name__ == '__main__':
    main()