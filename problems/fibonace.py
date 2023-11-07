# generate fibonacci function using recursion
def generate_fibonacci(num):
    fib_sequence = [0, 1]
    while len(fib_sequence) < num:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

num = int(input("Enter the number of Fibonacci terms to generate: "))
fibonacci_sequence = generate_fibonacci(num)
print("Fibonacci Sequence:", fibonacci_sequence)
