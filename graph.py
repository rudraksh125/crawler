import networkx as nx
import matplotlib.pyplot as plt
import pylab as py

def readEdgeListFromFile():
    lines = [line.rstrip('\n') for line in
         open('/Users/kvivekanandan/Desktop/ASU/CSE_598_Social_Media_Mining/Project/1_Submission/crawler/edgeList.txt')]
    return lines

def createGraphFromEdgeList(lines):
    G = nx.parse_edgelist(lines, delimiter=',', nodetype=int)
    return G

def print_dictionary(dict):
    for k,v in dict.iteritems():
        print(str(k)+ " " + str(v))

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

def print_degree_sequences(G):
    degree_sequence=sorted(nx.degree(G).values(),reverse=True) # degree sequence
    #print "Degree sequence", degree_sequence
    seen = set()
    for i in degree_sequence:
        if i not in seen:
            seen.add(i)

    for i in sorted(seen, reverse=False):
        print str(i) + " : " + str(degree_sequence.count(i))
        dict.update({str(i):str(degree_sequence.count(i))})

    size = len(seen)
    print("unique degrees in graph: " + str(size))
    return dict

def print_in_degree_sequences(G):
    degree_sequence=sorted(G.in_degree().values(),reverse=True) # degree sequence
    print "In Degree sequence"
    seen = set()
    for i in degree_sequence:
        if i not in seen:
            seen.add(i)

    for i in sorted(seen, reverse=True):
        print str(i) + " : " + str(degree_sequence.count(i))

    size = len(seen)
    print("unique in degrees in graph: " + str(size))

def difference_list(nodes, bfsnodes):
    difference = list(set(nodes) - set(bfsnodes))
    print str(len(difference))

def find_duplicate_nodes():
    seen = set()
    uniq = []
    for x in lines:
        y = x.strip().split(",")
        for e1 in y:
            if e1 not in seen:
                uniq.append(e1)
                seen.add(e1)
    print "unique nodes: " + str(len(uniq))
    difference_list(uniq, nodes)

def print_centralities(G, nodes, dc, eigc, pgc):
    print "{:<15} {:<8} {:<20} {:<20} {:<20}".format('Node','In-degree','Degree Centrality','EigenVector Centrality', 'PageRank Centrality')
    for node in nodes:
        print "{:<15} {:<8} {:<20} {:<20} {:<20}".format(str(node),str(G.in_degree(node)),str(dc[node]),str(eigc[node]),str(pgc[node]))

def three_cycles(G):
    cycles = nx.simple_cycles(G)
    for c in cycles:
        if len(c)==3:
            print c
    return cycles

def calculate_largest_connected_component():
    pass

def print_list(list):
    n =0
    for i in list:
        print ((str(n)) + " " + str(i))
        n = n + 1

#main

lines = readEdgeListFromFile()
G = createGraphFromEdgeList(lines)
nodes = G.nodes()
edges = G.edges()
print "num of nodes from parsing edgeList: " + str(len(nodes))
print "num of edges from parsing edgeList: " + str(len(edges))

degree_histogram = nx.degree_histogram(G)
print "degree histogram: "
print_list(degree_histogram)
dict = print_degree_sequences(G)
print_dictionary(dict)
#print_degree_sequences(G)
#convert to gigraph
directed_G = nx.convert.convert_to_directed(G)
#print_in_degree_sequences(directed_G)

#degreeCentrality = degree_centrality(G)
#eigenVectorCentrality = eigenvector_centrality(G)
#pageRankCentrality = pagerank_centrality(G)
#print_centralities(directed_G, nodes,degreeCentrality,eigenVectorCentrality,pageRankCentrality)
#three_cycles(directed_G)

#visualize graph
#nx.draw_spring(directed_G, node_size=0,edge_color='b',alpha=0.2,font_size=10,with_labels=True)


# d = nx.degree(G)
# plt.hist(d.values())
# plt.show()

# plt.loglog(degree_sequence,'b-',marker='o')
# plt.title("Degree plot")
# plt.ylabel("degree")
# plt.xlabel("rank")
# plt.show()




