import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (x+2*y-7)**2 + (2*x+y-5)**2


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with a colormap ranging from red to blue
surf = ax.plot_surface(X, Y, Z, cmap='jet')
surf.set_clim(np.min(Z), np.max(Z))
fig.colorbar(surf)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()