from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for x, c in count.items():
            buckets[c].append(x)

        result = []
        for c in range(len(nums), 0, -1):
            for x in buckets[c]:
                result.append(x)
                if len(result) == k:
                    return result