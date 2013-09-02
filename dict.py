d = {}
l = []
for i in range(5):
	l.append(raw_input('input --> '))
	d[l[-1]] = d.get(l[-1],0) + 1
	
print d
