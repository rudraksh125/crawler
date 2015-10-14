import networkx as nx

new_G = nx.read_graphml('networkx_graph.graphml')
undirected_G = new_G.to_undirected()
num_triads = nx.triangles(undirected_G)
print "triads " + str(len(list(num_triads.values())))