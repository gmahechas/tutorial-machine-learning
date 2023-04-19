import numpy as np

my_arange = np.arange(0, 11)
print(my_arange)

print(my_arange[8])

print(my_arange[0:5])

print(my_arange[5:])

# my_arange[0:5] = 100
# print(my_arange)

slice_of_arr = my_arange[0:6]
print(slice_of_arr)
slice_of_arr[:] = 99
print(slice_of_arr)
print(my_arange)  # it has been modified

my_arange_copy = my_arange.copy()
my_arange_copy[:] = 100
print(my_arange_copy)
print(my_arange)

print('# 2d indexing')

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)
print(arr_2d[2:, 1:])

print('# conditional selection')
other_arr = np.arange(1, 11)
bool_arr = other_arr > 5
print(bool_arr)
print(other_arr[other_arr > 5])

new_arr_2d = np.arange(50).reshape(5, 10)
print(new_arr_2d)
print(new_arr_2d[1:3, 3:5])
print(new_arr_2d[1:2, 3:5])
print(new_arr_2d[2:3, 3:5])
