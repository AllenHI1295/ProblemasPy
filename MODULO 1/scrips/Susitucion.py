import string
import numpy as np
num2alpha=dict(zip(range(1,27), string.ascii_lowercase))
x=np.array([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]])
z=x.flatten()
print(z)
w=z.tolist()
print(w)
for i in w:
    print(num2alpha[i])