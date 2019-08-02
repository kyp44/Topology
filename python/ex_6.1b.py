import itertools as it

c = 0
for i,f in enumerate(it.permutations(range(1,10+1), 8)) :
    c += 1

print(c)
