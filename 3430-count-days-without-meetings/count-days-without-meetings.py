class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        no_meeting = 0
        pre_end = 0
        meetings.sort()

        for s , e in meetings:
            if s > pre_end:
                no_meeting += s - pre_end - 1
            pre_end = max(pre_end,e)
        no_meeting += max(0, days - pre_end)

        return no_meeting