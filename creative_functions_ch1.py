
"""
Demonstrate how to use Python's list comprehension  syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
"""
# x[0] = 0
# x[1] = x + 2
# x[2] = x[1] + 4
# x[3] = x[2] + 6

# index = range(10)

# number = range(0, 18, 2)
# print number
# xy = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
# print xy[1]



# add_incremental_evens = [ for i in range(10) for y in range(0, 18, 2):  ]
# print add_incremental_evens

"""
Demonstrate how to use Python's list comprehension  syntax to produce
the list [a, b, c, ..., z ], but without having to type all 26 such characters literally
"""
#unicode alphabet "a" = 97
#unicode alphabet "A" = 65
#To find the ASCII value of a character use the ord() function.
#to get a character from it's ASCII value use the chr() function.


alphabet = [chr(96 + i) for i in range(1, 27)]
upper_alphabet = [chr(64 + i) for i in range(1, 27)]


# print alphabet
# print upper_alphabet

"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).

"""

'''
Write a Python program that outputs all possible strings formed by using the characters
c,a,t,d,o,and g exactly once
'''
def string_permutations():

    import itertools #import itertools for permutations() method
    # list comprehension create string with join() for every tuple element produced by itertools.permutations()
    listed = ["".join(x) for x in itertools.permutations(["c","a","t","d","o","g"])]
    
    
    print listed #print strings
    print len(listed) #check number of elements
    
    #6! is the number of possible original permutaitons of 6 elements. double-checking results
    import math 
    print math.factorial(6) 

string_permutations()