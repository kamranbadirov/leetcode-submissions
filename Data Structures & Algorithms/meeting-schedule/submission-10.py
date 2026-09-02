"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key=lambda i:i.start)
        for i in range(1, len(intervals)):
            # print(intervals[i].start, intervals[i].end, intervals[i-1].start, intervals[i-1].end)
            print(f"{intervals[i].start} < {intervals[i-1].end} = {intervals[i].start < intervals[i-1].end}")
            if intervals[i].start < intervals[i-1].end:
                return False
        return True


