def unshift(array, shift_value):
    new_Array = []

    for i in range(len(array)):
        new_Array.append(array[i] - shift_value)

    return new_Array

def unvigenere(array, keyword) :
    #Convert keyword to array[Int]
    new_Array = []
    keyArray = []
    for c in keyword:
        keyArray.append(ord(c))


    j = 0
    i = 0
    while i <= len(array) - 1:
        if j <= len(keyArray) - 1:
            value = array[i] - keyArray[j]
            new_Array.append(value)
        else:
            j = -1
            i -= 1

        i += 1
        j += 1

    return (new_Array)


