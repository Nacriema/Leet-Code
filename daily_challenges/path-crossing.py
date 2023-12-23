""" 
    Problem statement:
        Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
        You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

        Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. 
        Return false otherwise.

        Example 1: 
            Input: path = "NES"
            Output: false 
            Explanation: Notice that the path doesn't cross any point more than once. 

        Example 2;
            Input: path = "NESWW"
            Output: true
            Explanation: Notice that the path visits the origin twice.

        Constraints:
            * 1 <= path.length <= 10^4
            * path[i] is either 'N', 'S', 'E', or 'W'.

        Hints:
            * Simulate the process while keeping track of visited points.
            * Use a set to store previously visited points.
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction_mapping = {'N': (0, 1),
                     'S': (0, -1),
                     'E': (1, 0),
                     'W': (-1, 0)}
        visited_point = set([(0, 0)])
        last_visit = [0, 0]
        for direction in path:
            last_visit[0] += direction_mapping[direction][0]
            last_visit[1] += direction_mapping[direction][1]
            if tuple(last_visit) not in visited_point:
                visited_point.add(tuple(last_visit))
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPathCrossing(path="NES"))
    print(s.isPathCrossing(path="NESWW"))
