import numpy as np
rng = np.random.default_rng(12345)

print('# exercise 1')
my_list = [(x * 10) for x in range(1, 11)]
my_np_list = np.array(my_list)
my_np_mat = my_np_list.reshape(5, 2)
print(my_np_mat)

print('# exercise 2')
# my_arr_2 = np.arange(10, 101, 10).reshape(5, 2)
my_arr_2 = np.linspace(10, 100, 10).reshape(5, 2)
print(my_arr_2)

print('# exercise 3')
random_array = rng.random(9).reshape(3, 3)
print(random_array)
