class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
    
            if n in counts:
                counts[n] = counts[n] + 1
            else:
                counts[n] = 1
        srt= sorted(counts, key=counts.get, reverse=True)
        return srt[:k]