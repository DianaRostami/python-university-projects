# Import necessary libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the function that represents the first-order differential equation
def model(y, t):
    dydt = -y  # Example: dy/dt = -y
    return dydt

# Define the initial condition
y0 = 1

# Define the time points where you want to solve the differential equation
t = np.linspace(0, 5, 100)  # Time points from 0 to 5

# Solve the differential equation using odeint
y = odeint(model, y0, t)

# Plot the solution
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Solution of the First-Order Differential Equation')
plt.grid()
plt.show()