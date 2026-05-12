## ALGORITHM OBJECTIVES AND KEY TYPES

# MAIN OBJECTIVE IN ALGORITHMS
The primary goal of most data structure algorithms is Optimization and Efficiency. 
1. Efficiency: Solving a problem in the least amount of time (Time Complexity) using the minimum amount of memory (Space Complexity).
2. Correctness: Ensuring the algorithm produces the right output for all possible valid inputs.
3. Scalability: Ensuring the algorithm remains performant as the size of the data set (n) grows.

# GRAPH ALGORITHM COMPARISON

DIJKSTRA: The "Greedy" Shortest Path
- Purpose: Finds the shortest path from a single starting node to all other nodes in a graph.
- Logic: It always picks the "closest" unvisited node to process next.
- Constraint: Only works on graphs with non-negative edge weights.

A* (A-STAR): The "Informed" Search
- Purpose: Finds the shortest path from a starting node to a specific target node.
- Logic: It uses Dijkstra's logic but adds a "Heuristic" (an educated guess of the remaining distance). This allows it to "ignore" paths that lead away from the target, making it much faster for games and GPS.

PRIM'S ALGORITHM: The "Minimum Connector"
- Purpose: Finds the Minimum Spanning Tree (MST).
- Logic: It connects all nodes in a graph together using the lowest total edge weight possible, without creating any loops (cycles). 
- Difference: While Dijkstra finds the shortest distance from a START, Prim's finds the cheapest way to connect the WHOLE network.

BELLMAN-FORD: The "Robust" Shortest Path
- Purpose: Finds the shortest path from a single source to all other nodes.
- Logic: It "relaxes" all edges multiple times to ensure the shortest path is found.
- Advantage: Unlike Dijkstra, it can handle negative edge weights and can detect "negative cycles" (loops that infinitely reduce the path cost).