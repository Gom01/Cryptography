from random import randint
from math import gcd

#Shift Encoding : Add Int to a table of Int
def shift(array, shift_value):
    new_Array = []

    for i in range(len(array)):
        new_Array.append(array[i] + shift_value)
    
    return new_Array


#Xor Encoding : Xor two Int
def xor(array, xor_value):
    new_Array = []

    for i in range(len(array)):
        new_Array.append(array[i]^xor_value)

    return new_Array


def vigenere(array, keyword) :
    #Convert keyword to table[Int]
    new_Array = []
    keyArray = []
    for c in keyword :
        keyArray.append(ord(c))

    j = 0
    i = 0
    while i <= len(array)-1:
        if j <= len(keyArray) - 1 :
            value = array[i] + keyArray[j]
            new_Array.append(value)
        else :
            j = -1
            i -= 1

        i += 1
        j += 1

    return(new_Array)

def generate_rsa_keys():
    prime_numbers = [4549, 5623]
    p = prime_numbers[0]
    q = prime_numbers[1]
    n = p * q
    k = (p - 1) * (q - 1)

    e = generate_rsa_e(k)
    gcd, b, d = extended_gcd(k, e)

    if b >= 0:
        b = -b
        d = -d
    
    return [(n, e), (n, d)]

def generate_rsa_e(k):
    x = 0
    e = 0
    while x != 1:
        e = randint(2, k-1)
        x = gcd(k, e)
    return e


def extended_gcd(a, b):
   if b == 0: return a, 1, 0
  
   gcd, x1, y1 = extended_gcd(b, a % b)
   x = y1
   y = x1 - (a // b) * y1
   return gcd, x, y

if __name__ == "__main__":
    print(extended_gcd(13, 21))
