class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {};
        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i], 0) + 1;
        
        for key, value in seen.items():
            if(value > 1):
                return True;
        
        return False;
