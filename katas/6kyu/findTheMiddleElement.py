def gimme(input_array):
    return input_array.index(sorted(input_array)[1])

print(gimme([2,3,1]))