#Shift Encoding : Add Int to a table of Int
def shift(array, shift_value):
    res = ""
    new_Array = []

    for i in range(len(array)):
        new_Array.append(array[i] + shift_value)
    
    return new_Array




#Xor Encoding : Xor two Int
def xor(array, xor_value):
    res = ""
    new_Array = []

    for i in range(len(array)):
        new_Array.append(array[i]^xor_value)

    return new_Array