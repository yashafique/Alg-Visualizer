class Node:
    """Represents a single point (vertex) in the graph."""
    def __init__(self, node_id, x, y):
        self.id = node_id
        self.x = x
        self.y = y
        self.neighbors = []  # List of Edge objects

    """ Changes hexadecimal mem. to readable output"""
    def __repr__(self):
        return f"Node({self.id})"

class Edge:
    """Represents a weighted connection between two nodes."""
    def __init__(self, start_node, end_node, weight=1):
        self.start = start_node
        self.end = end_node
        self.weight = weight

    def __repr__(self):
        return f"Edge({self.start.id} -> {self.end.id}, w={self.weight})"
        # formatting for an output that provides "start" -> "end", w = "weight"

class Graph:
    """The data structure that manages all nodes and edges."""
    def __init__(self):
        # Dictionary mapping ID to Node object for O(1) access
        self.nodes = {} 

    def add_node(self, node_id, x, y):
        """Adds a node if it doesn't already exist."""
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id, x, y)

    def add_edge(self, u_id, v_id, weight=1, bidirectional=True):
        """Connects two nodes by their IDs."""
        if u_id in self.nodes and v_id in self.nodes:
            u = self.nodes[u_id]
            v = self.nodes[v_id]
            
            # Create forward edge
            u.neighbors.append(Edge(u, v, weight))
            
            # Create reverse edge if undirected
            if bidirectional:
                v.neighbors.append(Edge(v, u, weight))

    def get_nodes(self):
        """Returns all node objects currently in the graph."""
        return self.nodes.values()