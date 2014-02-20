print "Welcome to tower of honai by Nishchal"
print "How many discs would you like to play with?(3-10)"
choice=input();
if choice<3 or choice>10:
	print "invalid choice, try again"
	exit()
a=list()
b=list()
c=list()
a=range(1,choice+1)
while c!=range(1,choice+1):
	print "Current condition:"
	print "a",a
	print "b",b
	print "c",c
	print "enter source (a,b,c)"
	source=raw_input();
	if source=='a':
		element=a.pop()
	if source=='b':
		element=b.pop()
	if source=='c':
		element=c.pop()
	print "Enter destination"
	destination=raw_input()
	if destination=='a':
		if len(a)==0:
			a.append(element)
		elif element<a[-1]:
			print "invalid move"
			#push back
			if source=='a':
				a.append(element)
			if source=='b':
				b.append(element)
			if source=='c':
				c.append(element)
		else:
			a.append(element)
	if destination=='b':
		if len(b)==0:
			b.append(element)
		elif element<b[-1]:
			print "invalid move"
			#push back
			if source=='a':
				a.append(element)
			if source=='b':
				b.append(element)
			if source=='c':
				c.append(element)

		else:
			b.append(element)
	if destination=='c':
		if len(c)==0:
				c.append(element)
		elif element<c[-1]:
			print "invalid move"
			if source=='a':
				a.append(element)
			if source=='b':
				b.append(element)
			if source=='c':
				c.append(element)
		else:
			c.append(element)
print "Current condition:"
print "a",a
print "b",b
print "c",c
print "you won!!!"
