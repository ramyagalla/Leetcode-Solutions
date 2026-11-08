class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        freq={}
        for i in range(len(nums)-1):
            if nums[i]==key:
                if nums[i+1] not in freq:
                    freq[nums[i+1]]=1
                else:
                    freq[nums[i+1]]+=1
        return max(freq,key=freq.get)
