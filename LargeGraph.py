import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from numpy import set_printoptions
set_printoptions(precision=3, threshold=5, edgeitems=4, suppress=True)

'''

Here we first define some parameters:

'''
N_Triangle = 7
TriNodes = [[3 * i , 3 * i + 1, 3 * i + 2] for i in range(7)]
center = N_Triangle * 3 + 1

A = np.eye(center ) * 0
D = np.eye(center ) * 0

for trin in TriNodes:
    edges.append([TriNodes[0], TriNodes[1])
    edges.append([TriNodes[1], TriNodes[2])
    edges.append([TriNodes[0], TriNodes[2])
    edges.append([TriNodes[0], center )
    D[TriNodes[0]][TriNodes[0]] = 3
L = D - A



for edge in edges:
    n1, n2 = edge[0], edge[1]
    A[n1][n2] = 1
    A[n2][n1] = 1
G = nx.from_numpy_matrix(A)
subax1 = plt.subplot(121)
nx.draw(G)   # default spring_layout
