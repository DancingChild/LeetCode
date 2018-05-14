class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hash:
                return [nums_hash[target - nums[i]], i]
            nums_hash[nums[i]] = i
            """
              len_list = len(nums)
        for i in range(0, len_list):
            for j in range(1, len_list):
                sum2 = nums[i]+nums[j]
                if target == sum2:
                    return [i, j]
                else:
                    j+=1
            i += 1
            j = i+1
            """


    def test(self):
        l = [3, 2]
        r = self.twoSum(l, 5)
        print(r)

c = Solution()
c.test()

