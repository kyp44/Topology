from numpy import *
N = 10

h = {1: 1, 2: 2}
for n in range(3,N+1) :
    h[n] = sqrt(h[n-1] + h[n-2]**2)

print(h)

for n in range(2,N) :
    print(n, h[n], h[n+1]**2 - h[n-1]**2)

print()

"""
f = h
f[3] = -f[3]

for n in range(2,N) :
    print(n, f[n], f[n+1]**2 - f[n-1]**2)
"""

f = {1: 1, 2: 2}
for n in range(3,N+1) :
    v = sqrt(f[n-1] + f[n-2]**2)
    f[n] = -v if n == 3 else v

for n in range(2,N) :
    print(n, f[n], f[n+1]**2 - f[n-1]**2)

print()
print(h[3], sqrt(3))
print(h[4], sqrt(sqrt(3)+4))
