class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        for m in strs:
            # create a list of 26 '0' values, to simulate character frequency
            count = [0] * 26
            
            # count character frequency in each word
            for n in m:
                i = ord(n) - ord('a')
                count[i] += 1

            # if current word matches a tuple in the hash table, append it as a vlue of the tuple key
            tp = tuple(count)
            if tp not in map:
                map[tp] = []
            map[tp].append(m)
        return list(map.values())

        # time comp = O(m * n), 'm' is the number of strings, 'n' is the length of each string
        # space comp = O(m), memory usage grows based on array size at worst case