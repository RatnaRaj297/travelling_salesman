import networkx as nx
from itertools import permutations
import sys

def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()

    weight = 0
    for i in range(len(cycle)):
      u = cycle[i]
      if cycle[i] == cycle[-1]:
        v = cycle[0]
      else:
        v = cycle[i+1]

      weight = weight + g[u][v]['weight']

    return weight


# finds the shortest path. Checks all the possible weights and returns the minimum one.

def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    min_weight = sys.maxsize

    # Iterate through all permutations of n vertices
    for p in permutations(range(n)):
        w = cycle_length(g,p)
        if w<min_weight:
            min_weight = w

    return min_weight


# returns the average weight of the cycle 

def average(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    sum_of_weights = sum(g[i][j]['weight'] for i in range(n) for j in range(i))

    return (sum_of_weights*2)/(n-1)
