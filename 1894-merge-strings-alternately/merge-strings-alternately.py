class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        word = ""
        
        while i<len(word1) and j <len(word2):
            if i <= j:
                word += word1[i]
                i +=1
            else:
                word += word2[j]
                j +=1
        while i <len(word1):
            word += word1[i]
            i +=1
        while j <len(word2):
            word += word2[j]
            j +=1
        return word
            
        