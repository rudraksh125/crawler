import networkx as nx
import snap

"""takes forever!!
new_G = nx.read_graphml('networkx_graph.graphml')
G = new_G.to_undirected()
print "diameter of the graph :" + str(nx.diameter(G))
"""

G = snap.TNGraph.Load(snap.TFIn("../test.graph"))
test_nodes = 500

diameter = snap.GetBfsFullDiam(G,test_nodes,True)
print "Diameter of the network= %f" % (diameter)