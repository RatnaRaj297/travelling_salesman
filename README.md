# Travelling Salesman
Applied various algorithms to solve the Travelling Salesman Problem

### Exact Algorithms

<li>**Brute Force**: This is the most Naive and inefficient algorithm to solve the TSP. Time complexity is n!
**Branch and Bound**: Always produces the optimal result but the time taken varies on the given problem
**Dynamic Programmin**: The run time is a bit better. Time complexity is of the order (2^n)*(n^2)

### Approximate Algorithms

<li>**Nearest Neighbour** : This algorithm works fine for a Euclidian TSP but does not provide good results for a general graph. For a Eculedian TSP, it is apporximate log n times worse than the optimal result
**2-approximate** : Takes linear time to compute a sub-optimal solution. The sub-optimal solution's weight is less than 2 times the optimum solution's weight<li>
