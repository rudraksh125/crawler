import networkx as nx
import matplotlib.pyplot as plt
import pylab as py
import snap as snp

def readEdgeListFromFile():
    lines = [line.rstrip('\n') for line in
         open('P1_Deliverables/2_anonymized_edgeList.txt')]
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

def in_degree_sequences(G):
    degree_sequence=sorted(G.in_degree().values(),reverse=True) # degree sequence
    print "In Degree sequence"
    seen = set()
    for i in degree_sequence:
        if i not in seen:
            seen.add(i)
    in_dict = {}
    for i in sorted(seen, reverse=True):
        #print str(i) + " : " + str(degree_sequence.count(i))
        in_dict.update({str(i):str(degree_sequence.count(i))})

    size = len(seen)
    print("unique in-degrees in graph: " + str(size))
    return in_dict

def out_degree_sequences(G):
    degree_sequence=sorted(G.out_degree().values(),reverse=True) # degree sequence
    print "Out Degree sequence"
    seen = set()
    for i in degree_sequence:
        if i not in seen:
            seen.add(i)
    out_dict = {}
    for i in sorted(seen, reverse=True):
        #print str(i) + " : " + str(degree_sequence.count(i))
        out_dict.update({str(i):str(degree_sequence.count(i))})

    size = len(seen)
    print("unique out-degrees in graph: " + str(size))
    return out_dict

def difference_list(nodes, bfsnodes):
    difference = list(set(nodes) - set(bfsnodes))
    print str(len(difference))

def find_duplicate_nodes(lines, nodes):
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

def add_edges_to_graph(G, lines):
    for x in lines:
         y = x.strip().split(",")
         G.add_edge(y[0], y[1])
    return G

def find_missing_edge(edgelist1, edgelist2):
    seen = set()
    missing = set()
    for line in edgelist1:
        e1 = str(line[0])
        e2 = str(line[1])
        e=e1+e2
        seen.add(e)
    for line in edgelist2:
        e1 = str(line[0])
        e2 = str(line[1])
        e = e1+e2
        if e not in seen:
            missing.add(e)
    print "missing edge size: " + str(len(missing))
    for line in missing:
        print missing

def find_missing_edge_file(lines, edgeList):
    seen = set()
    missing = set()
    for line in edgeList:
        e1 = str(line[0])
        e2 = str(line[1])
        e=e1+e2
        seen.add(e)
    for line in lines:
        line1 = line.replace(',','')
        if line1 not in seen:
            missing.add(line)
    print "missing edge size: " + str(len(missing))
    for line in missing:
        print missing


def plot_in_degree_histogram(G):
    n = len(G.nodes())
    # make a list of each node's degree
    degree_list = list(G.in_degree().values())

    # compute and print average node degree
    print ("Avg. Node Degree: %f" %
     (float(sum(degree_list))/n))

    # generate a list degree distribution
    degree_hist = in_degree_sequences(G)

     # generate x,y values for degree dist. scatterplot
    x_list = []
    y_list = []
    # print the degree and number of nodes that have that degree
    for degree,number_of_nodes in degree_hist.iteritems():
       print ("%s : %s" % (degree,number_of_nodes))
       if number_of_nodes > 0:
        x_list.append(degree)
        y_list.append(number_of_nodes)

    # label the graph
    plt.title('In Degree Distribution')
    plt.xlabel('In Degree')
    plt.ylabel('Frequency')

    # plot degree distribution
    plt.scatter(x_list,y_list)
    plt.show()

def plot_out_degree_histogram(G):
    n = len(G.nodes())
    dict_nodes_out = G.out_degree()
    print "nodes with out degree 0"
    for n,d in dict_nodes_out.iteritems():
        if d ==0:
            print ("%s : %s" % (n,d))
    # make a list of each node's degree
    degree_list = list(G.out_degree().values())

    # compute and print average node degree
    print ("Avg. out Node Degree: %f" %
     (float(sum(degree_list))/n))

   # generate a list degree distribution
    degree_hist = out_degree_sequences(G)

     # generate x,y values for degree dist. scatterplot
    x_list = []
    y_list = []
    # print the degree and number of nodes that have that degree
    for degree,number_of_nodes in degree_hist.iteritems():
       print ("%s : %s" % (degree,number_of_nodes))
       if number_of_nodes > 0:
        x_list.append(degree)
        y_list.append(number_of_nodes)

    # label the graph
    plt.title('Out Degree Distribution')
    plt.xlabel('Out Degree')
    plt.ylabel('Frequency')

    # plot degree distribution
    plt.scatter(x_list,y_list)
    plt.show()

#main

# lines = readEdgeListFromFile()
# print "number of lines from file: " + str(len(lines))
# G = createGraphFromEdgeList(lines)
# nodes = G.nodes()
# edges = G.edges()
# print "num of nodes from parsing edgeList: " + str(len(nodes))
# print "num of edges from parsing edgeList: " + str(len(edges))
# print "duplicate nodes: "
# find_duplicate_nodes(lines, nodes)



# G= nx.DiGraph()
# lines = readEdgeListFromFile()
# new_G=add_edges_to_graph(G, lines)
# print "num of nodes from adding each edge: " + str(new_G.number_of_nodes())
# print "num of nodes from adding each edge: " + str(new_G.number_of_edges())
# nx.write_graphml(new_G,'networkx_graph.graphml')

#plot_in_degree_histogram(new_G)
#plot_out_degree_histogram(new_G)

new_G = nx.read_graphml('networkx_graph.graphml')
undirected_G = new_G.to_undirected()
# num_triads = nx.triangles(undirected_G)
# print "triads " + str(len(list(num_triads.values())))

count_connected_components = 0
for edge in undirected_G.edges():
    undirected_G.remove_edge(edge[0],edge[1])
    if nx.is_connected(undirected_G) == True:
        count_connected_components+=1
    undirected_G.add_edge(edge[0],edge[1])
print "number of bridges: " + count_connected_components
#print "missing edges: "
# find_missing_edge(new_edges, edges)
#find_missing_edge_file(lines, new_edges)




#degree_histogram = nx.degree_histogram(G)
#print "degree histogram: "
#print_list(degree_histogram)
#dict = print_degree_sequences(G)
#print_dictionary(dict)
#print_degree_sequences(G)

#convert to gigraph
# directed_G = nx.DiGraph(G)
# nodes = directed_G.nodes()
# edges = directed_G.edges()
# print "num of nodes from parsing edgeList: " + str(len(nodes))
# print "num of edges from parsing edgeList: " + str(len(edges))

#print_in_degree_sequences(directed_G)

#degreeCentrality = degree_centrality(G)
#eigenVectorCentrality = eigenvector_centrality(G)
#pageRankCentrality = pagerank_centrality(G)
#print_centralities(directed_G, nodes,degreeCentrality,eigenVectorCentrality,pageRankCentrality)
#three_cycles(directed_G)




