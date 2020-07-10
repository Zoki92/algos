class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbour(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return f"{self.id} connected to: {neighbour.id for neighbour in self.connected_to}"

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):

        return self.id
    def get_weight(self, nbr):
        return self.connected_to[nbr]

class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0
    
    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
    
    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        return None
    
    def __contains__(self, n):
        return n in self.vert_list
    
    def add_edge(self, f, t, weight=0):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbour(self.vert_list[t], weight)
    
    def get_vertices(self):
        return self.vert_list.keys()
    
    def __iter__(self):
        return iter(self.vert_list.values())

"""
The getVertices method returns the names of all of the vertices in the graph. 
In addition, we have implemented the __iter__ method to make it easy to iterate 
over all the vertex objects in a particular graph.
"""