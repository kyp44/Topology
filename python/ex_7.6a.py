from functools import reduce

N = 500
n = 7

def sets(s) :
    st = "{"
    if len(s) > 10 :
        st += ", ".join(map(str, sorted(s)[:10])) + "...}"
    else :
        st += ", ".join(map(str, sorted(s))) + "}"
    return st

A = set(range(1,N+1))
B = set(range(5,N+1))

f = lambda k : 4+2*k
fs = lambda S : set(map(f, S))

As = {1 : A}
Bs = {1 : B}
Cs = {1 : A - B}
for i in range(2,n+1) :
    As[i] = fs(As[i-1])
    Bs[i] = fs(Bs[i-1])
    Cs[i] = As[i] - Bs[i]

ss = lambda s,i : s + "_" + str(i)
    
for i in range(1,n+1) :
    print(ss("A", i), "=", sets(As[i]))
    print(ss("B", i), "=", sets(Bs[i]))
    print(ss("C", i), "=", ss("A", i), "-", ss("B", i), "=", sets(Cs[i]))
    print()

def h(x) :
    if x in reduce(set.union, Cs.values()) :
        return f(x)
    else :
        return x

print("h:")
for x in range(1, 20+1) :
    print(x, "->", h(x))
