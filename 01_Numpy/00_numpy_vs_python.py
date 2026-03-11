import numpy as np
import time

size = 10_000_000
py_list = list(range(size))
start = time.time()
sq_list = [i**2 for i in py_list]
end = time.time()
print(f"Execution time for list is: {end - start} seconds")

np_arr = np.array(py_list)
start = time.time()
sq_arr = np_arr **2
end = time.time()
print(f"Execution time for list is: {end - start} seconds")