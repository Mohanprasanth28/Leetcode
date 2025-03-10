class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            vowel = defaultdict(int)
            count = 0
            total = 0
            i = 0

            for j in range(len(word)):
                if word[j] in "aeiou":
                    vowel[word[j]] +=1 
                else:
                    count +=1
                while len(vowel) == 5 and count >= k:
                    total += (len(word) - j)
                    if word[i] in "aeiou":
                        vowel[word[i]] -= 1
                    else:
                        count -=1
                    if vowel[word[i]] == 0:
                            del vowel[word[i]]
                    
                    i += 1
            return total 
        return atleastk(k) - atleastk(k + 1)