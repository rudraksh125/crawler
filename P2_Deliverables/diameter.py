import networkx as nx
import snap
<<<<<<< HEAD

"""takes forever!!
=======
"""
>>>>>>> 6c28a133db4f7a4d70eaf6f87e26d11f4fbf5397
new_G = nx.read_graphml('networkx_graph.graphml')
G = new_G.to_undirected()
print "diameter of the graph :" + str(nx.diameter(G))
"""

G = snap.TNGraph.Load(snap.TFIn("../test.graph"))
test_nodes = 500

diameter = snap.GetBfsFullDiam(G,test_nodes,True)
<<<<<<< HEAD
print "Diameter of the network= %f" % (diameter)
=======
print "Diameter of the network= %f" % (diameter)

"""
OUTPUT:
Diameter of the network= 7.000000
"""
>>>>>>> 6c28a133db4f7a4d70eaf6f87e26d11f4fbf5397
