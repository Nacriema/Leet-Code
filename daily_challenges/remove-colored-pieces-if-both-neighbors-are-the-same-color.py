"""
    Problem Statement:
        There are n pieces arranged in a line, and each pieces is colored by 'A' or 'B'. You are given a string colors of 
        length n where colors[i] is the color of the ith piece.
        
        Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice
        moves first.
        
            * Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to 
            remove pieces that are colored 'B'.
        
            * Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to 
            remove pieces that are colored 'A'.
        
            * Alice and Bob can not remove pieces from the edge of the line.
        
            * If a player cannot make a move on their turn, that player loses and the other player wins.
        
        Assuming Alice and Bob play optimally, return True if Alice wins or return False if Bob wins.
        
    
    Example 1:
        Input: colors = "AAABABB"
        Output: true
        Explanation:
        AAABABB -> AABABB
        Alice moves first.
        She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.

        Now it's Bob's turn.
        Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
        Thus, Alice wins, so return true.
        
        
    Example 2:
        Input: colors = "AA"
        Output: false
        Explanation:
        Alice has her turn first.
        There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
        Thus, Bob wins, so return false.

    Example 3: 
        Input: colors = "ABBBBBBBAAA"
        Output: false
        Explanation:
        ABBBBBBBAAA -> ABBBBBBBAA
        Alice moves first.
        Her only option is to remove the second to last 'A' from the right.

        ABBBBBBBAA -> ABBBBBBAA
        Next is Bob's turn.
        He has many options for which 'B' piece to remove. He can pick any.

        On Alice's second turn, she has no more pieces that she can remove.
        Thus, Bob wins, so return false.
        
    Constraints:
        * 1 <= colors.length <= 10^5
        * colors consists of only letters 'A' and 'B'
"""
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Count the number of A or B in more than Triplet ('AAA' -> 1 or 'BBBB' -> 2)
        # Example: 
        # "AAABABB" -> "A": 1, "B": 0 
        # "AA" -> "A": 0, "B": 0
        # "ABBBBBBBAAA" -> "A": 1, "B": 5
        num_A = 0
        num_B = 0
        prev_char = None
        n_consecutive = 1
        for i in range(len(colors)):
            char = colors[i]
            if prev_char is None or char != prev_char:
                print(f'Consercutive value: {n_consecutive}')
                n_consecutive -= 2
                if n_consecutive > 0:
                    if prev_char == 'A':
                        num_A += n_consecutive
                    else:
                        num_B += n_consecutive
                n_consecutive = 1
            else:
                n_consecutive += 1
            prev_char = char
            
        # Process for the last
        n_consecutive -= 2
        if n_consecutive > 0:
            if prev_char == 'A':
                num_A += n_consecutive
            else:
                num_B += n_consecutive
                
        # We have the number of A and B
        if num_A == 0: 
            return False
        return num_A - num_B > 0
    
    
if __name__ == '__main__':
    s =Solution()
    print(s.winnerOfGame(colors="AAABABB"))
    # print(s.winnerOfGame(colors="AA"))
    # print(s.winnerOfGame(colors="ABBBBBBBAAA"))