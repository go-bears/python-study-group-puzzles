"""
Define a function that counts elements the elements in a list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""
string = "hello"
char_counter = 0

for letter in string: char_counter += 1

print char_counter    


"""
Define a function max_of_three() that takes three numbers as arguments via raw_input() and the function returns the largest of them
"""
# num_list = []
# while (len(num_list) < 3):
#     user_num = input("I need three numbers. please input a number: ")
#     num_list.append(user_num)
    
# if (len(num_list) == 3):
#     print "I have all the numbers I need. Thanks!"
    

# def max_of_three(num_list):
#     for i in num_list: 
#         high_num = i
#         if  high_num < i: 
#             high_num = i
#     return high_num 
        
    
# print max_of_three(num_list), "is the highest number"

"""
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.
"""


def is_palindrome(word):
    reverse_index = range(-1, -1*(len(word) - 1), -1)
    print len(word)
    if len(word) %2 ==0:
        for letter in word:
            for j in reverse_index:
                    if letter == word[j]:
                        print word, "is a palindrome"
                        return True
    else:
        middle = len(word)/2
        first_half = word[0:middle]
        second_half = [word[j] for j in reverse_index if j > ((middle+1)*-1)]
        second_half = "".join(second_half)
                #print word[-1: (-1*(len(word)/2) -1):]
        if first_half == second_half:
            print word, "is a palindrome"
            return True
        else:
            print word, "is not a palindrome"
            return False
        


# is_palindrome("radar")
# is_palindrome("noon")
# is_palindrome("dog")

"""
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

take it further:
write a function function that takes in a string via raw_input() 
returns the total number of vowels that are in the string.
Revise the function so that the function that it outputs the count of each vowel in the string
"""
def is_vowel(char):
    char = char.lower()
    vowel = ["a", "e", "i", "o", "u"]
    if (char in vowel): return True
    else: return False

# print "is a vowel? ", is_vowel("i")
# print "is a vowel? ", is_vowel("k")
# print "is a vowel? ", is_vowel("O")

"""
Write a function translate() that encrypts a phrase into "robber's language". That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".
Take it further:
write a function that translates strings in "robber's language" back into english:
"""
language = "this is fun"
vowel = ["a", "e", "i", "o", "u"]


def translate(string):
    robber_lang = []
    for character in language:
        if character not in vowel and character != " ":
            character = character + "o" + character
        robber_lang.append(character)
    
    robber_lang = "".join (robber_lang)
        
   
    
translate(language)


"""
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.




take it further:
Define a third function that processes (multiply, addition, factorial, etc) the returned outputs of the sum() and multiply() function
"""

nums_list = [1,2,3,4]

def sums(nums):
    sums = 0
    for x in nums:
        sums += x
    return sums

def multiply(nums):
    multiplied= 1
    for z in nums:
        multiplied *=z
    return  multiplied
    
def more_sums():
    num1 = multiply(nums_list)
    num2 = sums(nums_list)
    total = num1 + num2
    return total

print more_sums()
    

sums(nums_list)
multiply(nums_list)
"""This function sequence below outputs a 2x2 grid:
 
 
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Write a function that draws a similar grid with four rows and four columns.

Take it further: format each square with a unique number using functions

"""
def do_twice(f):
    f()
    f()
def do_four(f):
    do_twice(f)
    do_twice(f)
def print_beam():
    print '+ - - - -',
def print_post():
    print '|        ',
def print_beams():
    do_twice(print_beam)
    print '+'
def print_posts():
    do_twice(print_post)
    print '|'
def print_row():
    print_beams()
    do_four(print_posts)
def print_grid():
    do_twice(print_row)
    print_beams()
print_grid()

"""
credits: exercises borrowed and adapted from Allen Downey and Torbjorn Lager
"""
