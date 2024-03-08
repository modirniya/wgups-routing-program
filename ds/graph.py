from ds.hash_map import HashMap


class Graph:
    def __init__(self):
        # Initialize an empty graph using a hash map to store nodes and edges
        self.nodes = HashMap()  # O(1)

    def __str__(self):
        # Return a string representation of the graph
        return str(self.nodes)  # O(n)

    def add_node(self, node):
        # Add a new node to the graph if it doesn't already exist
        # Time complexity: O(1)
        if self.nodes[node] is None:
            self.nodes[node] = HashMap()

    def add_edge(self, from_node, to_node, weight):
        # Add a directed edge from 'from_node' to 'to_node' with the given weight
        # Time complexity: O(1)
        if weight is not None:
            weight = float(weight)
        if self.nodes[from_node] is None:
            self.add_node(from_node)
        if self.nodes[to_node] is None:
            self.add_node(to_node)
        self.nodes[from_node][to_node] = weight

    def get_edge_weight(self, origin, destination):
        # Get the weight of the edge from 'origin' to 'destination'
        # Time complexity: O(1)
        origin_node_edges = self.nodes[origin]
        if origin_node_edges:
            return origin_node_edges[destination]
        return None
