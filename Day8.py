class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<3: return True
        if coordinates[0][0] != coordinates[1][0]:
            a = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
            b = (coordinates[1][0]*coordinates[0][1]-coordinates[0][0]*coordinates[1][1])/(coordinates[1][0]-coordinates[0][0])
        else:
            for i in range(2,len(coordinates)):
                if coordinates[i][1] != coordinates[0][0]:
                    return False
            return True
        for i in range(2,len(coordinates)):
            if coordinates[i][1] != a*coordinates[i][0] + b:
                return False
        return True