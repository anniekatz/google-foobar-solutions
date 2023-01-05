# The following solution uses Djikstra's algorithm to find the shortest path from start to end, removing up to one wall if ideal.
# This solution is exhaustive, as it's essential for the bunnies to use the shortest path possible to escape.

from heapq import heappop, heappush

def djikstra_shortest_path(map, remove_wall=False):
    # Initialize distances and visited lists
    MAX_DIST = float('inf')
    distances = [[MAX_DIST for j in range(len(map[0]))] for i in range(len(map))]
    visited = [[False for j in range(len(map[0]))] for i in range(len(map))]
    
    # Set the distance of the start node to 0
    distances[0][0] = 0
    
    # Initialize the priority queue with start node
    heap = [(0, 0, 0)]
    
    # Extract nodes from the priority queue until empty
    while heap:
        distance, i, j = heappop(heap)
        
        # Ignore node if it has been visited
        if visited[i][j]:
            continue
        
        # Mark the node as visited
        visited[i][j] = True
        
        # Update the distances of the neighbor nodes
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= len(map) or nj < 0 or nj >= len(map[0]) or map[ni][nj] == 1:
                continue
            if distance + 1 < distances[ni][nj]:
                distances[ni][nj] = distance + 1
                heappush(heap, (distance + 1, ni, nj))
    
    # Return the shortest distance + the num of nodes visited
    return distances[-1][-1] + 1

def solution(map):
    # Get the shortest path without removing any walls
    shortest_path = djikstra_shortest_path(map)
    
    # Try all possible walls to remove
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                map[i][j] = 0
                # Take minimum
                shortest_path = min(shortest_path, djikstra_shortest_path(map, remove_wall=True))
                map[i][j] = 1
    
    return shortest_path


# Test the solution
print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))  # Expected output: 7
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))  # Expected output: 11
