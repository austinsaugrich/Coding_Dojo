# countdown, pass a number and countdown from the number

def countdown(int):
    for i in range(int, 0, -1):
        print(i)


countdown(5)

# print and return 1 and 2 value of a list

nums = [1, 2]


def printreturn(list):
    print(list[0])
    return list[1]


printreturn(nums)

# returns the first value of a list plus the length of the list

nums = [1, 2, 3, 4, 5]


def first_plus_length(list):
    sum = 0
    sum = list[0] + len(list)
    print(sum)


first_plus_length(nums)

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False


def values_greater_than_second(list):
    new_list = []
    if len(list) < 2:
        return False
    else:
        for i in list:
            if i > list[1]:
                new_list.append(i)
    print(len(new_list))
    return new_list


nums = [5, 2, 3, 2, 1, 4]
values_greater_than_second(nums)

# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.


def length_and_value(int1, int2):
    new_list = []
    for i in range(int1):
        new_list.append(int2)
    print(new_list)


length_and_value(4, 7)
