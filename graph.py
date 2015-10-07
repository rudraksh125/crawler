import networkx as nx

g = nx.DiGraph()

lines = [line.rstrip('\n') for line in
         open('/Users/kvivekanandan/Desktop/ASU/CSE_598_Social_Media_Mining/Project/1_Submission/crawler/edgeList.txt')]

G = nx.parse_edgelist(lines, delimiter=',', nodetype=int)
nodes = G.nodes()
edges = G.edges()
print "nodes from parsing edgeList: " + str(len(nodes))
# print G.edges()

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






