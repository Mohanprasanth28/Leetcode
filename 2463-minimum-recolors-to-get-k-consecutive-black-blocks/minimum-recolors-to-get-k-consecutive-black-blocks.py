class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        min_operations = white_count = blocks[:k].count('W')

        for i in range(k, len(blocks)):

            if blocks[i - k] == 'W':
                white_count -= 1
          
            if blocks[i] == 'W':
                white_count += 1

            min_operations = min(min_operations, white_count)

        return min_operations