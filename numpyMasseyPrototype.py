import numpy as np 

#load matrix
a = np.matrix([[0, 0, 1, 0, -1], [-1, 1, 0, 0, 0], [0, 1, 0, 0, -1], \
    [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [1, 0, 0, 0, -1], \
    [1, 0, -1, 0, 0], [0, 1, 0, -1, 0], [0, 0, 0, 1, -1], \
    [0, -1, 1, 0, 0]])
print("\n a")
print(a)

#load right side matrix
y = np.matrix([32, 8, 25, 49, 14, 7, 10, 2, 42, 7])

#calculate a transpose
at = np.transpose(a)
print("\n aT")
print(at)

#calculate a^t * a
at_a = at.dot(a)
print("\n aT * a")
print(at_a)

#reset last row according to the write-up
at_a[len(at_a)-1:,] = 1
print("\n SET LAST ROW IN aT*a")
print(at_a)

#calculate a^t * y
at_y = np.squeeze(np.asarray(at)).dot(np.squeeze(np.asarray(y)))
print("\n aT * y")
print(at_y)

#reset last entry according to the write-up
at_y[len(at_y)-1] = 0
print("\n SET LAST ROW IN aT*y")
print(at_y)

#solve the system of equations
results = np.linalg.solve(at_a, at_y)
print("\n RESULTS")
print(results)

#print(y)
