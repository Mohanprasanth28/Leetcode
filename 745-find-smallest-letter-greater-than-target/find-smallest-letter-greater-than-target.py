class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        for ch in letters:
            if ch != target and ord(ch) > ord(target):
                return ch
        return letters[0]
                
        