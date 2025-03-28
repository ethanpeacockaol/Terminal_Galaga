import numpy as np
import os
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

X = np.zeros(rows, columns)
print(X)
