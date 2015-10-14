import snap

file_graph = snap.TFIn("test.graph")
graph = snap.TNGraph.Load(file_graph)

num_nodes = graph.GetNodes()


local_cluster_coefficient = 0
for i in range(1, num_nodes):
    #Returns clustering coefficient of a particular node
	local_cluster_coefficient += snap.GetNodeClustCf(graph, i)
print "Local clustering coefficient = %f" % (local_cluster_coefficient *1.0/num_nodes)

triangle_count = 0
triad_count = 0
triad_vector = snap.TIntTrV()

#Computes the number of open and closed triads for every node in Graph
snap.GetTriads(graph, triad_vector)

for triple in triad_vector:
    triangle_count += triple.Val2()
    triad_count += triple.Val2()+triple.Val3()

print "Global clustering coefficient = %f" % (triangle_count*1.0/triad_count)

