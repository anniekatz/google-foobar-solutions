from decimal import Decimal, localcontext

def solution(s):
    # Convert string `s` to Decimal with context precision of 102
    n = Decimal(s)
    with localcontext() as ctx:
        ctx.prec = 102
        

        sqrt_of_2 = Decimal(2).sqrt()
        two_plus_sqrt_of_2 = Decimal(2) + sqrt_of_2

        # Recursively solve for the result
        def solve(number):
            if number == 0:
                return 0

            first_floor = int(sqrt_of_2 * number)
            second_floor = int(first_floor / two_plus_sqrt_of_2)
            
            return (first_floor * (first_floor + 1)) / 2 - solve(second_floor) - second_floor * (second_floor + 1)

        # Return the result as a string
        return str(int(solve(n)))

print(solution('77')) # Output: 4208
print(solution('5')) # Output: 19