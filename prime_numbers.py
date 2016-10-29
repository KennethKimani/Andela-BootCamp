import math

def all_prime_numbers_below_n(num):

    #check divisors from 2 to sqrt(n) only instead of from 2 to n-1
    for num in range(2,num):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
           print num


n = int(input("Enter max range number: "))
all_prime_numbers_below_n(n)
