import numpy as np

import os

os.system('cls')

"""
    array of 0
"""
a = np.zeros(5)
print(f"zeros(5): {a}\n")

"""
    replace - where()
"""
b = np.array([4, 5, 6])
print(f"where(array a > 0, 1, 0): {np.where(a > 0, 1, 0)}")
print(f"where(array b > 0, 1, 0): {np.where(b > 0, 1, 0)}\n")

"""
    multiplay dot()
    vector * scalar
"""
x = 5
a = np.array([1, 2, 3])
res = np.dot(a, x)
print(f"vector: {a}")
print(f"dot(1D_array, 5): {res}\n")

"""
    vector * vector
    1 * 4 + 2 * 5 + 3 * 6
"""
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
a = np.zeros(3)
b = np.array([1, 0, 0])
print(f"vector: {a}; vector {b}")
print(f"dot(vector, vector): {np.dot(a, b)}\n")

"""
    insert
"""
res = np.insert(b, 0, 8)
print(f"vector: {b}")
print(f"insert(vector, pos = 0, val = 8): {res}\n")

