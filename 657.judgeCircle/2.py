class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')
        
# 此方法虽然只写了一行，而且时间复杂度是O(N)，但是代码在运行的时候应该会遍历moves4次，
# 以计算上下左右的数量，这使得算法的时间复杂度常数较大。