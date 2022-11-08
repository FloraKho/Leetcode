class Solution:
    def climbStairs(self, n: int) -> int:
        #check how many way we can climb to the top
        #bottom up!!!dynamic programming problem
        
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        
        return one