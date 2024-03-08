def unshift(array, shift_value):
    new_Array = []

    for i in range(len(array)):
        new_Array.append(array[i] - shift_value)

    return new_Array
