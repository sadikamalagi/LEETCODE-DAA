import heapq


def prims_algorithm(graph, V):
   
    in_mst = [False] * V
    

    min_heap = [(0, 0)]  

    total_weight = 0  
    mst_edges = []   

    while min_heap:
        weight, u = heapq.heappop(min_heap)  
        
      
        if in_mst[u]:
            continue
        
     
        in_mst[u] = True
        total_weight += weight
        
        
        if weight != 0:
            mst_edges.append((u, weight))

        \
        for v, w in graph[u]:
            if not in_mst[v]:
                heapq.heappush(min_heap, (w, v))

    return total_weight, mst_edges



if __name__ == "__main__":
    
    V = 5
    

    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8)],
        4: [(1, 5), (2, 7)]
    }
    
    
    total_weight, mst_edges = prims_algorithm(graph, V)
    
    print(f"Total weight of MST: {total_weight}")
    print(f"Edges in MST: {mst_edges}")
