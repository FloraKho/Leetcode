class Solution:
    def dailyTemperatures(self, T):
        ans = [0]*len(T) 
        stack = []
    
        for i,v in enumerate(T):
        #check whether current val is greater than the last appended stack value.  We will pop all the elements which is lesser than the current temp
            while stack and stack[-1][1] < v:
                index,value = stack.pop()
                ans[index] = i - index # we are checking how many indices we 
            stack.append([i,v])      
        return ans
	
        