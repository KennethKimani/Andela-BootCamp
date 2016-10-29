def all_prime_numbers_below_n(num):

    for num in range(2,num):

        prime = True

        for x in range(2,num):

            if (num%x==0):
                prime = False

        if prime:
            print(num,"is prime")


n = int(input("Enter max number: "))
all_prime_numbers_below_n(n)
