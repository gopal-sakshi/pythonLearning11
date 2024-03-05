import scipy.linalg
import numpy as np

def blas(name, ndarray):
    arr = scipy.linalg.get_blas_funcs((name,), (ndarray,), dtype=ndarray.dtype)[0]
    return arr

blas_scal = blas('scal', np.array([], dtype=np.int32))
print ("int32 --> %s" % (blas_scal))

blas_scal = blas('scal', np.array([], dtype=np.int64))
print ("int64 --> %s" % (blas_scal.dtype))

blas_scal = blas('scal', np.array([], dtype=np.float32))
print ("float32 --> %s" % (blas_scal.dtype))

blas_scal = blas('scal', np.array([], dtype=np.float64))
print ("float64 --> %s" % (blas_scal.dtype))