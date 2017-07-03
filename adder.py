def xor(a,b):
	sum = ""
	for i in range(0,len(a)):
		if int(a[i]) != int(b[i]):
			sum += "1"
		else:
			sum += "0"
	return sum

# x = raw_input('First word: ')
# y = raw_input('Second word: ')
# print xor(x,y)

exit = 'n'
while(exit == 'n'):
	#exit = raw_input('Exit? (y/n): ')
	if exit == 'n':
		x = raw_input('First word: ')
		y = raw_input('Second word: ')
		print xor(x,y)
