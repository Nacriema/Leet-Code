""" 
    Problem statement:
        You are given a string num representing a large integer. An integer is good if it meets the following conditions:
            * It is a substring of num with length 3.
            * It consists of only one unique digit.
        
        Return the maximum good integer as a string or an empty string "" if no such integer exists.
        Note:
            * A substring is a contiguous sequence of characters within a string.
            * There may be leading zeroes in num or a good integer.
        

Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
 

Constraints:

3 <= num.length <= 1000
num only consists of digits.

"""
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        candidates = []
        
        num = num.lstrip("0")  # Remove all leading 0's
        if len(num) == 0:
            return "000"
        if len(num) < 3: return ""
        prev = num[0]
        hit = 1
        for i in range(1, len(num)):
            current = num[i]
            if int(current) not in candidates and current == prev:
                hit += 1
                if hit == 3:
                    candidates.append(int(current))
            else:
                hit = 1
            prev = current
        if len(candidates) == 0:
            return ""
        return str(max(candidates)) * 3


if __name__ == '__main__':
    s = Solution()
    print(s.largestGoodInteger(num="6777133339"))
    print(s.largestGoodInteger(num = "2300019"))
    print(s.largestGoodInteger(num = "42352338"))