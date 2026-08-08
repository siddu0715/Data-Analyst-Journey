def minimum(nums):
    return min(nums)
num= [int(x) for x in input("Enter numbers separated by space: ").split()]
minimum_value = minimum(num)
print("The minimum value is:", minimum_value)