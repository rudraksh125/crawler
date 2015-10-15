import snap
import matplotlib.pyplot as plt
import numpy as np
import sys

FIn = snap.TFIn("../test.graph")
graph = snap.TNGraph.Load(FIn)

num_nodes = graph.GetNodes()

c = 1.898  # Average degree.
Cp = 0.067
C0 = 0.75
b= 1-(Cp/C0)**0.3333

small_world_graph = snap.GenSmallWorld(num_nodes,int(c),b)
FOut = snap.TFOut('small_world.graph')
small_world_graph.Save(FOut)

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

DegToCntV = snap.TIntPrV()
snap.GetDegCnt(small_world_graph, DegToCntV)
node_count = []
degree = []
for item in DegToCntV:
	node_count.append(item.GetVal2())
	degree.append(item.GetVal1())

# plt.plot(degree,node_count,'b-')
# plt.yscale('log')
# plt.xscale('log')
# plt.ylabel('Number of nodes')
# plt.xlabel('Degrees')
# plt.suptitle("Small-World model degree distribution")
# plt.grid()
# plt.show()

avg_path_len = 0
n = num_nodes*(num_nodes-1)
num_pairs = 20000
p1 = np.random.random_integers(0,num_nodes-1,num_pairs)
p2 = np.random.random_integers(0,num_nodes-1,num_pairs)
for i in range(num_pairs):
	avg_path_len += snap.GetShortPath(small_world_graph, p1[i], p2[i], True)

print 'Average path length = %f' %(avg_path_len*1.0/num_pairs)
