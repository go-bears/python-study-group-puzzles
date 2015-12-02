"""
Brick Wall exercise:

Functions are used to isolate different small specific tasks.
Functions abstract action, grouping several actions as a single object, and then you group those actions to create more  bigger and more advanced objects. 
to 

Goal: I've given you "starter functions" of  that create different size bricks.
use the individual brick functions to create rows of bricks to build a "strong" wall. You have to design your "row" functions so that the seams do not meet. (there's a sample below)

Finally, create a small_wall() function that automatically builds the brick wall so it matches the sample output below. Note the seams of the bricks should not line up to make the strongest wall

print small_wall() is the trigger to build the entire wall, all the functions return outputs until the last function call.


Take it further: 
make a medium_wall() function and a large_wall() function, making sure to use all the brick sizes. 


learning goals: abstraction, chaining functions, return vs. print statements, calling functions, passing values through function parameters and arguments, calling elements from a list, global & local scope

"""
import time
from itertools import permutations, combinations
import random

bricks = [ "[]", "[__]", "[____]", "[______]" ]


def row1(brick3, mortar): 
    mortar = bricks[0]  #sample code, you should replace it
    brick3 = bricks[2]  #sample code, you can replace it
    row1 = (mortar + brick3 + mortar)  #sample code, you can replace it
    return row1
    
    
def row2(brick2,brick1):
    brick2 = bricks[2]
    brick1 = bricks[1]
    row2 = brick2 + brick1
    return row2

def row3(brick1,mortar):
    #do something
    brick1 = bricks[1]
    mortar = bricks[0]
    row3 = (brick1 * 2) + mortar
    return row3

def row4(brick3,mortar):
    #do something
    brick3 = bricks[3]
    mortar = bricks[0]
    row4 = mortar + brick3 
    return row4

def row5(brick3, mortar):
     #do something
    brick3 = bricks[3]
    mortar = bricks[0]
    row5 =  brick3 + mortar
    return row5



def small_wall():
    print row1(bricks[3], bricks[0])
    time.sleep(1)
    print row2(bricks[2], bricks[1])
    time.sleep(1)
    #call row function with relevant argument(s)
    print row3(bricks[1],bricks[0])
    time.sleep(1)
    #call row function with relevant argument(s)
    print row4(bricks[3],bricks[0])
    time.sleep(1)
    #call row function with relevant argument(s)
    print row5(bricks[3], bricks[0])

    
small_wall()


#automate brick wall with for loop & shuffle
def big_wall(bricks):
    for item in range(6):
        random.shuffle(bricks)
        print "".join(bricks)
        


big_wall(bricks)
    

"""
sample output of a wall. Note how the seams between the bricks meet at in the middle of another brick.

[__][__][]
[][__][__]
[__][__][]
[][__][__]
[__][__][]

"""