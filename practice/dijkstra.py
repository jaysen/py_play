# implement dikstra's algorithm to find the shortest path from a source node to all other nodes in a graph
import heapq

# A simple representation of an Undirected graph using Adjacency Lists (letters for nodes and numbers for edges)
graph = {
    'A': {'B': 3, 'C': 4, 'F': 13},
    'B': {'A': 3, 'D': 5},
    'C': {'A': 4, 'D': 6},
    'D': {'B': 5, 'C': 6, 'E': 7},
    'E': {'D': 7, 'F': 3},
    'F': {'A': 13, 'E': 3}
}

# implementation of dikstra's algorithm:
def dijkstra(graph, source):
    # create a dictionary to store the distance from the source to all other nodes
    # set the distance to infinity for all nodes except the source node
    # set the distance to the source node to 0
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0

    # create a set to store all the visited nodes
    visited = set()

    # create a priority queue to store the nodes and their distances
    # initialize the queue with the source node and its distance to itself, which is 0
    pq = [(0, source)]

    # loop while the priority queue is not empty
    while len(pq) > 0:
        # pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)

        # check if the node has been visited
        if current_node in visited:
            continue

        # iterate through the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # calculate the distance from the current node to the neighbor
            distance = current_distance + weight

            # check if the distance is smaller than the current distance
            if distance < distances[neighbor]:
                # update the distance
                distances[neighbor] = distance

                # push the neighbor into the priority queue
                heapq.heappush(pq, (distance, neighbor))

        # add the current node to the visited set
        visited.add(current_node)

    return distances

print(dijkstra(graph, 'A'))
