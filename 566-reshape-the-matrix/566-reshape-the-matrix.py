class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat)*len(mat[0]):
            return mat
        queue = [cell for row in mat for cell in row]
        return [[queue.pop(0) for _ in range(c)] for _ in range(r)]