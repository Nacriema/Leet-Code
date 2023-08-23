# Link for the problem: https://leetcode.com/problems/excel-sheet-column-title/
import string

# My solution
def convertToTitle(columnNumber):
    """
    Idea: 
        - Same idea when we trying to convert a number to any base
        - Modify when the remainder == 0, then q -= 1 and we reassign it to the number, loop untill it finished
    """
    string_list = string.ascii_lowercase[:26]
    digits = []
    while columnNumber > 0:
        q, r =  columnNumber // 26, columnNumber % 26
        if r == 0:
            q -= 1
            r = 26
        digits.append(r)
        columnNumber = q
    result = ''.join(list(map(lambda x: string_list[x - 1].upper(), reversed(digits))))
    return result

# Optimal solution
def optimal_convertToTitle(columnNumber):
    """
    :type columnNumber: int
    :rtype: str
    """
    res = []
    while columnNumber:
        columnNumber -= 1
        res.append(chr(ord('A') + columnNumber % 26))
        columnNumber //= 26
    return ''.join(reversed(res))


if __name__ == '__main__':
    print(convertToTitle(columnNumber=28))
