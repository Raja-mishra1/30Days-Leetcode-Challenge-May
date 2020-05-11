class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oriCol = image[sr][sc]
        if oriCol == newColor: return image
        row, col, surs = len(image), len(image[0]), [(sr, sc)]
        while surs:
            for i, j in surs: image[i][j] = newColor
            surs = [(x, y) for i, j in surs for x, y in 
                     [(i+1, j), (i-1, j), (i, j-1), (i, j+1)] 
                     if 0<=x<row and 0<=y<col 
                     and image[x][y] == oriCol]
        return image
