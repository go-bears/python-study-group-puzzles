#problem statement: there are n lightswitches (100 or 1000?), and the 1st person turns on all the 
#lights, the 2nd person turns off every 2nd light, the third person turns off every 4th light etc 
#until the 100th person.
#how many lights are still on? which numbered lights are still on?

def lightswitches(n):

	#person 1 turns on all the lightswtiches
	lights_on = range(1, 101)
	
	#create variable for persons 2 thru 100, turning off lights (-1)
	people = range(1, 101)

	lights_off = []

	for n in lights_on: #loops through lights_on list
		for p in people: #loops though persons 2-100
			if n % 2 == 0:
				lights_off.append(-1)  #appends -1
			if n % 3 == 0:
				lights_off.append(-1)  #appends -1
			if n % 5 == 0:
				lights_off.append(-1)  #appends -1
			if n % 7 == 0:
				lights_off.append(-1)  #appends -1
			if n % 11 == 0:
				lights_off.append(-1)  #appends -1
			if n % 13 == 0:
				lights_off.append(-1)  #appends -1

			if n % (p*p) == 0:
				lights_off.append(-1)

			else:
				lights_off.append(n)



	print lights_off


lightswitches(100)
