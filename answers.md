
# CMPS 2200 Recitation 08 Answers

**Name:** Shiqian Zhang

### 2) Work of reachable

The work of reachable is O(n + m), where n is the number of nodes and m is the number of edges.

Each node is added to the frontier at most once because we use a set to track visited nodes.

Each node is processed once, and each edge is examined at most twice in an undirected graph.

Therefore, the total work is O(n + m).

### 4) Number of Calls to reachable

We only need to call reachable once to determine whether a nonempty undirected graph is connected.

Starting from any node, we find all nodes reachable from it.

If the number of reachable nodes equals the total number of nodes, the graph is connected. Otherwise, it is disconnected.

Therefore, the worst-case number of calls is 1.

### 5) Work of connected

The connected function calls reachable only once.

Since reachable takes O(n + m) work, and checking the size of the visited set takes O(1) time, the total work is:

O(n + m)

Therefore, connected has linear work in the number of nodes and edges.

### 7) Adjacency Matrix Representation

Yes, the work of reachable would change if we used an adjacency matrix.

With the map-of-neighbors representation, we only examine the actual neighbors of each node, resulting in O(n + m) work.

With an adjacency matrix, we must examine an entire row of n entries to identify the neighbors of a node.

In the worst case, we visit all n nodes, and each node requires checking n entries.

Therefore, the total work becomes:

O(n^2)

This is less efficient for sparse graphs, where the number of edges is much smaller than n^2.
