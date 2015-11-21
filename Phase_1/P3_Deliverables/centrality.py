import networkx as nx
import pandas as pd



def degree_centrality(G):
    #degree_centrality
    dictionary_centrality = nx.in_degree_centrality(directed_G)
    return dictionary_centrality

def eigenvector_centrality(G):
    #eigenvector_centrality
    dictionary_centrality = nx.eigenvector_centrality_numpy(directed_G)
    return dictionary_centrality

def pagerank_centrality(G):
    #pagerank
    dictionary_centrality = nx.pagerank(directed_G)
    return dictionary_centrality

def print_centralities(G, nodes, dc, eigc, pgc):
    print "{:<15} {:<8} {:<20} {:<20} {:<20}".format('Node','In-degree','Degree Centrality','EigenVector Centrality', 'PageRank Centrality')
    for node in nodes:
        print "{:<15} {:<8} {:<20} {:<20} {:<20}".format(str(node),str(G.in_degree(node)),str(dc[node]),str(eigc[node]),str(pgc[node]))

#main
directed_G = nx.read_graphml('../networkx_graph.graphml')
degreeCentrality = degree_centrality(directed_G)
eigenVectorCentrality = eigenvector_centrality(directed_G)
pageRankCentrality = pagerank_centrality(directed_G)

df = pd.DataFrame({'dc':degreeCentrality})
df.to_csv('dc.csv', index = False)

df = pd.DataFrame({'eig':eigenVectorCentrality})
df.to_csv('eig.csv', index=False)

df = pd.DataFrame({'pr':pageRankCentrality})
df.to_csv('pr.csv', index=False)

s_dc = sorted(degreeCentrality,key= degreeCentrality.get, reverse=True)
e_vc = sorted(eigenVectorCentrality,key= eigenVectorCentrality.get, reverse=True)
p_rc = sorted(pageRankCentrality,key= pageRankCentrality.get, reverse=True)

for i in s_dc[1:11]:
    print "node: " + str(i) + " degree centrality: " +  str(degreeCentrality[i])

for i in e_vc[1:11]:
    print "node: " + str(i) + " eigen vector centrality: " +  str(eigenVectorCentrality[i])

for i in p_rc[1:11]:
    print "node: " + str(i) + " page rank centrality: " +  str(pageRankCentrality[i])