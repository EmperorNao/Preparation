

class Solution:

    def rec_fill(self, im, i, j, old, new):

        print(i, j)
        if not(0 <= i < len(im) and 0 <= j < len(im[0])) or self.visited[i][j]:
            return

        self.visited[i][j] = 1
        if im[i][j] == old:

            self.rec_fill(im, i + 1, j, old, new)
            self.rec_fill(im, i, j + 1, old, new)
            self.rec_fill(im, i - 1, j, old, new)
            self.rec_fill(im, i, j - 1, old, new)

            im[i][j] = new


    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        self.visited = [[0 for i in range(len(image[0]))] for j in range(len(image))]
        self.rec_fill(image, sr, sc, image[sr][sc], newColor)
        return image
