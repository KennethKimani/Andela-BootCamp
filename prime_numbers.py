import math

def all_prime_numbers_below_n(num):

    #The only even prime number
    print 2
    for num in range(3,num,2):
        #increment range you by 2, and only check odd numbers
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
           print num

n = int(input("Enter max range number: "))
all_prime_numbers_below_n(n)
