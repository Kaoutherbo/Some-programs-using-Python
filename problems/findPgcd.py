def find_pgcd():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    while num2:
        num1, num2 = num2, num1 % num2

    print("The greatest common divisor (PGCD) is:", num1)

find_pgcd()
