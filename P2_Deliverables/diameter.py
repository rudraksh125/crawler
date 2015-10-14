import networkx as nx

new_G = nx.read_graphml('networkx_graph.graphml')
G = new_G.to_undirected()
print "diameter of the graph :" + str(nx.diameter(G))