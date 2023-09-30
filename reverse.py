def reverse_integer():
    x = int(input("Enter an integer: "))
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    reversed_x = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
    return reversed_x if INT_MIN <= reversed_x <= INT_MAX else 0

result = reverse_integer()
print("Reversed Integer:", result)
