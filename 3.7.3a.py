def xor(a,b):
	sum = ""
	for i in range(0,len(a)):
		if int(a[i]) != int(b[i]):
			sum += "1"
		else:
			sum += "0"
	return sum

s = range(0,8)

for j in range(0,len(s)):
	s[j] = raw_input('input:')

p = s[0]	
for k in range(1,8):
	p = xor(p,s[k])

print p