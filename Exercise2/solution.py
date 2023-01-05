from fractions import Fraction  
 
def solution(pegs):
    num_pegs = len(pegs)
    if (num_pegs <= 1):
        return [-1,-1]
 
    # if num_pegs is even, return true
    # if num_pegs is odd, return false
    
    
   

    even = True if (num_pegs % 2 == 0) else False
    sum = (- pegs[0] + pegs[num_pegs - 1]) if even else (- pegs[0] - pegs[num_pegs -1])
 
    if (num_pegs > 2):
        for index in range(1, num_pegs-1):
            sum += 2 * (-1)**(index+1) * pegs[index]
 
    FirstGearRadius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()
 
 
    currentRadius = FirstGearRadius
    for index in range(0, num_pegs-2):
        CenterDistance = pegs[index+1] - pegs[index]
        NextRadius = CenterDistance - currentRadius
        if (currentRadius < 1 or NextRadius < 1):
            return [-1,-1]
        else:
            currentRadius = NextRadius
 
    return [FirstGearRadius.numerator, FirstGearRadius.denominator]

pegs = [4, 30, 50]
print(solution(pegs)) 

pegs = [4, 17, 50]
print(solution(pegs)) 


