import numpy as np

print('#### vector')
my_list = [1, 2, 3]
print(my_list)

np_array = np.array(my_list)
print(np_array)

print('#### two-dimensional matrices')
my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_mat = np.array(my_mat)
print(np_mat)

print('### properties')
print(np_mat.ndim)
print(np_mat.shape)
print(np_mat.size)
print(np_mat.dtype)

print('#### arange')
my_arange = np.arange(0, 11, 2)
print(my_arange)

print('#### array of zeros')
my_zeros = np.zeros(7)
print(my_zeros[0])
print(my_zeros)

print('#### two-dimensional array of zeros')
my_two_dimensional_zeros = np.zeros((7, 7))
print(my_two_dimensional_zeros)

print('#### array of ones')
my_two_dimensional_ones = np.ones((7, 7))
print(my_two_dimensional_ones)


print('#### linspace')
# spacing = (stop=10 - start=0) / (num=5 - 1) =2.5
# 0
# 0+2.5 = 2.5
# 2.5 + 2.5 = 5
# 5 + 2.5 = 7.5
# 7.5 + 2.5 = 10
my_linspace = np.linspace(0, 10, 5)
print(my_linspace)

print('### eye')
my_eye = np.eye(7)
print(my_eye)


print('### random generator')
rng = np.random.default_rng(12345)
print(rng)
print(rng.normal())
print(rng.random())

print('### rand')
my_random = np.random.rand(7)
print(my_random)

print('### randn')
# + and - numbers, use randn(7, 7) to get a matrix
my_random = np.random.randn(7)
print(my_random)

print('### randint')
my_random_int = np.random.randint(1, 10, 3)
print(my_random_int)

print('### randint')
my_random_int = np.random.randint(1, 10, 3)
print(my_random_int)

print('### reshape')
my_reshape_range = np.arange(25)
print(my_reshape_range)
my_reshape = my_reshape_range.reshape(5, 5)
print(my_reshape)

print('### max min')
my_max_min_range = np.random.rand(25)
print(my_max_min_range)
print(f'max: {my_max_min_range.max()}')
print(f'max index: {my_max_min_range.argmax()}')
print(f'min: {my_max_min_range.min()}')
print(f'min index: {my_max_min_range.argmin()}')

