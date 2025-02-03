class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            if self.hasEvenDigits(num):
                count += 1
        return count