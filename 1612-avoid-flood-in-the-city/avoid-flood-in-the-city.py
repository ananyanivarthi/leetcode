import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n                # default: -1 on rainy days
        lastRain = {}                 # lake -> last day it rained
        dryDays = []                  # sorted list of dry day indices
        
        for i, lake in enumerate(rains):
            if lake > 0:  # rainy day
                # if this lake is already full
                if lake in lastRain:
                    # find earliest dry day after it was last filled
                    idx = bisect.bisect_right(dryDays, lastRain[lake])
                    if idx == len(dryDays):
                        return []  # no dry day available -> flood
                    dry_day = dryDays.pop(idx)
                    ans[dry_day] = lake  # use that dry day to dry this lake
                # mark current day as last rain day for this lake
                lastRain[lake] = i
                ans[i] = -1
            else:
                # no rain today -> we can dry any lake later if needed
                bisect.insort(dryDays, i)
                ans[i] = 1  # default, will be replaced if used to dry a lake
                
        return ans
