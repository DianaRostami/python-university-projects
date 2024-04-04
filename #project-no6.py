#project-no6
from sympy import symbols, Eq, solve
# variables definition
x, y = symbols('x y')

# equation definition
eq1 = Eq(2*x + 4*y, 94)
eq2 = Eq(x + y, 35)

# equation solution
solution = solve((eq1, eq2), (x, y))

# print anwser 

print("number of chickens:", solution[x])
print("number of rabbits: ", solution[y])