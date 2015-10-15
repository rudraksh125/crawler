import snap
import matplotlib.pyplot as plt
import numpy as np

FIn = snap.TFIn("../test.graph")
graph = snap.TNGraph.Load(FIn)

num_nodes = graph.GetNodes()
num_edges = graph.GetEdges()
c = 2

pref_attach_graph = snap.GenPrefAttach(num_nodes,c)
file_pa = snap.TFOut('preferential_attachment.graph')
pref_attach_graph.Save(file_pa)

local_cf = 0
for i in range(0, num_nodes):
	local_cf += snap.GetNodeClustCf(pref_attach_graph, i)
print "Local clustering coefficient = %f" % (local_cf*1.0/num_nodes)

triangle_count = 0
triad_count = 0
TriadV = snap.TIntTrV()
snap.GetTriads(pref_attach_graph, TriadV)
for triple in TriadV:
    triangle_count += triple.Val2()
    triad_count += triple.Val2()+triple.Val3()

print "Global clustering coefficient = %f" % (triangle_count*1.0/triad_count)

DegToCntV = snap.TIntPrV()
snap.GetDegCnt(pref_attach_graph, DegToCntV)
node_count = []
degree = []
for item in DegToCntV:
	node_count.append(item.GetVal2())
	degree.append(item.GetVal1())

plt.plot(degree,node_count,'bo')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Number of nodes')
plt.xlabel('Degrees')
plt.suptitle("Preferential attachment model")
plt.grid()
plt.show()

avg_path_len = 0
n = num_nodes*(num_nodes-1)
num_pairs = 2000
p1 = np.random.random_integers(0,num_nodes-1,num_pairs)
p2 = np.random.random_integers(0,num_nodes-1,num_pairs)
for i in range(num_pairs):
	avg_path_len += snap.GetShortPath(pref_attach_graph, p1[i], p2[i])

print 'Average path length = %f' %(avg_path_len*1.0/num_pairs)