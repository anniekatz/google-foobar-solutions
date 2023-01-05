def solution(x, y):
    # Calculate the ID of the worker at coordinates (x, y)
    # Sequence used to determine ID
    bunny_id = int(x + ((x + (y - 2)) * (x + (y - 1))) / 2)

    return str(bunny_id)


print(solution(5, 10)) #96

print(solution(3, 2)) #9

print(solution(3, 3)) #13

print(solution(1, 5)) #11