import numpy as np


def dijkstra_shortest_path(graph, start_node, target_node):
    # Initialize distance array with infinity for all nodes
    distances = np.full(graph.shape[0], np.inf)
    # Set the distance to the starting node as 0
    distances[start_node] = 0
    # Initialize visited set
    visited = set()
    # Initialize previous node array with None for all nodes
    previous = [None] * graph.shape[0]
    # Main loop
    while target_node not in visited:
        # Find the node with the minimum distance
        min_node = np.argmin(distances)
        # Add the node to the visited set
        visited.add(min_node)
        # Update the distances and previous nodes for the neighboring nodes
        for neighbor_node, distance in enumerate(graph[min_node]):
            if distance > 0 and neighbor_node not in visited:
                new_distance = distances[min_node] + distance
                if new_distance < distances[neighbor_node]:
                    distances[neighbor_node] = new_distance
                    previous[neighbor_node] = min_node
        # Set the minimum node distance to infinity so it won't be selected again
        distances[min_node] = np.inf
        print(distances)
    # Trace back the path from target node to start node
    path = [target_node]
    while previous[target_node] is not None:
        path.append(previous[target_node])
        target_node = previous[target_node]
    path.reverse()
    print('The shortest path is:', path)
    path_length = 0
    # Sum the shortest path length
    current = start_node
    for next_node in path[1:]:
        path_length = path_length + graph[current, next_node]
        current = next_node
    print(path_length)


# build weighted array of graph
graph = np.array([[0, 50, 40, 0, 0],  # start node/ node 0
                  [50, 0, 0, 0, 200],  # node 1
                  [40, 0, 0, 130, 175],  # node 2
                  [0, 0, 130, 0, 180],  # node 3
                  [0, 200, 175, 180, 0]])  # node 4/goal node

dijkstra_shortest_path(graph, 0, 4)
