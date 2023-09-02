"""
    Problem Statement:

        You are given a 0-indexed string s and a dictionary of words dictionary. 
        You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. 
        There may be some extra characters in s which are not present in any of the substrings.

        Return the minimum number of extra characters left over if you break up s optimally.

        (Break the string OPTIMALLY !!!)

    Example 1:
        Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
        Output: 1
        Explanation: 
            We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. 
            There is only 1 unused character (at index 4), so we return 1.
    
    Example 2:
        Input: s = "sayhelloworld", dictionary = ["hello","world"]
        Output: 3
        Explanation: 
            We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. 
            The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
"""
# TODO: NEED TO REVISIT THIS PROBLEM, BECAUSE This is not my solution :<< 

from typing import List
import re 
from functools import reduce, lru_cache


class Solution:
    def minExtraChar_greedy(self, s: str, dictionary: List[str]) -> int:
        """
            My implementation here

            1. Use Greedy first
                - May be we need to sort the dictionary based on the length of words
                - Loop through the dictionary, find the index of the string in s

            2. Use Dynamic Programming :<

        """
        result = len(s)
        dictionary = sorted(dictionary, key=lambda x: len(x), reverse=True)
        print(f'Sorted dictionary: {dictionary}')

        # TODO: Notice about the NON-OVERLAPPING words !!!, to handle this case, just replace the string with " " instead of ""
        for word in dictionary:
            # using re.finditer() to find all occurrences of substring in string
            occurrences = re.finditer(word, s)
            # using reduce() to get start indices of all occurrences
            res = reduce(lambda x, y: x + [y.start()], occurrences, [])
            if len(res):
                print(f'Hit: {word}, Total occurences: {len(res)}')
                s = s.replace(word, " ")
                print(f'Adjusted: {s}')
                result -= len(res) * len(word)
        print(f'Last {s}')
        return result
    
    def minExtraChar_DP(self, s: str, dictionary: List[str]) -> int:
        """

            So far the greedy method does not give the optimal solution (just passed 95% cases)
            Use hints:
                Define DP[i] as the min extra character if breaking up s[0:i] optimally.
            
            TODO: Find the recurrent relation ship in this problem
            Let's call: 
                - DP[i] is the min extra character if breaking up s[0:i] optimally
            Then:
                - DP[i + 1] is the min extra character if breaking up s[0:i+1] optimally, how can I find this
                
                DP[i + 1] = DP[i] + 1 if s[i+1] inside the dict (but may be not optimally)
                
                # Check for the rest
                for end in range(i, n):
                    if 
        """
        
        # TODO: Add memo
        n, dictionary_set = len(s), set(dictionary)
        memo = dict()

        # NOTE: To achieve O(1) when lookup, convert dict to set
        print(f'Dictionary set: {dictionary_set}')
        def dp(i):
            print(f'Memo: {memo}')
            if i == n:
                return 0
            if i in memo:
                return memo[i]
            
            ans = dp(i+1) + 1
            for end in range(i, n):
                curr = s[i: end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
            memo[i] = ans
            return ans
        
        return dp(0)

if __name__ == '__main__':
    s = Solution()
    # print(s.minExtraChar(s="leetscode", dictionary=["leet","code","leetcode"]))
    # print(s.minExtraChar(s ="sayhelloworld", dictionary=["hello", "world"]))
    # print(s.minExtraChar(s="dwmodizxvvbosxxw", dictionary =["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]))
    # print(s.minExtraChar(s="ecolloycollotkvzqpdaumuqgs", dictionary=["flbri","uaaz","numy","laper","ioqyt","tkvz","ndjb","gmg","gdpbo","x","collo","vuh","qhozp","iwk","paqgn","m","mhx","jgren","qqshd","qr","qpdau","oeeuq","c","qkot","uxqvx","lhgid","vchsk","drqx","keaua","yaru","mla","shz","lby","vdxlv","xyai","lxtgl","inz","brhi","iukt","f","lbjou","vb","sz","ilkra","izwk","muqgs","gom","je"]))
    # print(s.minExtraChar_greedy(s="azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf",
    #                      dictionary=["na","i","edd","wobow","kecv","b","n","or","jj","zul","vk","yeb","qnfac","azv","grtjba","yswmjn","xowio","u","xi","pcmatm","maqnv"]))
    # print(s.minExtraChar_greedy(s="rkmsilizktprllwoimafyuqmeqrujxdzgp",
    #                             dictionary=["afy","lyso","ymdt","uqm","cfybt","lwoim","hdzeg","th","rkmsi","d","e","tp","r","jx","tofxe","etjx","llqs","cpir","p","ncz","ofeyx","eqru","l","demij","tjky","jgodm","y","ernt","jfns","akjtl","wt","tk","zg","lxoi","kt"]))
    
    print(s.minExtraChar_DP(s="rkmsilizktprllwoimafyuqmeqrujxdzgp",
                                dictionary=["afy","lyso","ymdt","uqm","cfybt","lwoim","hdzeg","th","rkmsi","d","e","tp","r","jx","tofxe","etjx","llqs","cpir","p","ncz","ofeyx","eqru","l","demij","tjky","jgodm","y","ernt","jfns","akjtl","wt","tk","zg","lxoi","kt"]))