class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def findway(now=0):
            if graph[now]:
                for i in graph[now]:
                    if i == len(graph) - 1:
                        path.append(i)
                        paths.append(path.copy())
                        for j in range(len(path)-1):
                            path.pop()
                    else:
                        path.append(i)
                        findway(i)
        path = [0]
        paths = [ ]
        findway()
        print(paths)
        return paths
        # N = len(graph)
        # def solve(node):
        #     if node == N-1:
        #         return [[N-1]]
        #     ans = []
        #     for nei in graph[node]:
        #         for path in solve(nei):
        #             ans.append([node] + path)
        #     print(ans)
        #     return ans
        # return solve(0)

    def test(self):
        grid =[[1,2], [3], [3], []]
        self.allPathsSourceTarget(grid)

s = Solution()
s.test()