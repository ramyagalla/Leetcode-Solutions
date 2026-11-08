class Solution:
    def trimMean(self, arr: list[int]) -> float:
        k=len(arr)//20
        arr.sort()
        arr=arr[k:len(arr)-k]
        s=0
        c=0
        for i in arr:
            s+=i
            c+=1
        t=s/c
        return t
        
