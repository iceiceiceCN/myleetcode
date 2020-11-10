class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dic = {"x":0,"y":0}
        for idx,val in enumerate(moves):
            if val == "U":dic["y"] +=1
            elif val == "D":dic["y"] -=1
            elif val =="L":dic["x"] +=1
            elif val == "R":dic["x"] -=1
        
        if dic["x"] == 0 and dic["y"] == 0:
            return True
        return False
