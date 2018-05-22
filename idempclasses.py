"""
Subject: Classes calculator for given 'n'
Author: Arjan Gupta
Created on: 4/16/2016
"""

#def classes(n):
	#something

def r_calc(n):
	if(n == 1):
		return 1
	else:
		r = 2
		while((2**r)%n != 1):
			r = r + 1
		else:
			return r


n = 2
while(n%2 == 0):
	n = raw_input('What is n? (Odd input needed): ')
	n = int(n)

print r_calc(n)

