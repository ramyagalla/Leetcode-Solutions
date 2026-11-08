class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        nums.sort(key=lambda x:(freq[x],-x))
        return nums
