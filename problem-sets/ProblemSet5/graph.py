# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

class WeightedEdge(Edge):
    """
    A weighted edge for use in weighted directed graph
    """
    def __init__(self, src, dest, distTotal, distOut):
        Edge.__init__(self, src, dest)
        self.distTotal = float(distTotal)
        self.distOut = float(distOut)
        
    def getTotalDistance(self):
        return self.distTotal
        
    def getOutdoorDistance(self):
        return self.distOut
        
    def __str__(self):
        return '%s->%s (%d, %d)' % \
            (self.src, self.dest, self.distTotal, self.distOut)

class WeightedDigraph(Digraph):
    """
    A weighted directed graph
    """
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        distTotal = edge.getTotalDistance()
        distOut = edge.getOutdoorDistance()
        
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
            
        self.edges[src].append([dest, (distTotal, distOut)])
        
    def childrenOf(self, node):
        return [x[0] for x in self.edges[node]]
        
    def getEdge(self, src, dest):
        for node, dist in self.edges[src]:
            if node == dest:
                return dist
        
    def __str__(self):
        res = ''
        for k in self.edges:
            for d, (x, y) in self.edges[k]:
                res += '%s->%s (%.1f, %.1f)\n' % \
                    (k, d, x, y)
        return res[:-1]
    