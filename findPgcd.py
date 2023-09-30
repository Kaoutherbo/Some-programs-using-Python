def find_gcd():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    while num2:
        num1, num2 = num2, num1 % num2

    print("The greatest common divisor (GCD) is:", num1)

find_gcd()
