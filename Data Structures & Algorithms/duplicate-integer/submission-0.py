class Solution:

        
    def hasDuplicate(self, nums: List[int]) -> bool:
        Seen = []
        for n in nums:
            if n in Seen:
              return True
            Seen.append(n)
           
        return False
              