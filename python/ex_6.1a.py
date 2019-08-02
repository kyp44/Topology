import itertools as it

for f in it.permutations(range(1,4+1), 3) :
    print("\\item $" + str(f) + "$")
