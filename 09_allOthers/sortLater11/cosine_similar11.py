## calculate cosine similarity
## to find distance between two documents

import numpy as np

A = np.array([1, 3])
B = np.array([-2, 2])

dot_prod = np.dot(A, B)                 # Compute dot product
print("dot prod ==> ", dot_prod)        # Print dot product