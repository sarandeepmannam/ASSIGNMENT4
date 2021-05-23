
import matplotlib.pyplot as plt
import numpy as np
import math 
def F(x):
  return math.sqrt(1/math.sqrt(2*math.pi))*math.exp(-pow(x-1,2)/2)
X=np.linspace(-3,5,100000)
Y=[F(x) for x in X]
plt.plot(X,Y)
plt.xlabel('$x$')
plt.ylabel('$f_X(x)$')
plt.title('PDF')
plt.show