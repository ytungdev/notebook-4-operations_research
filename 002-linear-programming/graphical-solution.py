import matplotlib.pyplot as plt
import numpy as np


# plot the feasible region
d = np.linspace(0,10,500)
x,y = np.meshgrid(d,d)
plt.imshow( ((x<=4) & (2*y<=12) & (3*x+2*y<=18) & (x>=0) & (y>=0)).astype(int) , 
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3);


# plot the lines defining the constraints
x = np.linspace(0,10,500)
# eq1 : x <= 4
plt.axvline(x=4, label=r'$x\leq 4$', color="r")
# eq2 : 2y <= 12
plt.axhline(y=6, label=r'$2y\leq 12$', color="y")
# eq3 : 3x+2y <= 18
y3 = (-3*x)/2.0 +9.0

# Make plot
plt.plot(x, y3, label=r'$3x+2y\leq 18$')
plt.plot(x, y3, label=r'$3x+2y\leq 18$')
plt.xlim(0,16)
plt.ylim(0,11)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')


plt.show()
