class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter as counter
        group = {}

        for s in strs:
            key = tuple(sorted(s))

            if key not in group:
                group[key] = []

            group[key].append(s)
        return list(group.values())


            



        