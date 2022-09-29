class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res
        