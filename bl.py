import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def boundary_layer_simulation():
    # Parameters
    nx, ny = 100, 50  # Grid points in x and y directions
    lx, ly = 2.0, 1.0  # Length of the domain in x and y directions
    dx, dy = lx / (nx - 1), ly / (ny - 1)  # Grid spacing
    nu = 0.01  # Kinematic viscosity
    dt = 0.001  # Time step size
    n_steps = 500  # Number of time steps

    # Initial conditions
    u = np.zeros((ny, nx))  # Velocity in x direction
    v = np.zeros((ny, nx))  # Velocity in y direction
    u[0, :] = 1.0  # Free-stream velocity at the top boundary

    # Plot setup
    fig, ax = plt.subplots()
    x = np.linspace(0, lx, nx)
    y = np.linspace(0, ly, ny)
    X, Y = np.meshgrid(x, y)
    cax = ax.contourf(X, Y, u, cmap='jet')
    fig.colorbar(cax)

    def update(frame):
        nonlocal u, v
        un = u.copy()
        vn = v.copy()
        
        # Simple finite difference method for boundary layer development
        for j in range(1, ny-1):
            for i in range(1, nx-1):
                u[j, i] = un[j, i] + nu * dt * (
                    (un[j+1, i] - 2 * un[j, i] + un[j-1, i]) / dy**2 +
                    (un[j, i+1] - 2 * un[j, i] + un[j, i-1]) / dx**2
                ) - dt * (un[j, i] * (un[j, i] - un[j, i-1]) / dx + vn[j, i] * (un[j, i] - un[j-1, i]) / dy)
                v[j, i] = vn[j, i] + nu * dt * (
                    (vn[j+1, i] - 2 * vn[j, i] + vn[j-1, i]) / dy**2 +
                    (vn[j, i+1] - 2 * vn[j, i] + vn[j, i-1]) / dx**2
                ) - dt * (un[j, i] * (vn[j, i] - vn[j, i-1]) / dx + vn[j, i] * (vn[j, i] - vn[j-1, i]) / dy)
    
        # Enforce boundary conditions
        u[:, 0] = 1.0  # Inlet velocity
        u[:, -1] = u[:, -2]  # Outflow condition
        u[-1, :] = u[-2, :]  # No-slip at the bottom
        u[0, :] = 1.0  # Free-stream velocity at the top

        v[:, 0] = 0.0  # No transverse velocity at the inlet
        v[:, -1] = v[:, -2]  # Outflow condition
        v[-1, :] = 0.0  # No-slip at the bottom
        v[0, :] = 0.0  # No transverse velocity at the top

        ax.clear()
        cax = ax.contourf(X, Y, u, cmap='jet')
        return [cax]

    ani = animation.FuncAnimation(fig, update, frames=n_steps, interval=20, blit=True)
    plt.show()

    return u, x, y

def analyze_boundary_layer(u, x, y):
    # Select x positions for analysis
    x_positions = [0.1, 0.5, 1.0, 1.5]
    nx, ny = u.shape[1], u.shape[0]

    fig, ax = plt.subplots()
    for xpos in x_positions:
        i = np.abs(x - xpos).argmin()
        ax.plot(u[:, i], y, label=f'x = {xpos:.2f}')

    ax.set_xlabel('Velocity')
    ax.set_ylabel('y')
    ax.set_title('Velocity Profiles at Different x Positions')
    ax.legend()
    plt.show()

    # Measure boundary layer thickness
    boundary_layer_thickness = []
    for i in range(nx):
        y99 = y[np.where(u[:, i] >= 0.99)[0][0]]
        boundary_layer_thickness.append(y99)

    fig, ax = plt.subplots()
    ax.plot(x, boundary_layer_thickness, label='Boundary Layer Thickness')
    ax.set_xlabel('x')
    ax.set_ylabel('Boundary Layer Thickness')
    ax.set_title('Boundary Layer Thickness Along the Plate')
    ax.legend()
    plt.show()

    # Calculate velocity gradients at the wall
    velocity_gradients = []
    for i in range(nx):
        dyu_dy = (u[1, i] - u[0, i]) / (y[1] - y[0])
        velocity_gradients.append(dyu_dy)

    fig, ax = plt.subplots()
    ax.plot(velocity_gradients,x,  label='Velocity Gradient at the Wall')
    ax.set_xlabel('x')
    ax.set_ylabel('Velocity Gradient')
    ax.set_title('Velocity Gradient at the Wall Along the Plate')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    u, x, y = boundary_layer_simulation()
    analyze_boundary_layer(u, x, y)
u, x, y = boundary_layer_simulation()

# Choose an x position
xpos = 1.0
i = np.abs(x - xpos).argmin()

# Extract the velocity profile at xpos
velocity_profile = u[:, i]
print("Velocity profile at x =", xpos)
print(velocity_profile)

# Plotting the velocity profile
import matplotlib.pyplot as plt

plt.plot(velocity_profile, y)
plt.xlabel('Velocity')
plt.ylabel('y')
plt.title(f'Velocity Profile at x = {xpos}')
plt.show()
