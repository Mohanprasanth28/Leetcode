class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = defaultdict(int)
        i = 0
        count = 0
        for j in range(len(s)):
            dic[s[j]] +=1
            
            while len(dic) == 3:
                count += (len(s) - j)
            
                dic[s[i]] -=1
                if dic[s[i]] == 0:
                    del dic[s[i]]

                i +=1
        return count 

            