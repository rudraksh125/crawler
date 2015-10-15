import networkx as nx
import  matplotlib.pyplot as plt

directed_G = nx.read_graphml('../networkx_graph.graphml')
undirected_G = directed_G.to_undirected()

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

def plot_in_degree_histogram(G):
    n = len(G.nodes())
    # make a list of each node's degree
    degree_list = list(G.in_degree().values())

    # compute and print average node degree
    avg_in_degree = float((sum(degree_list)*1.0)/n)
    print ("Avg.Node In-Degree: %f" % (avg_in_degree))

    # generate a list degree distribution
    degree_hist = in_degree_sequences(G)

     # generate x,y values for degree dist. scatterplot
    x_list = []
    y_list = []
    # print the degree and number of nodes that have that degree
    for degree,number_of_nodes in degree_hist.iteritems():
       #print ("%s : %s" % (degree,number_of_nodes))
       if number_of_nodes > 0:
        x_list.append(degree)
        y_list.append(number_of_nodes)

    # plot degree distribution
    #plt.scatter(x_list,y_list)
    #plt.show()
    plt.plot(x_list,y_list,'b-')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Number of nodes')
    plt.xlabel('Degrees')
    plt.suptitle("in-degree distribution")
    plt.grid()
    plt.show()

def plot_out_degree_histogram(G):
    n = len(G.nodes())
    dict_nodes_out = G.out_degree()
    # print "nodes with out degree 0"
    # for n,d in dict_nodes_out.iteritems():
    #     if d ==0:
    #         print ("%s : %s" % (n,d))
    # make a list of each node's degree
    degree_list = list(G.out_degree().values())

    # compute and print average node degree
    avg_out_degree = float((sum(degree_list)*1.0)/n)
    print ("Avg.out Node Degree: %f" % (avg_out_degree))

    #generate a list degree distribution
    degree_hist = out_degree_sequences(G)

     # generate x,y values for degree dist. scatterplot
    x_list = []
    y_list = []
    # print the degree and number of nodes that have that degree
    for degree,number_of_nodes in degree_hist.iteritems():
       # print ("%s : %s" % (degree,number_of_nodes))
       if number_of_nodes > 0:
        x_list.append(degree)
        y_list.append(number_of_nodes)

    # plot degree distribution
    #plt.scatter(x_list,y_list)
    #plt.show()
    plt.plot(x_list,y_list,'b-')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Number of nodes')
    plt.xlabel('Degrees')
    plt.suptitle("out-degree distribution")
    plt.grid()
    plt.show()

plot_in_degree_histogram(directed_G)
plot_out_degree_histogram(directed_G)

