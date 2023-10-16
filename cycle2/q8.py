import numpy as np
print("Register No:SJC22MCA-2019 \n:Name:Blessey Maria Kurian \n:Batch:S3 MCA \n****************\n")
# Create a 1D numpy array
arr_1D=np.array([1, 2, 3, 4, 5])

# Insert a value (e.g., 10) at a specific index (e.g., index 2)
new_arr_1D = np.insert(arr_1D, 2,10)

# Print the updated array
print(new_arr_1D)
# Create a 2D NumPy array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Insert a row (e.g., [7, 8, 9]) at a specific index (e.g., index 1) along axis 0 (rows)
new_arr_2d = np.insert(arr_2d, 1, [7, 8, 9], axis=0)

# Print the updated array
print(new_arr_2d)

