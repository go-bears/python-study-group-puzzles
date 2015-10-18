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
        
print is_Even(11)
print is_Even(12)
print is_Even(1)
print is_Even(2)
print is_Even(4)
print is_Even(7)
print is_Even(8)