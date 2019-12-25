def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

flights = [("ORD", "SEA"), ("ORD", "LAX"), ('ORD', 'DFW'), ('ORD', 'PIT'),
           ('SEA', 'LAX'), ('LAX', 'DFW'), ('ATL', 'PIT'), ('ATL', 'RDU'),
           ('RDU', 'PHL'), ('PIT', 'PHL'), ('PHL', 'PVD')]

G = {}
for (x,y) in flights: make_link(G,x,y)

# Write centrality to return the avarage distance
# from a node to all the other nodes it can reach
def centrality (G, v):
    distance = {}
    openlist = [v]
    distance[v] = 0
    while len(openlist) > 0:
        current = openlist.pop(0)
        for neibor in G[current].keys():
            if neibor not in distance:
                distance[neibor] = distance[current] + 1
                openlist.append(neibor)
    return (sum(distance.values()) + 0.0)/len(distance)

print centrality(G, 'LAX')
print centrality(G, 'RDU')