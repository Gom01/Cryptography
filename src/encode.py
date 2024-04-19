import math
import random
import numpy as np
import time
from .utils import loadData

#Saved primes numbers
array_prime_numbers = loadData("PrimeNumbersNumpy")
array_prime_numbers5000 = loadData("PrimeNumbersNumpy5000")

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

#Vigenere encoding (need a keyword)
def vigenere(array, keyword) :
    #Convert keyword to table[Int]
    new_Array = []
    keyArray = []
    for c in keyword :
        keyArray.append(ord(c))
    j = 0
    i = 0
    #Add value of the letter to the Int
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

#RSA encoding use n and e to create a message
def rsa(array, n, e):
    res = []
    for a in array:
        temp_e = e
        encoded_car = 1
        while temp_e > 0:
            if temp_e % 2 == 1:
                encoded_car = (encoded_car * a) % n
            temp_e = temp_e >> 1
            a = (a * a) % n
        res.append(encoded_car)
    return res


#Key generation RSA
def generate_rsa_keys():
    prime_numbers = [int(np.random.choice(array_prime_numbers)), int(np.random.choice(array_prime_numbers))]
    p = prime_numbers[0]
    q = prime_numbers[1]
    n = p * q
    k = (p - 1) * (q - 1)

    e = generate_rsa_e(k)
    b, d = extended_gcd(k, e)
    if b >= 0:
        b = b-e
        d = d+k
        if b >= 0:
            b = -b
            d = -d
    
    return [(n, e), (n, d)]

#Calculate the e which should be coprime and smaller than k
def generate_rsa_e(k):
    x = 0
    e = 0
    while x != 1:
        e = random.randint(2, k-1)
        x = math.gcd(k, e)
    return e
#Find d and b
def extended_gcd(a, b):
    if b == 0: return 1, 0
  
    x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return x, y

def modPow(b, m, e):
    if m == 1:
        return 0
    r = 1
    b = b % m
    while e > 0:
        if e % 2 == 1:
            r = (r*b) % m
        b = (b*b) % m
        e = e >> 1
    return r

#Diffie Hellman encoding
def generatediffieHellmanKeys() :
    p = int(np.random.choice(array_prime_numbers5000))
    g = generator(p)
    return(p,g)


#Check if congruent or not (for generator)
def notCongruent(g,primeNumbers,n) :
    for k in range(len(primeNumbers)):
        a = int((n-1)/primeNumbers[k])
        if pow(a,g,n) == 1 :
            return False
    return True

def pow(a,g,n):
    temp_a = a
    res = 1
    while temp_a > 0:
        if temp_a % 2 == 1:
            res = (res * g) % n
        temp_a = temp_a >> 1
        g=(g*g)% n
    return res



def find_prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    unique_factors = list(set(factors))
    return unique_factors
#Creation of the generator
def generator(n):
    arrayOfPrime = find_prime_factors(n-1)
    # look if g is not congruent
    isFalse = False
    while not isFalse:
        g = random.randint(1, 2**16)
        isFalse = notCongruent(g, arrayOfPrime, n)
    return g

if __name__ == "__main__":

    a = time.time()
    keys = generate_rsa_keys()
    encoded = rsa([84, 200, 345, 3048, 32, 5], *keys[0])
    print(time.time()-a)


