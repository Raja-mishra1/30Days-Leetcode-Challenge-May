class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph, visited = collections.defaultdict(set), {}
        for u, v in dislikes: graph[u].add(v), graph[v].add(u) # build graph
        def dfs(node, g): 
            if node in visited: return visited[node] == g 
            visited[node] = g 
            return all(dfs(nei, 1-g) for nei in graph[node]) 
        return all(dfs(node, 0) for node in range(1,N+1) if node not in visited) # DFS for all nodes
        