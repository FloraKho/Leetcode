class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(g, i, target):
            if target == 0:
                ans.append(g)
            elif target < candidates[i]:
                return
            for j in range(i, n):
                backtrack(g + [candidates[j]], j, target - candidates[j])
                
        ans = []
        
        n = len(candidates)
        candidates.sort()
        backtrack([], 0, target)
        return ans
    
    