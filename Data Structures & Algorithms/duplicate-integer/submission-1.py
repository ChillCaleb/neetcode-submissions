class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums) 

# set automatically removes duplicates from the nums list 
#if the number is not greater than the number being compared, it s removed



         