"""
Kruskal and Prim algorithm for Minimum or Maximum Spanning Tree(MST)
"""

def __find(father, node):
    """
    Find the parent of the given node
    :param father: To update the dictionary
    :param node: The node you wish to find its parent
    :return: Parent node
    """
    if father[node] != node:
        father[node] = __find(father, father[node])
    return father[node]

def __merge(father, depth, node1, node2):
    """
    Merge the two tree depends on condition
    """
    father_x = __find(father, node1)
    father_y = __find(father, node2)
    if father_x == father_y:
        return
    if depth[father_x] < depth[father_y]:
        father[father_x] = father_y
    else:
        father[father_y] = father_x
        if depth[father_x] == depth[father_y]:
            depth[father_x] += 1
            
def Kruskal(v, e, min=True):
    """
    Kruskal algorithm for MST, set min to False for Maximum Spanning Tree
    :param v: A dictionary or a list with all the vertices in the graph
    :param e: A list of edges in the graph
    :return: The cost for MST
    """
    father = {}
    depth = {}
    mst = []
    for node in v:
        father[node] = node
        depth[node] = 0
    cost = 0
    e.sort(reverse=not min)
    """
    If the implementation of your e is not in such way [(cost, start, des)...]
    Please change the codes below here according to your implementation
    """
    for edge in e:
        if __find(father, edge[1]) != __find(father, edge[2]):
            __merge(father, depth, edge[1], edge[2])
            mst.append(edge)
            cost += edge[0]
    print(cost)
    for r in mst:
        print(r)

def Prim(v, min=True):
    """
    Prim algorithm for MST, set min to False for Maximum Spanning Tree
    :param v: A dictionary which vertex as key and edge as value i.e
              v[vertex] = [("C1", W1), ("C2, W2)...]
    :return: The cost for MST
    """
    begin = list(v)[0]
    prQ = PriorityQueue()
    visit = {}
    mst = []
    for vertex in v:
        visit[vertex] = False
    prQ.put((0, begin, begin))
    cost = 0
    """
    If the implementation of your v is not same as mine 
    Please change the codes below here according to your implementation
    """
    while not prQ.empty():
        vertex = prQ.get()
        if visit[vertex[2]]:
            continue
        visit[vertex[2]] = True
        cost += vertex[0]
        mst.append(vertex)
        for child in v[vertex[2]]:
            if not visit[child[0]]:
                prQ.put((child[1] if min else -child[1], vertex[2], child[0]))


    print(cost if min else -cost)
    for r in mst[1:]:
        print(r)
     
    return cost if min else -cost

if __name__ == '__main__':

    # "For Prim Test:"
    v = {"A":[("B", 7), ("D", 5)],
         "B":[("C", 8), ("D", 9), ("E", 7), ("A", 7)],
         "C":[("E", 5), ("B", 8)],
         "D":[("E", 15), ("F", 6), ("B", 9), ("A", 5)],
         "E":[("F", 8), ("G", 9), ("C", 5), ("B", 7), ("D", 15)],
         "F":[("G", 11), ("D", 6), ("E", 8)],
         "G":[("E", 9), ("F", 11)]}
    # "For Kruskal Test:“
    e = [
        (7, "A", "B"),
        (5, "A", "D"),
        (8, "B", "C"),
        (9, "B", "D"),
        (7, "B", "E"),
        (5, "C", "E"),
        (15, "D", "E"),
        (6, "D", "F"),
        (8, "E", "F"),
        (9, "E", "G"),
        (11, "F", "G")
    ]
    Kruskal(v, e)
    Kruskal(v, e, False)
    Prim(v)
    Prim(v, False)
