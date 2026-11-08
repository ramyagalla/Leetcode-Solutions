class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        count = 0
        seen = []

        for num in nums:
            if num != 0 and num not in seen:
                seen.append(num)
                count += 1

        return count
