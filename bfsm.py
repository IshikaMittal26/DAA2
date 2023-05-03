def topological_sort(adj_matrix):
    num_nodes = len(adj_matrix)
    in_degree = [0] * num_nodes

    for node in range(num_nodes):
        for neighbor in range(num_nodes):
            if adj_matrix[node][neighbor] == 1:
                in_degree[neighbor] += 1

    queue = [node for node in range(num_nodes) if in_degree[node] == 0]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)

        for neighbor in range(num_nodes):
            if adj_matrix[node][neighbor] == 1:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    if len(result) != num_nodes:
        # Graph has a cycle
        return None
    else:
        return result
    
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
    