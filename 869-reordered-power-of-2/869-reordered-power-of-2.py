class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return Counter(str(n)) in [Counter(str(1 << i)) for i in range(30)]