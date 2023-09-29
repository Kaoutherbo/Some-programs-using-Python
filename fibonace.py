# generate fibonacci function using recursion
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

n = int(input("Enter the number of Fibonacci terms to generate: "))
fibonacci_sequence = generate_fibonacci(n)
print("Fibonacci Sequence:", fibonacci_sequence)
