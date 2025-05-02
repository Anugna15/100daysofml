#to create an empty and a full NumPy array
import numpy as np
arr_empty=np.empty((2,3))
arr_full=np.full((2,3),5)
print("Empty array:\n",arr_empty)
print("Full array:\n",arr_full)

#to create a NumPy array with a specific data type
arr_float=np.array([1,2,3],dtype=float)
print("Array with float data type:\n",arr_float)

#to create a NumPy array with zeros and ones
arr_zeros=np.zeros((2,3))
arr_ones=np.ones((2,3))
print("Array of zeros:\n",arr_zeros)
print("Array of ones:\n",arr_ones)

#Find the number of occurrences of a sequence in a NumPy array
arr = np.array([1, 2, 3, 1, 2, 1])
sequence = 1
count = np.count_nonzero(arr == sequence)
print(f"The number of occurrences of {sequence} in the array is: {count}")

#Find the most frequent value in a NumPy array
arr = np.array([1, 2, 3, 1, 2, 1])
unique, counts = np.unique(arr, return_counts=True)
most_frequent = unique[np.argmax(counts)]
print(f"The most frequent value in the array is: {most_frequent}")

#transpose a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr_transpose = np.transpose(arr)
print("Original array:\n", arr)
print("Transposed array:\n", arr_transpose)

#identity matrix
arr_identity = np.eye(3)
print("Identity matrix:\n", arr_identity)

#inverse of a matrix
arr = np.array([[1, 2], [3, 4]])
arr_inverse = np.linalg.inv(arr)
print("Original matrix:\n", arr)
print("Inverse matrix:\n", arr_inverse)

#determinant of a matrix
arr = np.array([[1, 2], [3, 4]])
arr_determinant = np.linalg.det(arr)
print("Original matrix:\n", arr)
print("Determinant of the matrix:\n", arr_determinant)

#ADD BORDER TO ARRAY
arr = np.array([[1, 2], [3, 4]])
arr_bordered = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
print("Original array:\n", arr)
print("Array with border:\n", arr_bordered)

#COMPARE TWO ARRAYS
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 4])
comparison = np.array_equal(arr1, arr2)
print("Are the two arrays equal?:", comparison)

#FLATTEN ARRAY
arr = np.array([[1, 2], [3, 4]])
arr_flattened = arr.flatten()
print("Original array:\n", arr)
print("Flattened array:\n", arr_flattened)

#FIND UNIQUE ELEMENTS IN ARRAY
arr = np.array([1, 2, 2, 3, 4, 4])
unique_elements = np.unique(arr)
print("Original array:\n", arr)
print("Unique elements in the array:\n", unique_elements)

#FIND INDEX OF MAXIMUM ELEMENT IN ARRAY
arr = np.array([1, 2, 3, 4, 5])
max_index = np.argmax(arr)
print("Original array:\n", arr)
print("Index of maximum element in the array:\n", max_index)

#FIND INDEX OF MINIMUM ELEMENT IN ARRAY
arr = np.array([5, 4, 3, 2, 1])
min_index = np.argmin(arr)
print("Original array:\n", arr)
print("Index of minimum element in the array:\n", min_index)

#FIND ELEMENTS GREATER THAN A SPECIFIC VALUE
arr = np.array([1, 2, 3, 4, 5])
greater_than_3 = arr[arr > 3]
print("Original array:\n", arr)
print("Elements greater than 3:\n", greater_than_3)

#FIND ELEMENTS LESS THAN A SPECIFIC VALUE
arr = np.array([1, 2, 3, 4, 5])
less_than_3 = arr[arr < 3]
print("Original array:\n", arr)
print("Elements less than 3:\n", less_than_3)

#FIND ELEMENTS EQUAL TO A SPECIFIC VALUE
arr = np.array([1, 2, 3, 4, 5])
equal_to_3 = arr[arr == 3]
print("Original array:\n", arr)
print("Elements equal to 3:\n", equal_to_3)

#SUM OF ELEMENTS IN ARRAY
arr = np.array([1, 2, 3, 4, 5])
sum_of_elements = np.sum(arr)
print("Original array:\n", arr)
print("Sum of elements in the array:\n", sum_of_elements)

#SUM OF ELEMENTS ALONG A SPECIFIC AXIS
arr = np.array([[1, 2, 3], [4, 5, 6]])
sum_along_axis_0 = np.sum(arr, axis=0)
sum_along_axis_1 = np.sum(arr, axis=1)
print("Original array:\n", arr)
print("Sum along axis 0:\n", sum_along_axis_0)
print("Sum along axis 1:\n", sum_along_axis_1)

#MEAN OF ELEMENTS IN ARRAY
arr = np.array([1, 2, 3, 4, 5])
mean_of_elements = np.mean(arr)
print("Original array:\n", arr)
print("Mean of elements in the array:\n", mean_of_elements)

#MEAN OF ELEMENTS ALONG A SPECIFIC AXIS
arr = np.array([[1, 2, 3], [4, 5, 6]])
mean_along_axis_0 = np.mean(arr, axis=0)
mean_along_axis_1 = np.mean(arr, axis=1)
print("Original array:\n", arr)
print("Mean along axis 0:\n", mean_along_axis_0)
print("Mean along axis 1:\n", mean_along_axis_1)

#MEDIAN OF ELEMENTS IN ARRAY
arr = np.array([1, 2, 3, 4, 5])
median_of_elements = np.median(arr)
print("Original array:\n", arr)
print("Median of elements in the array:\n", median_of_elements)

#MODE OF ELEMENTS IN ARRAY
from scipy import stats
arr = np.array([1, 2, 2, 3, 4])
mode_of_elements = stats.mode(arr)[0][0]
print("Original array:\n", arr)
print("Mode of elements in the array:\n", mode_of_elements)

