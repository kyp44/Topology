from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ps = np.linspace(-10, 10, 51)
(xd, yd) = np.meshgrid(ps, ps)

f = np.vectorize(lambda x, y : 0 if (x,y) == (0,0) else x*y / (x**2 + y**2))

ax.plot_wireframe(xd, yd, f(xd, yd))

plt.show()
