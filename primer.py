"""
 takes an integer value and returns True if k is even, and  False otherwise.  However, your function
cannot use the multiplication, modulo, or division operators
"""

def is_Even(k):
    """ converts integer to binary and checks if last 
    element is "0" == True and "1" == False"""
    k = bin(k)
    for item in k:
        if k[-1] == "0":
            return True
        if k[-1] =="1":
            return False
        
# print is_Even(11)
# print is_Even(12)
# print is_Even(1)
# print is_Even(2)
# print is_Even(4)
# print is_Even(7)
# print is_Even(8)

"""takes two integer values and returns True if
n  is a multiple of m ,thatis, n=mi for some integer i
,and False otherwise """

def is_Multiple(n, m):
    if n % m ==0:
        return True
    else:
        return False

# print is_Multiple(36, 2)
# print is_Multiple(3, 5)
# print is_Multiple(21, 7)


"""
takes a sequence  of one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two.  Do not use the built-in functions min or max
in implementing your solution
"""
data1 = [2, 3, 15, 100, 1, 50]
data2 = [1]
data3 = [7, 9, 3, 0, -2]

def minmax(data):
    min_num = data[0]
    max_num = data[-1]
    
    for i in data[1:]: 
        if i < min_num: 
            min_num = i
        else:
            if i > max_num:
                max_num = i
                
                
    return min_num, max_num

# print minmax(data1)
# print minmax(data2)
# print minmax(data3)
        
"""
Write a function that takes a positive integer n and returns  
the sum of the squares of all the positive integers smaller than n
"""
def squares(i):
    i_list = range(i)
    squares_list = []
    for i in i_list:
        s = i * i
        squares_list.append(s)
    return sum(squares_list)
    
# print squares(4)
# print squares(1)
# print squares(10)

"""calculate sum of squares of integers i < n in one line using built-in function & list comprehension """
squares2 = sum( [i**2 for i in range(10)])
 
# print squares2

"""
Python  allows  negative  integers  to  be  used  as  indices 
into  a  sequence, such as a string. If string s has length n
and expression s[k] is used for index -n<= k<0, what is the equivalent 
index j>= 0 such that s[j] references the same element?
"""

string = "string"
index = range(len(string)) #create indices with range drawn from length of string
backwards_index=(range(-1*(len(string)), 0)) # create indices range that starts from negative of length of string & counts up to -1

for i in index:
    print string[i]

for j in backwards_index:
    print string[j]

"""
What  parameters  should  be  sent  to  the
range constructor,  to  produce  a
range with values 50, 60, 70, 80?
"""
#range(starting #, ending#, interval between integers in range
print range(50, 90, 10)

"""
What  parameters  should  be  sent  to  the
range constructor,  to  produce  a
range with values 8, 6, 4, 2, 0,
-2, -4,-6,-8?
"""
#range(starting #, ending#, interval between integers in range
print range(8, -9, -2)


"""
Demonstrate how to use Python's list comprehension syntax to produce the list
[1, 2, 4, 8, 16, 32, 64, 128, 256].
"""
#sooo, hacky-y!!

doubles = [int(i*2) for i in [.5, 1, 2, 4, 8, 32, 64, 128 ] ]
print doubles


"""
Python's random module includes a function choice(data) that returns a random  element  from  a  non-empty  sequence.   
The random module  includes a more basic function randrange , with parameterization similar to
the built-in range function, that return  a random  choice  from  the given range.  Using only the
randrange function, implement your own version of the choice function.
(in other words, use the random.randrange() function, which creates a range & selects a number at the same time)
"""

def random_range():
    import random
    x = random.randrange(1, 150, 3)
    return x
    
print random_range()
    