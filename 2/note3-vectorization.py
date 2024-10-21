import numpy as np

a = [i for i in range(5)]
b = [i for i in range(5,10)]
c = [i for i in range(10,15)]

a = np.array(a)
b = np.array(b)
c = np.array(c)

c += a + b
