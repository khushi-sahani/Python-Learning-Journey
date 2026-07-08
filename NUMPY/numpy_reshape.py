import numpy as np

arr = np.array([1,2,3,4,5,6])

print("Original")
print(arr)

new_arr = arr.reshape(2,3)

print("Reshaped")
print(new_arr)

print("Flatten")
print(new_arr.flatten())