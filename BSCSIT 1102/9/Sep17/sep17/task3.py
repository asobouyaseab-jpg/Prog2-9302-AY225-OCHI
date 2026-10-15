import math 
import random
import time

def _prime(n):
   if n < 2:
    return False
   for i in  range (2, int (n **0.5)+1):
      if n % i == 0:
       return False
   return True

def prime_list(N):
   return[n for n in range(2, N + 1) if _prime(n)]

#example: N = 50
N = 50
print(prime_list(N))