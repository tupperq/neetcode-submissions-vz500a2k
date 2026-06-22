class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
         return 0
        longest_cons = 1

        for i in range(len(nums)):
               count = 1
               while nums[i] + count in nums:
                  count += 1
               else: 
                  longest_cons = max(longest_cons, count)
        return longest_cons
               


