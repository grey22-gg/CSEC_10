n = int(input())
o = 1
l = []
for i in range(n):
	c = input()
	l.append(c)
for i in range(len(l)-1):
    if l[i] != l[i+1]:
    	o += 1
print(o)
