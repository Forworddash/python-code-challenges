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

# max_of_two_numbers(34, 4)

import math

def is_prime(int1):
    if int1 < 2:
        return False

    for i in range(2, int(math.sqrt(int1)) + 1):
        if int1 % i == 0:
            return False
        
    return True
# is_prime(5)

# fizzbuzz
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
# fizz_buzz()

# word frequency
def word_frequency(str):

    words = str.split() # split letters into words
    

# word_frequency('this is a string')

# sum of squares
def sum_of_squares(n):

    sum = 0

    for i in range(1, n + 1):      
        if n >= 0:
            sum += pow(i, 2)
        else:
            return False
    return sum

# sum_of_squares(4)

# compressed string
def compress_string(str1):
    
    count = ''
    
    for i in str1:
        if i not in count:
            count += i
            count += str((str1.count(i)))
    if len(count) < len(str1):
        print(count)
    else: 
        print(str1)    


# compress_string('aaabbbs')
# updated one 
def compress_string(str1):
    compressed = '' # initialize variable 'compressed' with empty string
    count = 1 # initialize variable 'count' to 1

    for i in range(len(str1)): # for loop from 1 > 7 (length of string)
        if i == len(str1) - 1 or str1[i] != str1[i + 1]: # if i is 6 or i does not equal the next i 
            compressed += str1[i] + str(count) # add i + number to 'compressed' variable
            count = 1 # set current i count to 1
        else:
            count += 1 # set current i count to num of i's

    if len(compressed) < len(str1): # print the shortest string between str1 & compressed
        print(compressed) 
    else:
        print(str1) 

# compress_string('aaabbbs')
# sentence reversal
# def reverse_sentence(str1):
    # reversed_words = str1[::-1]
    # print(reversed_words)
# reverse_sentence('this is a sentence')
def reverse_sentence(str1):
    words = str1.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    print(reversed_sentence)

# reverse_sentence('this is a test')
# has unique characters
def has_unique_characters(str1):
    no_duplicates = set(str1)
    if len(str1) > len(no_duplicates):
        return False
    else:
        return True

# has_unique_characters('abcdee')
# anagram check
def is_anagram(str1, str2):
    #string_one = [str1]
    #string_two = [str2]
    anagram = 0

    for i in str1:
        if i in str2:
            anagram += 1
        else:
            print('False')
    print(anagram)
    if anagram == len(str1):
        print('anagram detected')
    else:
        print('anagram not detected')

    print(anagram)

# is_anagram('silent', 'listen')
# reverse words
def reverse_words(str1):

    words = str1.split()
    reversed_words = ''

    for word in words:
        reversed_words += word[::-1] + ' '

    reversed_words = reversed_words.strip()

    print(reversed_words)

# reverse_words('Hello World')

# unique elements
def unique_elements(list1):
    unique_list = []
    seen = set()

    for element in list1:
        if element not in seen:
            unique_list.append(element)
            seen.add(element)
    print(unique_list)

# unique_elements([4, 3, 6, 7, 7, 1])

def unique_elements(list1):
    new_list = []
    seen_dict = set()

    for i in list1:
        if i not in seen_dict:
            new_list.append(i)
            seen_dict.add(i)
    print(new_list)
# unique_elements([1, 1, 1, 5, 2, 2, 4])
# common elements
def common_elements(list1, list2):
    common_nums = []

    for i in list1:
        if i in list2:
            common_nums.append(i)
    return common_nums

# common_elements([1, 4, 5], [1, 2, 5, 5, 3])
# palindrome
def is_palindrome(str1):
    reversed_string = str1[::-1]

    if reversed_string == str1:
        return True
    else:
        return False

# is_palindrome('alisla')
#count vowels
def count_vowels(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for i in str1:
        if i in vowels:
            vowel_count += 1

    return vowel_count
# count_vowels('alice')
# find duplicates
def find_duplicates(list1):
    new_list = []
    duplicates = []

    for i in list1:
        if i not in new_list:
            new_list.append(i)
        elif i in new_list:
            duplicates.append(i)

    print(new_list)
    print(duplicates)

# find_duplicates([1, 4, 2, 2, 3, 4, 5])
# anagram better
def is_anagram(str1, str2):
    sorted_string_1 = sorted(str1.lower())
    sorted_string_2 = sorted(str2.lower())

    if sorted_string_1 == sorted_string_2:
        return True
    else:
        return False

# is_anagram('test', 'estt')
# remove duplicates
def remove_duplicates(list1):
    dict1 = set(list1)
    no_duplicates = list(dict1)

    return no_duplicates
# remove_duplicates([1, 1, 2, 2, 3, 3])
# find missing number
def find_missing_number(list1):
# first find sum of number 1 to n (n * (n + 1)) / 2
    n = list1[-1]
    result = (int((n * (n + 1)) / 2) - sum(list1))

    return result

# find_missing_number([1, 2, 3, 4, 6])
# max subarray
def max_subarray_sum(arr):
    n = len(arr) # n = 9 (length of list of nums)
    maxSum = -1e8 # ?
    currSum = 0

    for i in range(0, n): # for i in range (0 to 9)
        currSum = currSum + arr[i] # current sum = current sum + current i (-4)
        if (currSum > maxSum): # if current sum is smaller than the max, then set max to current
            maxSum = currSum
        if (currSum < 0): # if current sum is less than 0, set current sum to 0
            currSum = 0

    return maxSum


# max_subarray_sum([-4, -3, -2, -1, 0, 1, 2, 3, 4])
# find duplicates
def find_duplicates(arr):
    new_list = []
    duplicates = []

    for i in arr:
        if i not in new_list:
            new_list.append(i)
        else:
            duplicates.append(i)

    return duplicates
# find_duplicates([1, 2, 3, 4, 4, 5])
# is pangram 
def is_pangram(str1):

    letters = set(c.lower() for c in str1 if c.isalpha())

    if len(letters) == 26:
        return True
    else:
        return False


# is_pangram('The quick brown fox jumps over the lazy dog')
# average list
def average_list(list1):
    new_list = float(sum(list1) / len(list1))
    
    return new_list


# average_list([1, 3, 3, 4, 4])
# fizzbuzz
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

# fizz_buzz()
# prime number checker #math.sqrt(4)
def is_prime(int1):
    square_root = int(math.sqrt(int1))

    if int1 < 2:
        return False

    for i in range(2, square_root + 1):
        if int1 % i == 0:
            return False
        else:
            return True
# is_prime(60)
# anagram
def is_anagram(str1, str2):

    sorted_string_1 = sorted(str1.lower())
    sorted_string_2 = sorted(str2.lower())

    if sorted_string_1 == sorted_string_2:
        return True
    else:
        return False

# is_anagram('silent', 'listen')
# duplicate element finder
def duplicate_element(list1):

    new_list = []
    duplicates = []

    for i in list1:
        if i not in new_list:
            new_list.append(i)
        else:
            duplicates.append(i)

    return duplicates
# duplicate_element([1, 2, 3, 3, 4, 5])
# map game
# def map_game():
#     map = [
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 4, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#     ]

#     bad_sectors = random.randint(1, 36)


#     for i in range(len(map)):
#         for j in range(len(map[i])):
#             # map[i][j] = random.randint(0, 1)
#             if map[i][j] == 4:
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print()
            # if map[i][j] == bad_sectors:
            #     print('#', end="")
            # else:
            #     print(' ', end='')
        # print()
    # print(bad_sectors)
#map_game()
def find_the_tallest_number(list1):
    highest_number = max(list1)
    print(highest_number)
        

find_the_tallest_number([1, 2, 3, 4, 53, 121, 7])