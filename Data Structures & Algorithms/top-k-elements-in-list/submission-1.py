class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            if n not in map:
                map[n] = 0
            map[n] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for n, i in map.items():
            bucket[i].append(n)

        group = []
        for i in range(len(bucket) - 1, -1, -1):
            if not bucket[i]:
                continue
            else:
                group += bucket[i]
                if len(group) >= k:
                    break
                else:
                    continue

        return group
        
    # time comp = O(n)
    # space comp = O(n)