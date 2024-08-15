import queue

class Graph:
    def __init__(self, n):
        # vertices are 1, 2, 3, .., n
        self.adj_list = dict()
        self.n = n
        
        for v in range(1, n+1):
            self.adj_list[v] = []
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        return
        
    def compute_min_distance(self, U, v):
        # Computes d[v]
        present = dict()
        for u in U:
            present[u] = True
        if present.get(v) != None:
            return 0
        
        visited = [False for _ in range(self.n+1)]
        dis = float("inf")
        q = queue.Queue()
        q.put(v)
        visited[v] = True
        level = 0
        while q.empty() == False:
            vertices_count = q.qsize()
            
            # Finding next level vertices ->
            while vertices_count > 0:
                u = q.get()
                for v in self.adj_list[u]:
                    if present.get(v) != None:
                        dis = level + 1
                        return dis
                    
                    if visited[v] == False:
                        q.put(v)
                        visited[v] = True # This is missed
                
                vertices_count -= 1
            level += 1
        return dis

g = Graph(4)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 3)
g.compute_min_distance([4], 1)
