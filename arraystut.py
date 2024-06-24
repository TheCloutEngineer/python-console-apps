import numpy as np

my_array = np.array([1, 2, 3, 4, 5])

my_array_two = np.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype=np.float64)

print(my_array[0])

print(my_array[1])

print(my_array[2])

print(my_array[-1])

my_array[2] = 99

print(my_array[2])

# modifying arrays

print(my_array)


my_array_three = np.array([1, 2, 3, 4, 5])

my_array_four = np.array([6, 7, 8, 9, 10])

# add element wise
result = my_array_three + my_array_four

print(result)

my_arr = np.array([7, 3, 1, 2, 4, 5, 6])

min_value = np.min(my_arr)

max_value = np.max(my_array)

sorted_arr = np.sort(my_arr)

print(sorted_arr)

# reverse order using flip from original order but flip using my_arr on l:33
reverse_arr = np.flip(my_arr)

print(reverse_arr)