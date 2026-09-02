"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if len(intervals) < 2:
        #     return len(intervals)
        # intervals.sort(key = lambda i : i.start)
        # days = [[intervals[0]]]
        # for inter in intervals[1:]:
        #     for day in days:
        #         placed = False
        #         if day[-1].end <= inter.start:
        #             day.append(inter)
        #             placed = True
        #             break
        #     if not placed:
        #         days.append([inter])

        # return len(days)

        time = []
        for inter in intervals:
            time.append((inter.start, 1))
            time.append((inter.end, -1))
        
        time.sort(key=lambda x: (x[0], x[1]))
        
        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count