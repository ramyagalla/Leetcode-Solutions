class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        a=set(nums1)
        b=set(nums2)
        l=a.intersection(b)
        if l:
            return min(l)
        t=[]
        for i in nums1:
            m=str(i)
            for j in nums2:
                 n=str(j)
                 k=m+n
                 s=n+m
                 t.append(int(k))
                 t.append(int(s))
        return min(t)


        
