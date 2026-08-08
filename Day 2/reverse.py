def reverse_list():
    lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
    reversed_lst = lst[::-1]
    print("The reversed list is:", reversed_lst)
reverse_list()