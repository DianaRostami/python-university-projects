from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt 
# differential equation definition as a function

def  diff_eq(t,y):

        dydt = -2 * y
        return dydt
# preliminary conditions definition 

initial_condition = [1]  # y(0)=1 

#differential solution (using solve_ivp)
solution=solve_ivp(diff_eq, [0,5], initial_condition)
#anwser 
print("solution for y(t);",solution.y)

#charts
plt.figure()
plt.plot(solution.t,solution.y[0],label='y(t)')
plt.xlabel('t')
plt.ylabel('y')
plt.title('solution of the differential Equation')
plt.legend()
plt.grid(True)
plt.show()
