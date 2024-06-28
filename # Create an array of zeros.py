import numpy as np
# # Create an array of zeros
# zeros = np.zeros((3, 3))
# print("Zeros array:\n", zeros)

# # Create an array of ones
# ones = np.ones((2, 4))
# print("Ones array:\n", ones)

# # Create an array with a range of values
# range_array = np.arange(0, 10, .5)
# print("Range array:", range_array)

# # Create an array with evenly spaced values
# linspace_array = np.linspace(0, 1, 4)
# print("Linspace array:", linspace_array)


# arr = np.array([1, 2, 3, 4, 5])
# print("Element at index 2:", arr[2])

# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr2)
# print("Element at row 1, column 2:", arr2[0,2])
arr = np.array([1, 2, 3, 4, 5])
print("Slice from index 1 to 4:", arr[1:4])

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Slice first row:", arr2[0, :])
print("Slice first column:", arr2[:, 0])




arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print("Vertical stack:\n", np.vstack((arr1, arr2)))
print("Horizontal stack:\n", np.hstack((arr1, arr2)))
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
