class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        count = defaultdict(int)
        n = len(grid)

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] +=1
        rep , miss = 0,0
        for num in range(1,n*n+1):
            if count[num] == 0:
                miss = num
            if count[num] == 2:
                rep = num
        return [rep,miss]
            

        