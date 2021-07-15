num_list = [1, 2, 3, 4, 3, 2, 1]

def remove_duple(num_list):
    num_list = set(num_list)
    return list(num_list)

list_removed = remove_duple(num_list)
print(num_list)
print(list_removed)
