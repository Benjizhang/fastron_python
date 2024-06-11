# import pyximport
# pyximport.install()
from distutils.sysconfig import get_python_lib
print(get_python_lib())

import numpy as np
from fastronWrapper.fastronWrapper import PyFastron

# # Initialize PyFastron
# fastron = PyFastron(data) # where data.shape = (N, d)

# fastron.y = y # where y.shape = (N,)

# fastron.g = 10
# fastron.maxUpdates = 10000
# fastron.maxSupportPoints = 1500
# fastron.beta = 100

# # Train model
# fastron.updateModel()

# # Predict values for a test set
# pred = fastron.eval(data_test) # where data_test.shape = (N_test, d) 

