"""
    Problem statement: 
        Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

        An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
        substrings respectively, such that:

            * s = s1 + s2 + ... + sn
            * t = t1 + t2 + ... + tm
            * |n - m| <= 1
            
        The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
        Note: a + b is the concatenation of strings a and b.
        
        
        Follow up: Could you solve it using only O(s2.length) additional memory space?
    
    # TODO: How can I cached just O(s2.length)
"""


class Solution:
    def isInterleave_with_cache(self, s1: str, s2: str, s3: str) -> bool:
        """
            This is a hard problem ;<
            Hint - use DP to solve
        """
        
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        
        # 1. Handle trivial case (passed 63 / 106) cases
        if s1_len + s2_len != s3_len:
            return False 
        
        # 2. Handle hard cases
        # Example: "aabcc"  "dbbca" vs "aadbbbaccc"
        mem = {}
        
        def checker(i: int, j: int, k: int) -> bool:
            """
                i: pointer indicate pivot of s1 string
                j: pointer indicate pivot of s2 string
                k: pointer of the constructed string
            """
            print(f'i: {i}, j: {j}')
            
            if k == s3_len:
                return True
            
            if (i, j) in mem:
                return mem[(i, j)]
            
            # Try to add
            ans = False  # Variable that tell us the current can
            
            # In case of recurrent, we need to store the result of the previous work to advoid redoing the process ath the checker
            if i < s1_len and s1[i] == s3[k]:
                ans = checker(i + 1, j, k + 1)
            
            if j < s2_len and s2[j] == s3[k]:
                ans = ans or checker(i, j + 1, k + 1)
            
            mem[(i, j)] = ans
            return ans
        
        return checker(0, 0, 0)


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
            How can I convert from recurrent to 
        """
        global my_stack 
        my_stack = []  # Stack will contains the variables - the params
        my_stack.append((s1, s2, s3))
        count = 0
        
        def recusive_check(str1, str2, str3):
            # Handle base case
            if str1 == "":
                return str3 == str2
            if str2 == "":
                return str3 == str1
            if str3[-1] not in (str2[-1], str1[-1]):
                return False
            else:
                if str3[-1] == str2[-1]:
                    my_stack.append((str1, str2[:-1], str3[:-1]))
                if str3[-1] == str1[-1]:
                    my_stack.append((str1[:-1], str2, str3[:-1]))
        
        while len(my_stack) > 0:
            s1, s2, s3 = my_stack.pop()
            count += 1
            print(f'Count: {count}')
            if recusive_check(s1, s2, s3) == True:
                return True
        return False
    

if __name__ == '__main__':
    s = Solution()
    # print(s.isInterleave_with_cache(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
    # print(s.isInterleave_with_cache(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
    # print(s.isInterleave_with_cache(s1="", s2="", s3="a"))
    # print(s.isInterleave_with_cache(s1="ab", s2="bc", s3="babc"))
    print(s.isInterleave_with_cache(s1="bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
                                     s2="babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
                                     s3="babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))