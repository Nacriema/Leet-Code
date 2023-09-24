"""
    Problem Statement:
        We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and 
        so on until the 100th row. Each glass holds one cup of champagne.

        Then, some champagne is poured into the first glass at the top. When the topmost glass is full, any
        excess liquid poured will fall equally to the glass immediately to the left and right of it. When 
        those glasses be come full, any excess chanpagne will fall equally to the left and right of those 
        glasses, and so on. (A glass at the botton row has its excess champagne fall on the floor)

        For example, after one cup of champagne is poured, the topmost glass if full. After two cups of 
        champagne are poured, the two glasses on the second row are half full. After three cups of champange 
        are poured, those two cups become full - there are 3 full glasses now. After four cups of champagne are
        poured, the third row as the middle glass half full, and the two outside glasses are a quarter full.

        Now after pouring some non-negative integer cups of champagne, return how full the j_th glass in the i_th
        row is (both i and j are 0-indexed)

    Example 1:
        Input: poured = 1, query_row = 1, query_glass = 1
        Output: 0.00000
        Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)).
                    There will be no excess liquid so all the glasses under the top glass will remain empty.

    Example 2: 
        Input: poured = 2, query_row = 1, query_glass = 1
        Output: 0.50000
        Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). 
        There is one cup of excess liquid.
        The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally,
        and each will get half cup of champange.

    Example 3:
        Input: poured = 100000009, query_row = 33, query_glass = 17
        Output: 1.00000

    Constrains: 
        * 0 <= poured <= 10^9
        * 0 <= query_glass <= query_row < 100

    I've tried with the Pascal triangle idea, but this problem is not in that case.
    So sad, this problem again the DP.

"""
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
            Create and array that compute the total water flow that reached to each glass
        """
        DP = [[0] * k for k in range(1, 102)]
        DP[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r+1):
                divided = (DP[r][c] - 1.0) / 2.0
                if divided > 0:
                    DP[r+1][c] += divided
                    DP[r+1][c+1] += divided
        return min(1, DP[query_row][query_glass])


if __name__ == '__main__':
    s = Solution()
    # print(s.champagneTower(poured=1, query_row=1, query_glass=1))
    # print(s.champagneTower(poured=2, query_row=1, query_glass=1))
    # print(s.champagneTower(poured=100000009, query_row=33, query_glass=17))
    # print(s.champagneTower(poured=0, query_row=0, query_glass=0))
    print(s.champagneTower(poured=6, query_row=3, query_glass=1))