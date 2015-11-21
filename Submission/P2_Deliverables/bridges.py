import networkx as nx

new_G = nx.read_graphml('../networkx_graph.graphml')
undirected_G = new_G.to_undirected()

count_connected_components = 0
for edge in undirected_G.edges():
    undirected_G.remove_edge(edge[0],edge[1])
    if nx.is_connected(undirected_G):
        count_connected_components+=1
    undirected_G.add_edge(edge[0],edge[1])
print "number of bridges: " + count_connected_components