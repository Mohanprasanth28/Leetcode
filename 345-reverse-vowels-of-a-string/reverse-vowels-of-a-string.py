class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = []
        for ch in s:
            arr.append(ch)
        a = ['A','E','I','O','U','a','e','i','o','u']
        i  = 0
        j = len(arr)-1
        while i < j:
            if arr[i] not in a:
                i +=1
            elif arr[j] not in a:
                j -=1
            elif arr[i] in a and arr[j] in a:
                arr[i],arr[j] = arr[j],arr[i]
                i +=1
                j -=1
        st = ""
        for c in arr:
            st += c
        return st

            


        