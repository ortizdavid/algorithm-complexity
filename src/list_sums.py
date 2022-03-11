from functools import reduce
import random

class ListSum:

    @classmethod
    def sum1(cls, L):
        total = 0
        for i in range(len(L)):
            total = total + L[i]
        return total
    
    @classmethod
    def sum2(cls, L):
        total = 0
        [total := total + x for x in L]
        return total

    @classmethod
    def sum3(cls, L):
        return reduce(lambda x, y: x + y, L)
        
    @classmethod
    def sum4(cls, L):
        return sum(L)

    @classmethod
    def generate_list(cls, N):
        L = []
        for i in range(1, N):
            elem = random.randint(0, 100) - 2 + i
            L.append(elem)
        return L


