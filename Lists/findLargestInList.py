def find_largest_element():
    numbers = [float(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    largest = max(numbers)
    print("The largest number is:", largest)

find_largest_element()
