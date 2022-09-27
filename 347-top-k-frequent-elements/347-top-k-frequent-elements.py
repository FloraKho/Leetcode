from collections import Counter
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		count = collections.Counter(nums)
		return heapq.nlargest(k,count.keys(),key = count.get)