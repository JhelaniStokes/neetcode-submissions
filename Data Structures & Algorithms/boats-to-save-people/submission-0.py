class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = [0] * max(people)

        for p in people:
            count[p-1] += 1

        l=0
        r=len(count)-1

        res = 0
        while l <= r:
            if l+r+2 > limit:
                while l+r+2 > limit and count[r] > 0:
                    res += 1
                    count[r] -= 1
                r -= 1
                continue
            else:
                while count[l] > 0 and count[r] > 0:
                    res += 1
                    count[r] -= 1
                    count[l] -= 1
                if count[l] == 0:
                    l += 1
                else:
                    r -= 1
        
        return res



        

        