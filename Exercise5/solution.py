# Implementation of a BFS algorithm

def solution(n):
  # Convert the string to an integer
  n = int(n)
  
  # Initialize a queue for the BFS
  pellet_queue = [(n, 0)]
  
  # Initialize set for keeping track of visited nums
  visited = set()
  
  # While looping until the queue is empty
  while pellet_queue:
    # Get the current number and the number of operations
    num, operations = pellet_queue.pop(0)
    
    # If the num is 1, return the # of operations
    if num == 1:
      return operations
    
    # If the num has not been visited before, add it to the visited set
    if num not in visited:
      visited.add(num)
      
      # Add the next possible nums to the queue
      pellet_queue.append((num + 1, operations + 1))
      pellet_queue.append((num - 1, operations + 1))
      if num % 2 == 0:
        pellet_queue.append((num // 2, operations + 1))


print(solution(4))
print(solution(15))