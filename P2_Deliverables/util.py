import snap

def readEdgeListFromFile():
    lines = [line.rstrip('\n') for line in
         open('P1_Deliverables/2_anonymized_edgeList.txt')]
    return lines

def add_nodes_edges_to_graph(G, lines):
    seen = set()

    for line in lines:
        line = line.split(',')
        seen.add(line[0])
        seen.add(line[1])

    for s in seen:
        G.AddNode(int(s))

    for line in lines:
        line = line.split(',')
        G.AddEdge(int(line[0]),int(line[1]))
    return G

def save_graph_to_file(G):
    file_graph = snap.TFOut('test.graph')
    G.Save(file_graph)
    file_graph.Flush()

#main

lines = readEdgeListFromFile()
G = snap.TNGraph.New()
G = add_nodes_edges_to_graph(G,lines)
save_graph_to_file(G)

#TIntTrV, a vector of (integer, integer, integer) triplets;
triad_vector = snap.TIntTrV()
snap.GetTriads(G,triad_vector)
count = 0
for i in triad_vector:
    count+=i.Val1()
print "count: " + str(count/3)