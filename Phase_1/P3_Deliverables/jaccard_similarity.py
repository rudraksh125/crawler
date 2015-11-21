import networkx as nx

G = nx.read_graphml('networkx_graph.graphml')
undirected_G = G.to_undirected()
jaccard_similarity = nx.jaccard_coefficient(undirected_G)
sorted_js = sorted(jaccard_similarity, key=lambda tup:tup[3], reverse=True)
print "most similar nodes by jaccard similarity: " + str(sorted_js[0])
