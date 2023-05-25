import random
from math import sqrt


# prints 1 to 100
def zeroToHundred():
    for i in range(1, 101):
        print(i)
# zeroToHundred()

#displays the map as 1 = # and 0 = space
def mapping():
    map = [
        [1, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0]
    ]

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()

# sort list of integers by changing the variable
def sortFunction():
    numbers = [1, 5, -34, 0, -92, -2, 59, 61]
    numbers.sort()
    print(numbers)
# sortFunction()

#sorting without modifying the string
def sortFunctionV2():
    numbers = [1, 5, -34, 0, -92, -2, 59, 61]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
    # print(numbers)
# sortFunctionV2()

# return uppercase indices of string
def capital_indexes(string):
    
    list = []
    
    for i, char in enumerate(string):
        if char.isupper():
           list.append(i)
    
    print(list)
 
# capital_indexes("HeLlo")

# detect how many people are online
def online_count(statuses):
    count_online = 0

    for status in statuses.values():
        if status == "online":
            count_online += 1

    return count_online

def main():
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }

    count = online_count(statuses)
    print(count)


# if __name__ == "__main__":
    # main()


# random number
def random_number():
    random_number = random.randint(1, 100)
    print(random_number)
    
# random_number()

# type check
def only_ints(par1, par2):

    if type(par1) is int and type(par2) is int:
        return True
    else:
        return False
   

# only_ints('a', 6)

# detect double letters
def double_letters(param1):

    # iterate through 0 to 8   
    for i in range(len(param1) - 1):
        # if current char == char(next) print true
        if param1[i] == param1[i + 1]:
            return True
    return False


# double_letters("strdding")

# divisble by 3
def div_3(param1):
    if param1 % 3 == 0:
        return True
    else:
        return False
# div_3(2)

# is even or odd
def even_odd(param1):
    if param1 % 2 == 0:
        print('this is even')
    else:
        print('this is odd')
# even_odd(32132)

# true if all params are True bool else false
def triple_and(param1, param2, param3):
    if param1 and param2 and param3:
        return True
    else:
        return False
# triple_and(True, True, True)

# check if all list is matching
def all_equal(my_list):  

    if len(set(my_list)) == 1:
        print('true')
    else:
        print('false')
        
# all_equal([2, 2, 2])

# calculate area of triangle are = 1/2 bh
def calculate_rectangle_area(side1, side2):

    area = side1 * side2
    return area
    

# calculate_rectangle_area(2, 4)

# is even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
# is_even(5)

# count occurences in string
def count_char_occurences(text, target):
    num_of_occur = 0
    for i in text:
        if i == target:   
            num_of_occur += 1

    return num_of_occur

# count_char_occurences('how are you, hh', 'o')

# duplicates from a list
def remove_duplicates(list1):

    filtered_list = list(dict.fromkeys(list1))
    return filtered_list

# remove_duplicates([1, 2, 2, 2, 4, 5])

#number classification
def classify_number(int1):

    if int1 > 0:
        print('Positive')
    elif int1 < 0:
        print('Negative')
    elif int1 == 0:
        print('Zero')
    elif int1 % 2 == 0:
        print('Even')
    else:
        print('Odd')
    
# classify_number(4)
