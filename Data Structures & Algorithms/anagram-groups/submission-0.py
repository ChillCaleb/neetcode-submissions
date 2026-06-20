class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of anagrams
        for s in strs:
            count = [0] * 26 #a-z
            for c in s:
                count[ord(c)-ord('a')] +=1 #counting each character
            res[tuple(count)].append(s) # group all anagrams in the count together
        return list(res.values()) # returning grouped anagrams


        