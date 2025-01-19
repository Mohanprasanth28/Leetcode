class Solution:
    def repeatedCharacter(self, s: str) -> str:
        array = []
        for char in s:
            if char in array:
                return char
            else:
                array.append(char)
        
        