class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        max_total = 0
        for num in nums:
            if num == 1:
                total+=1
                max_total = max(max_total, total)
            else:
                total=0
        return max_total