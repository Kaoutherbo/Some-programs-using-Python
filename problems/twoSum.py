def two_sum():
    nums = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    target = int(input("Enter the target sum: "))
    
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return None

result = two_sum()
print("Indices:", result)

