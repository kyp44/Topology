from pylab import *
import numpy as np

xs = ys = linspace(-2, 2, 500)

(xsd, ysd) = meshgrid(xs, ys)

dsd = abs(xsd - ysd)

levels = np.linspace(np.min(dsd), np.max(dsd), 200)
    
cf = contourf(xsd, ysd, dsd, levels=levels)
colorbar(cf)
show()
