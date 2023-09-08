"""
    Problem Statement:
        Given an integer numRows, return the first numRows of Pascal's triangle.
        In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    
    Example 1:
        Input: numRows = 5
        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    Example 2:
        Input: numRows = 1
        Output: [[1]]
        
    Constrains:
        * 1 <= numRows <= 30
"""
class Solution:
    def generate(self, numRows: int):
        """
            My implementation here
            This is the optimal solution
        """
        ans = [[1], [1, 1]]
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return ans
        
        for _ in range(2, numRows):
            pas = [1, 1]
            insert_idx = 1
            for j in range(0, len(ans[-1]) - 1):
                sum_pair = ans[-1][j] + ans[-1][j+1]
                pas.insert(insert_idx, sum_pair)
                insert_idx += 1
            ans.append(pas)
        return ans
    

if __name__ == '__main__':
    s = Solution()
    print(s.generate(numRows=5))
    print(s.generate(numRows=1))
    