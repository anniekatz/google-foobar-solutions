def solution(x,y):
    # turn x and y into sets
    set_x = set(x)
    set_y = set(y)

    # find the difference using the symmetric difference method
    # there should only be one in the list
    diff = set_x.symmetric_difference(set_y)

    return diff


x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]
additional_id = solution(x, y)
print(additional_id)  # Output: 6

x = [14, 27, 1, 4, 2, 50, 3, 1]
y = [2, 4, -4, 3, 1, 1, 14, 27, 50]
additional_id = solution(x, y)
print(additional_id)  # Output: -4
