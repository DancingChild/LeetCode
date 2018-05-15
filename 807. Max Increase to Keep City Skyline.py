class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        import time

        np_grid = np.array(grid)
        tb_max = np.max(np_grid , axis=0)
        lr_max = np.max(np_grid , axis=1)
        w,h = np_grid.shape
        sum = 0
        for i in range(w):
            for j in range(h):
                sum += min(lr_max[i], tb_max[j]) - grid[i][j]

    def test(self):
        grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
        self.maxIncreaseKeepingSkyline(grid)
s = Solution()
s.test()