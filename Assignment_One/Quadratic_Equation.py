import cmath
def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    
    sol1 = (-b - cmath.sqrt(d)) / (2*a)
    sol2 = (-b + cmath.sqrt(d)) / (2*a)
    return sol1, sol2

a = 1
b = 5
c = 6

solutions = solve_quadratic(a, b, c)
print(f'The solutions are {solutions[0]} and {solutions[1]}')
