class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)] 

        count = Counter(nums)

        for num, v in count.items():
            buckets[v].append(num)
        
        res = []
        i = len(buckets)-1
        while len(res) < k:
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
            i-=1
        
        return res
