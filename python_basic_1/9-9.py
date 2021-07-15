num_list = list(range(1, 11))
even_list = list(filter(lambda x: x % 2 == 0, num_list))
result_list = list(map(lambda x: x**2, even_list))
print(result_list)