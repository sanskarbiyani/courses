d = {'a':10, 'b':1, 'c':22}
t= sorted(d.items())# sorted gives us a sorted list of tuples
print(t)
for k,v in sorted(d.items()):#sort by key
    print(k,v)

#sorting ny value
p = list()
for k,v in d.items():
    p.append((v,k))
print(p)

p = sorted(p,reverse=True)
print(p)
