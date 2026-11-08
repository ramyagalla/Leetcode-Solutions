Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def canBeIncreasing(self, nums: list[int]) -> bool:
...         count=0
...         for i in range(len(nums)-1):
...             if nums[i]>=nums[i+1]:
...                 count+=1
...                 if count>1:
...                     return False
...                 if i>0 and nums[i-1]>=nums[i+1]:
...                     nums[i+1]=nums[i]
...         return True
...                 
... 
