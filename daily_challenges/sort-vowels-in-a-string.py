from collections import Counter


class Solution:
    def sortVowelsSLOW(self, s: str) -> str:
        index = []
        asci = []
        for i in range(len(s)):
            if s[i].lower() in ('a', 'e', 'i', 'o', 'u'):
                asci.append((ord(s[i]), s[i]))
                index.append(i)
        
        # Sort by the ascii value
        index = set(index)
        print(index)
        asci = sorted(asci, key=lambda x: x[0])
        print(asci)

        rs = ''
        count = 0
        for i in range(len(s)):
            if i in index:
                rs += asci[count][1]
                count += 1
            else:
                rs += s[i]
        return rs
    
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        count_char = Counter(s)
        print(f'Count char: {count_char}')

        s_vowels = []
        for char in count_char.keys():
            if char in vowels:
                s_vowels.append(char)                
                s = s.replace(char, '_')  
        print(f's_vowels: {s_vowels}')                            
        s_vowels.sort()
        print(f's_vowel sort: {s_vowels}')
        
        for char in s_vowels:
            s = s.replace('_', char, count_char[char])
            print(s)
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.sortVowels(s = "lEetcOde"))