class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map each number & their frequency
        map = {}
        for n in nums:
            if n not in map:
                map[n] = 0
            map[n] += 1

        # create a bucket to store frequency of each number as index
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, i in map.items():
            bucket[i].append(n)

        # iterate bucket backwards, if value in bucket, add to new list, stop when list has 'k' no. of elements
        group = []
        for i in range(len(bucket) - 1, -1, -1):
            if not bucket[i]:
                continue
            else:
                group += bucket[i]
                if len(group) == k:
                    break
                else:
                    continue
        return group
        
    # time comp = O(n), loops through input, hashmap, & bucket once, time taken depends on input size
    # space comp = O(n), memory used to store values in map & bucket grows based on input size