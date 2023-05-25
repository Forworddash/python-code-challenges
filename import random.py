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
def netWorth():
    investments = int(input('enter the amount of money in your investment account: '))
    cheq = int(input('enter the amount of money in your chequing account: '))
    savings = int(input('enter the amount of money in your savings account: '))
    emergency = int(input('enter the amount of money in your emergency fund: '))
    cash = int(input('enter the amount of cash you have on hand: '))
    silver = int(input('enter the amount of money in silver/metals: '))
    misc = int(input('enter the amount of money in misc objects: '))
    car = int(input('enter the value of your vehicle: '))
    student_loans = int(input('enter the amount of money you owe on your student loans: '))
    credit_card = int(input('enter the amount of money you owe on your credit card: '))

    assets = [investments, cheq, savings, emergency, cash, silver, misc, car]
    liabilities = [student_loans, credit_card]

    total_assets = sum(assets)
    total_liabilities = sum(liabilities)

    net_worth = total_assets - total_liabilities

    print("Here's your net worth: {}".format(net_worth))
    

def compoundInterest():
    # Step 1
    initial_investment = int(input("Enter your initial investment: "))

    # Step 2
    monthly_contribution = int(input("How much will you be contributing monthly: "))
    years_investing = int(input("Enter the number of years you'll be investing: "))

    # Step 3
    interest_rate = float(input("Enter your expected interest rate (in percentage): ")) / 100

    compound_frequency = 12

    def compound():
        total_amount = initial_investment

        for i in range(years_investing):
            total_amount *= (1 + interest_rate / compound_frequency)  # Calculate compound interest

            for j in range(compound_frequency):
                total_amount += monthly_contribution  # Add monthly contribution

        print("Total amount after", years_investing, "years:", round(total_amount, 2))

def calculator():
    integer_1 = int(input("Pick an integer: "))
    integer_2 = int(input("pick a 2nd integer: "))

    mulitply = integer_1 * integer_2
    divide = integer_1 / integer_2
    subtract = integer_1 - integer_2
    addition = integer_1 + integer_2

    print("{} divided by {} is {}".format(integer_1, integer_2, divide))
    print("{} times {} is {}".format(integer_1, integer_2, mulitply))
    print("{} minus {} is {}".format(integer_1, integer_2, subtract))
    print("{} plus {} is {}".format(integer_1, integer_2, addition))
 

def mapping():
    map = [ 
        [1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1]
    ]

    for i in range(len(map)):
        for j in range(len(map[i])):
            # print(map[i][j])
            if map[i][j] == 1:
                print("@", end="")
            else:
                print(" ", end="")
        print()
# mapping()

def countTo100():
    x = 100
    y = 0
    for y in range(x):
        y += 1
        print(y)

# easier

def countTo100v2():
    for y in range(1, 101):
        print(y)

# try sorting
def sortSmallestToBiggest():
    x = [0, 1, 32, 40, 99, -5, 10, 20, 231, 49, 2, 11]
    for i in range(len(x)):
        if x[i] < 0:
            print(x[i])

def bubbleSort(numbers):

    n = len(numbers)
    
    for i in range(n-1):
        print("n is: {}".format(n))
        print("i is: {}".format(i))
        for j in range(n-1-i):
            print("n-i is: {}".format(n-i))
            print("j is: {}".format(j))
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

numbers = [4, 2, 3]
# bubbleSort(numbers)
# print(numbers)

# list xor, is membership
def list_xor(n, list1, list2):
    in_list1 = n in list1
    in_list2 = n in list2

    print(in_list1 ^ in_list2)   
 
# list_xor(3, [1, 2, 3], [0, 2, 7])

#calculate averages
def calculate_average(list1):
    # if the list is empty, return 0
    if not list1:
        return 0

    sum_of_list = round(sum(list1) / len(list1), 2)

    return sum_of_list


calculate_average([1, 2, 3, 4, 5])

# reverse words
def reverse_words(string):
    words = string.split() # split the string into words

    reversed_words = words[::-1] # reverse the words
    
    reversed_sentence = " ".join(reversed_words) # join the reversed words into a string

    print(reversed_sentence)

# reverse_words('test 1 2 3')

# palindrome check
def is_palindrome(string):
    processed_string = "".join(char.lower() for char in string if char.isalpha())
    
    reversed_string = processed_string[::-1]

    if processed_string == reversed_string:
        return True
    else:
        return False

# is_palindrome('A man, a plan, a canal: Panama')


#count the vowels
def count_vowels(string):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    vowel_count = 0
    
    for i in string.lower():
        if i in vowels:
            vowel_count += 1

    return vowel_count

# count_vowels('OpenAI Chatbot')

# unique elements
def unique_elements(list1, list2):

    x = sorted(set(list1 + list2))# concatonates lists, removes duplicates, sorts lowest to highest
    return x

# unique_elements([1, 2, 5], [6, 5, 3])

# remove duplicates
def remove_duplicates(list1):

    my_list = list1
    my_list = list(dict.fromkeys(my_list))
    return my_list


# remove_duplicates([1, 2, 2, 3])

# matrix transpose
def transpose_matrix(matrix):
    transpose = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose[j][i] = matrix[i][j]

    return transpose
# transpose_matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

#unique common elements

def unique_common_elements(list1, list2):
    mylist = list1 + list2
    master_list = []
    common_elements = []

    for i in mylist:
        if i not in master_list:
            master_list.append(i)
        else:
            common_elements.append(i)

    return common_elements
# unique_common_elements([1, 2, 3], [1, 4, 5])

# hello world
def hello_world():
    print('Hello, World!')
# hello_world()

#sum of 2 nums
def sum_of_two_numbers(num1, num2):

    total = num1 + num2
    return total


# sum_of_two_numbers(3, 4)

#max of 2 numbers
def max_of_two_numbers(num1, num2):

    if num1 < num2:
        return num2
    else: 
        return num1

max_of_two_numbers(34, 4)

