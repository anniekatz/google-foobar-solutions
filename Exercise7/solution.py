class Graph:
    def __init__(self, banana_list):
        # Initialize the graph with the given list of banana counts
        self.trainers = len(banana_list)
        self.matrix = [[0 for _ in range(self.trainers)] for _ in range(self.trainers)]
        for i in range(self.trainers):
            for j in range(self.trainers):
                # Only add an edge between two trainers if they can get stuck in an infinite loop
                if i < j and can_loop(banana_list[i], banana_list[j]):
                    self.matrix[i][j] = 1
                    self.matrix[j][i] = 1

    def find_match(self, u, match, visited):
        # Find a match for the current trainer using a breadth-first search
        for v in range(self.trainers):
            if self.matrix[u][v] and not visited[v]:
                visited[v] = True
                if match[v] == -1 or self.find_match(match[v], match, visited):
                    match[v] = u
                    return True
        return False

    def max_match(self):
        # Use the find_match function to find a maximum matching in the graph
        match = [-1] * self.trainers
        result = 0
        for i in range(self.trainers):
            visited = [False] * self.trainers
            if self.find_match(i, match, visited):
                result += 1
        # Return the number of trainers that are not part of the matching
        return self.trainers - 2 * (result // 2)

def solution(l):
    return Graph(l).max_match()

def can_loop(x, y):
    # Determine whether two trainers with x and y bananas can get stuck in an infinite loop
    gcd_base = int((x + y) / gcd(x, y))
    return bool(gcd_base & (gcd_base - 1))

def gcd(a, b):
    # Calculate the greatest common divisor of a and b
    while b:
        a, b = b, a % b
    return a


print(solution([1, 1])) # Expected output: 2
print(solution([1, 7, 3, 21, 13, 19])) # Expected output: 0

