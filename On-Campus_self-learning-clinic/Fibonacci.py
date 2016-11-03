def Fibonacci(n):
    """Generate Fibonacci sequence from 1 to n"""
    previous = 0
    current = 1

    sequence = [previous, current]
    for i in xrange(1, n):
        tmp = previous
        previous = current
        current += tmp

        sequence.append(current)

    return sequence

m = int(input("Enter max value: "))
print Fibonacci(m)

