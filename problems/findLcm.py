def find_lcm():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    def pgcd(a, b):
        if b == 0:
            return a
        return pgcd(b, a % b)
    
    lcm = (num1 * num2) // pgcd(num1, num2)
    print("The least common multiple (LCM) is:", lcm)

find_lcm()
