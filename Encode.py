#Shift Encoding : Add Int to a table of Int
def shift(array, shift_value):
    res = ""
    new_Array = []

    for i in range(len(array)):
        new_Array.append(array[i] + shift_value)
    
    return new_Array

res = shift([123,23,21,34,65], 12)



def xor(message, xor_value):
    res = ""

    for car in message:
        res += chr(ord(car)^xor_value)

    return res
