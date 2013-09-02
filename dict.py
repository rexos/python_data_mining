d = {}
l = []
for i in range(5):
    l.append(raw_input('input --> '))
    if d.has_key(l[-1]):
        d[l[-1]] += 1
    else:
        d[l[-1]] = 1

print d
