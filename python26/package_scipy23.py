from scipy import linalg
import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[5],[6]])

print(linalg.inv(A).dot(B))             # one is fast..
print(np.linalg.solve(A,B))             # other is slow... dont know which one
print("----------------------------------------------------")
#######################################################

C = np.array([[1,2],[3,4]])             ### determinant ==> axd - bxc       (1x4 - 2x3)
print('determinant of matrix A ==> ', linalg.det(A))

'''

    sub packages of SciPy
        Special functions               (scipy.special)
        Integration                     (scipy.integrate)
        Optimization                    (scipy.optimize)
        Interpolation                   (scipy.interpolate)
        Fourier Transforms              (scipy.fft)
        Signal Processing               (scipy.signal)
        Linear Algebra                  (scipy.linalg)
        Sparse Arrays                   (scipy.sparse)
        Spatial DS and algo             (scipy.spatial)
        Statistics                      (scipy.stats)
        File IO                         (scipy.io)
        Others are also there

'''


'''
    scipy.linalg vs numpy.linalg
    - scipy contains all functions of numpy + some advanced stuff not present in numpy

'''