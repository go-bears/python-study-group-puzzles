"""problem statement: there are only 3 fixed sizes of chicken nuggets. For any given amount of chicken nuggets can the 
order be filled with any combination of the box of 3, box of 6, or box of 20 chicken nuggets. return true if the order can
be filled, return false if the order cannot be filled"""

def chicken(n):

	box1 = 6
	box2 = 9
	box3 = 20

	if n < 6:
		return False

	if n % box1 == 0 or n % box2 == 0 or n % box3 == 0:
		return True

	else: 
		if chicken(n - box1):
			return True
		if chicken(n - box2):
			return True
		if chicken(n - box3):
			return True

		return False

print chicken(239)

assert chicken(236) is True
assert chicken(146) is True
assert chicken(17) is False
assert chicken(133) is True
assert chicken(45) is True
assert chicken(28) is False
assert chicken(16) is False
assert chicken(15) is T
