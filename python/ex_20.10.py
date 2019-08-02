from pylab import *

xn = lambda n : 3/n
yn = lambda n : 2/n
zn = lambda n : 1/n

N = 1000
ser = lambda an : sum([an(n)**2 for n in range(1,N+1)])

sn = lambda n : sum([(xn(i) - zn(i))**2 for i in range(1,n+1)])
sns = lambda n : sqrt(sn(n))

print(sqrt(sn(N)))
print(sns(N))
