# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
import random

def find_eulerian_tour(graph):
    # your code here
    nodes = []
    first, last = pop_randomly(graph)
    nodes.append(first)
    nodes.append(last)
    while len(graph) > 0:
        x, y = pop_randomly(graph)
        if x == last:
            nodes.append(y)
            last = y
        elif y == last:
            nodes.append(x)
            last = x
        elif x == first:
            nodes.insert(0, y)
            first = y
        elif y == first:
            nodes.insert(0, x)
            first = x
        else:
            graph.append((x,y))
    return nodes

def pick_randomly(nodes):
    i = random.randrange(0, len(nodes))
    return nodes[i]

def pop_randomly(nodes):
    i = random.randrange(0, len(nodes))
    return nodes.pop(i)

def test():
    tour = [(1, 2), (2, 3), (3, 1)]
    tour = [(1, 4), (2, 3), (2, 1), (3, 4)]
    tour = [(1, 5), (2, 1), (5, 4), (3, 4), (2, 5)]
    return find_eulerian_tour(tour)



