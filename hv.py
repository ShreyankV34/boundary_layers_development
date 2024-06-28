import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the x range
x = np.linspace(0, 10, 1000)

# Define the initial pressure gradient (favorable)
def favorable_pressure_gradient(x):
    return -0.1 * x + 2

# Define the transition to adverse pressure gradient
def adverse_pressure_gradient(x, t):
    return -0.1 * (1 - t) * x + 2 + 0.1 * t * x**2

# Define the boundary layer thickness function
def boundary_layer_thickness(x, t):
    # Simplified model: thinner boundary layer for favorable, thicker for adverse
    return 0.1 * (1 - t) * np.sqrt(x) + 0.2 * t * (x - 5)**2 / 25

# Create the figure and axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Initial plots
line1, = ax1.plot(x, favorable_pressure_gradient(x), label='Pressure Gradient')
line2, = ax2.plot(x, boundary_layer_thickness(x, 0), label='Boundary Layer Thickness')

# Set axis limits
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 2)

# Add labels and titles
ax1.set_xlabel('x')
ax1.set_ylabel('Pressure Gradient')
ax1.set_title('Transition from Favorable to Adverse Pressure Gradient')
ax2.set_xlabel('x')
ax2.set_ylabel('Boundary Layer Thickness')
ax2.set_title('Boundary Layer Development')

# Function to update the animation
def update(t):
    y1 = adverse_pressure_gradient(x, t)
    y2 = boundary_layer_thickness(x, t)
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    return line1, line2

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), blit=True)

# Show the plot
plt.tight_layout()
plt.legend()
plt.show()
