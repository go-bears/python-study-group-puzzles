"""
Write  a  pseudo-code  description  of  a  function  that  reverses  a  list  of n integers,  
so  that  the  numbers  are  listed  in  the  opposite  order  than  they were before, 
and compare this method to an equivalent Python function for doing the same thing
"""

xy = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
xy.reverse() #python function to reverse lists
new_list = xy #store reversed list into new variable

yx = [] 
reverse_index = range(-1, -1*(len(xy)+1), -1)
#last element is new_list[-1], set range to (-1, -11, and increment list by -1)

for i in reverse_index:
    yx.append(new_list[i])

#print yx
        


"""
Demonstrate how to use Python's list comprehension  syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
"""

index = range(10) #set a range that matches len() of original list
evens_increment = range(0, 20, 2) #set increments that of the original list
print evens_increment

neo_list = [] #set a new empty list
x = 0   #set global scope x to inital value
while len(neo_list) < len(index):  #while loop to add elements for new list for length of index list
    for num in index:    #run for loop to move up through index
        x =  x + evens_increment[num]    #set local scope variable to add previous x value to evens_increment value as it moves through indices 
        neo_list.append(x)  #add new values of x to new list.
print neo_list

#not happy with this solution
list_2 = [i for increment in [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] for i in range(0, 91) if i == increment]
print list_2 

#this one doesn't work
list3 = [x     for x in range(0, 91)  for num in evens_increment if x==x+num and x%2==0]
print list3

 

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

#string_permutations()