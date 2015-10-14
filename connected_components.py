import random
import networkx as nx
import matplotlib.pyplot as plt

new_G = nx.read_graphml('networkx_graph.graphml')
G = new_G.to_undirected()

#generate x% for edge removal
x = random.randint(1,100)
edges = G.edges()
num_edges = len(edges)
num_iterations = int (float(x * 0.01 )* num_edges)
sample_edges = random.sample(range(1, num_edges), num_iterations)

for e in sample_edges:
    G.remove_edge(edges[e][0],edges[e][1])

largest_component = sorted(nx.connected_components(G), key = len, reverse=True)[0]
print "size of largest component after removing " + str(x) + "% of edges : " + str(len(largest_component))

for e in sample_edges:
    G.add_edge(edges[e][0],edges[e][1])


print "progressing from x = 1 to 100"
component_lengths = []
for x in range(1,100):
    num_iterations = int (float(x * 0.01 ) * num_edges)
    sample_edges = random.sample(range(1, num_edges), num_iterations)
    for e in sample_edges:
        G.remove_edge(edges[e][0],edges[e][1])

    largest_component = sorted(nx.connected_components(G), key = len, reverse=True)[0]
    print "size of largest component after removing " + str(x) + "% of edges : " + str(len(largest_component))
    component_lengths.append(len(largest_component))

    for e in sample_edges:
        G.add_edge(edges[e][0],edges[e][1])

component_lengths.append(0)
progress = []
progress.extend(range(1, 100))
progress.append(100)
plt.plot(progress, component_lengths, 'bo')
plt.xlabel('% edges removed')
plt.ylabel('size of largest component')
plt.show()