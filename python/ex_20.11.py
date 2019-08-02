from pylab import *

f = lambda x : x / (1+x)
fp = lambda x : 1 / (1+x)**2

xs = linspace(0, 5, 500)

plot(xs, f(xs), label="f")
plot(xs, fp(xs), label="f'")
legend()
show()
