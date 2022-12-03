class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        partial_result = []
        
        def findPath(node):
            if node == len(graph) - 1:
                result.append(partial_result.copy())
                return
            
            for i in graph[node]:
                partial_result.append(i)
                findPath(i)
                partial_result.pop()
                
        partial_result.append(0)
        findPath(0)
            
        return result