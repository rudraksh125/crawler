import snap
import matplotlib.pyplot as plt
import numpy as np

file_graph = snap.TFIn("../test.graph")
graph = snap.TNGraph.Load(file_graph)

num_nodes = graph.GetNodes()
local_cluster_coefficient = 0

for i in range(1, num_nodes):
    # Returns clustering coefficient of a particular node
    local_cluster_coefficient += snap.GetNodeClustCf(graph, i)
print "Local clustering coefficient = %f" % (local_cluster_coefficient * 1.0 / num_nodes)

triangle_count = 0
triad_count = 0
triad_vector = snap.TIntTrV()

# Computes the number of open and closed triads for every node in Graph
snap.GetTriads(graph, triad_vector)

for triple in triad_vector:
    triangle_count += triple.Val2()
    triad_count += triple.Val2() + triple.Val3()

print "Global clustering coefficient = %f" % (triangle_count * 1.0 / triad_count)

degree_vector = snap.TIntPrV()
snap.GetDegCnt(graph, degree_vector)
node_count = []
degree = []
for item in degree_vector:
    node_count.append(item.GetVal2())
    degree.append(item.GetVal1())

plt.plot(degree, node_count, 'bo')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Number of nodes')
plt.xlabel('Degrees')
plt.suptitle("Crawled network degree distribution")
plt.grid()
plt.show()

avg_path_len = 0
n = num_nodes * (num_nodes - 1)
n_pairs = 20000
a1 = np.random.random_integers(0, num_nodes - 1, n_pairs)
a2 = np.random.random_integers(0, num_nodes - 1, n_pairs)
for i in range(n_pairs):
    avg_path_len += snap.GetShortPath(graph, a1[i], a2[i])

print 'Average path length = %f' % (avg_path_len * 1.0 / n_pairs)
