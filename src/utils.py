from enum import Enum
import math
import pickle
import time
import numpy


class EncryptionMethod(Enum):
    NOTHING = 'nothing'
    XOR = 'xor'
    SHIFT = 'shift'
    VIGENERE = 'vigenere'


def frequency_analysis(message):
    res = {}

    for c in message:
        if c in res.keys():
            res[c] = res[c] + 1
        else:
            res[c] = 1
    return res

#print(frequency_analysis("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."))

def store_prime_numbers(filename, max_value, with_numpy=False):
    path = Path(__file__).parent.parent / 'res'
    if not os.path.exists(path):
        os.makedirs(path)

    if with_numpy:
        prime_numbers = primesfrom2to_numpy(max_value)
    else:
        prime_numbers = primes2(max_value)

    dbfile = open(path / filename, 'ab')
    db = {'prime_numbers': prime_numbers}
     
    # source, destination
    pickle.dump(db, dbfile)                    
    dbfile.close()
    print(time.time()-a)

def primesfrom2to_numpy(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
                    
def loadData(filename):
    path = Path(__file__).parent.parent / 'res'
    # for reading also binary mode is important
    dbfile = open(path / filename, 'rb')    

    db = pickle.load(dbfile)
    primes = db['prime_numbers']
    dbfile.close()
    return primes

if __name__ == "__main__":
    store_prime_numbers("PrimeNumbersNumpy", int(math.pow(2, 32)), True)
    store_prime_numbers("PrimeNumbersNumpy5000", 5000, True)
    primes_numpy = loadData("PrimeNumbersNumpy")
    primes_numpy_5000 = loadData("PrimeNumbersNumpy5000")
    print(len(primes_numpy))
    print(len(primes_numpy_5000))
