class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {i:nums[i] for i in range(len(nums))}
       # print(d)
        for i in range(len(nums)):
            del d[i]
            if target - nums[i] in d:
                return [i, d[target - nums[i]]]


t = Solution().twoSum([3,2,4], 6)
print(t)
