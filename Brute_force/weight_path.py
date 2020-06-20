# This is a function which takes a graph and a list of vertices in a Hamiltonian cycle, and returns the weight of this cycle.
import networkx as nx

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

# Example Graph
g = nx.Graph()
g.add_edge(0, 1, weight = 2)
g.add_edge(1, 2, weight = 2)
g.add_edge(2, 3, weight = 2)
g.add_edge(3, 0, weight = 2)
g.add_edge(0, 2, weight = 1)
g.add_edge(1, 3, weight = 1)

# Now we want to compute the lengths of two cycles:
cycle1 = [0, 1, 2, 3]
cycle2 = [0, 2, 1, 3]


print(cycle_length(g,cycle1))
print(cycle_length(g,cycle2))
