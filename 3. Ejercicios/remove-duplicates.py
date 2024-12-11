
def remove_duplicates(input_array):
    return list(set(input_array))


input_array = [1, 2, 3, 4, 2, 5, 6, 1]
result = remove_duplicates(input_array)
print(result)   # Prints [1, 2, 3, 4, 5, 6]