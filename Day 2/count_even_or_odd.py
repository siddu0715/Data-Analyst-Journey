def oddeven(nums):
    even_count = 0
    odd_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
nums=[int(x) for x in input("Enter numbers separated by space: ").split()]
result = oddeven(nums)
print(result)