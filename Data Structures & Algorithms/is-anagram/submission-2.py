class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for ch in s:
            if ch in counts:
                counts[ch] = counts[ch] + 1      
            else:
                counts[ch] = 1       

        for ch in t:
            if ch not in counts or counts[ch] == 0:
                return False
            counts[ch] = counts[ch] - 1                             

        return True

        
        
        
        
