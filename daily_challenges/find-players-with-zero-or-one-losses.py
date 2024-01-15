""" 
    Problem statement:
        You are given an integer array matches where matches[i] = [winner_i, loser_i] 
        indicates that the player winner_i defeated player loser_i in a match.
        Return a list answer of size 2 where:
            * answer[0] is a list of all players that have not lost any matches.
            * answer[1] is a list of all players that have lost exactly one match.
        
        The values in the two lists should be returned in increasing order.

        Note:
            * You should only consider the players that have played at least one match.
            * The testcases will be generated such that no two matches will have the same outcome.
        
        Example 1:
            Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
            Output: [[1,2,10],[4,5,7,8]]
            Explanation:
                Players 1, 2, and 10 have not lost any matches.
                Players 4, 5, 7, and 8 each have lost one match.
                Players 3, 6, and 9 each have lost two matches.
                Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

        Example 2:
            Input: matches = [[2,3],[1,3],[5,4],[6,4]]
            Output: [[1,2,5,6],[]]
            Explanation:
                Players 1, 2, 5, and 6 have not lost any matches.
                Players 3 and 4 each have lost two matches.
                Thus, answer[0] = [1,2,5,6] and answer[1] = [].

        Constraints:
            * 1 <= matches.length <= 10^5
            * matches[i].length == 2
            * 1 <= winneri, loseri <= 10^5
            * winner_i != loser_i
            * All matches[i] are unique.
"""
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_dict = dict()  # type: dict
        teams = dict() # type: dict
        for (win, lose) in matches:
            loose_time = lost_dict.get(lose, 0) + 1
            lost_dict[lose] = loose_time
            
            if win not in teams.keys():
                teams[win] = True
            if lose not in teams.keys():
                teams[lose] = True
        part1 = sorted(list(set(teams.keys()).difference(set(lost_dict.keys()))))
        part2 = sorted([k for (k, v) in lost_dict.items() if v == 1])
        return [part1, part2]


if __name__ == '__main__':
    s = Solution()
    print(s.findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
    print(s.findWinners(matches = [[2,3],[1,3],[5,4],[6,4]]))
