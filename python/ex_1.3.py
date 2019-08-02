from pylab import *

xs = linspace(-4, 4, 500)
ys = xs**2 - xs

plot(xs, ys)
grid()
savefig("part_a.png")
