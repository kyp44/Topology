from pylab import *

bname = "ex_2_6_"
ext = ".pdf"

f = lambda x : x**3 - x

xs = linspace(1, 10, 500)
ys = f(xs)

plot(xs, ys, color="k")
xlim(xs[0], xs[-1])
grid()
xlabel("$g$")
savefig(bname + "g" + ext, bbox_inches="tight")

clf()
plot(ys, xs, color="k")
xlim(ys[0], ys[-1])
grid()
xlabel("$g^{-1}$")
savefig(bname + "gi" + ext, bbox_inches="tight")
