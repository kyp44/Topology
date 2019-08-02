from pylab import *

f = lambda x : x / (1 + x)

xs = linspace(0,10, 500)
plot(xs, f(xs))
show()
