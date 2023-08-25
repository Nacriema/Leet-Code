# Link: https://leetcode.com/problems/text-justification/

"""
Problem statement:

Given an array of strings words and maxWidth, format text such each line has exactly maxWidth characters
and fully left, right justified

Pack words in a greedy approach, each pack contains words that much as we can have at each line. Pading 
extra spaces if we need so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line 
does not divide evenly between words, the empty slots on the left will be assigned more spaces than the 
slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
    * A word is defined as a character sequence consisting of non-space characters only.
    * Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    * The input array words contains at least one word.


My idea:

    * Map the list of words to list of the lengths for each word. DONE
    
    
"""
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
            Implement the solution for the text justification problem
        """
        def format_line(words_line: List[str], words_length: int, width: int, isLastLine: bool=False) -> str:
            """
                Given a list of words in line and the maxWidth value
                Return the formated line
                
                Calculate the spaces that we need for each gap, notice that the left will be largest
                
                LAST LINE MUST BE LEFT JUSTIFY !!!
                
                CETNER JUSTIFY - FULLY ALIGNED: Left space is more than other
            """
            if len(words_line) == 1:
                return '{0}{1}'.format(words_line[0], (width - words_length) * " ")
            
            # Here words line has at least 2
            if isLastLine:
                # left-aligned instead of fully-aligned  
                return '{0}{1}'.format(" ".join(words_line), (width - words_length - (len(words_line) - 1)) * " ")
            
            # Handle the overall case (Fully aligned)
            q, r = divmod(width - words_length, len(words_line) - 1)
            out_string = ''
            for i, word in enumerate(words_line):
                if i == (len(words_line)-1):
                    out_string += word
                elif i < r:
                    out_string += word + ' ' * (q+1)
                else:
                    out_string += word + ' ' * q
            
            return out_string
        
        length_of_words = list(map(lambda x: len(x), words))
        print(f'Length of words: {length_of_words}')
        
        # Init the pivot index, keep track of the index of the starting word for each line
        pivot_index = 0
        total_length = 0
        steps = 0
        
        result = []
        line = []
        
        while True:
            print(f'Total length: {total_length}')
            print(f'Pivot: {pivot_index}, Steps: {steps}')
            
            # Check if we have reached the end of words list
            if pivot_index + steps > len(words) - 1:
                print(f'Word in this line: {line}\n')
                result.append(format_line(words_line=line, words_length=total_length, width=maxWidth, isLastLine=True))
                return result
            
            if total_length + length_of_words[pivot_index + steps] + steps <= maxWidth:
                line.append(words[pivot_index + steps])
                total_length += length_of_words[pivot_index + steps]
                steps += 1
            else:
                # Here we got a successfull line
                print(f'Actual length we can get in this line: {total_length + steps - 1}')
                print(f'Word in this line: {line}\n')
                print(f'Total length of these words: {total_length}')
                
                result.append(format_line(words_line=line, words_length=total_length, width=maxWidth))
                
                # Start the new line
                pivot_index += steps
                total_length = 0
                steps = 0
                line = []
        

if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["What","must","be","acknowledgment","shall","be"]
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    
    s = Solution()
    print(s.fullJustify(words=words, maxWidth=20))

    # print(s.format_line(words_line= ['everything', 'else', 'we'], words_length=16, width=20))
    # print(s.format_line(words_line= ['do'], words_length=2, width=20))
    # print(s.format_line(words_line= ['shall', 'be'], words_length=7, width=16, isLastLine=True))
    # print(s.format_line(words_line= ['understand', 'well'], words_length=14, width=20, isLastLine=False))