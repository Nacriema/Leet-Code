from typing import List


class Solution:
    """
        There are an optimized solution using prefix tree (Trie)
    """
    def replaceWords_slow(self, dictionary: List[str], sentence: str) -> str:
        """
            Overall: O(len(dictionary) * len(sentence))
        """
        dictionary = sorted(dictionary, key=lambda x: len(x), reverse=False)
        words = sentence.split()
        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break
        return " ".join(words)
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """ 
            Overall O(27*(len(sentence)))
            Construct the Trie: https://en.wikipedia.org/wiki/Trie by using dict

            ====== Node ========
            Structure
                Children Node[Alphabet-Size]
                Is-Terminal Boolean
                Value Data-Type
            end structure

            ====== Trie-Find(x, key) ========
            for 0 ≤ i < key.length do
                if x.Children[key[i]] = nil then
                    return false
                end if
                x := x.Children[key[i]]
            repeat
            return x.Value

            ====== Trie-Insert(x, key, value) ======
            for 0 ≤ i < key.length do
                if x.Children[key[i]] = nil then
                    x.Children[key[i]] := Node()
                end if
                x := x.Children[key[i]]
            repeat
            x.Value := value
            x.Is-Terminal := True

            # NOTE: Using the dictionary instead of List give the faster execution time: self.children is dict instead of List
        """
        class Node:
            def __init__(self, is_terminal=False):
                self.children = {}
                self.is_terminal = is_terminal
        
        def trie_insert(trie: Node, word):
            for char in word:
                if trie.children.get(char, None) is None:
                    trie.children[char] = Node()
                trie = trie.children.get(char)
                if trie.is_terminal: # Skip adding the longer string
                    return
            trie.is_terminal = True

        def trie_find(trie: Node, word):
            for id, char in enumerate(word):
                idx = ord(char) - 97
                if trie.children.get(char, None) is None:
                    if trie.is_terminal:
                        return True, word[:id]
                    return False, word
                trie = trie.children.get(char)
            return True, word
        
        root_trie = Node()  # Initial trie
        dictionary.sort(key=lambda x: len(x), reverse=False)
        for word in dictionary:
            trie_insert(root_trie, word)
        
        words = sentence.split()
        for i, word in enumerate(words):
            flag, string = trie_find(root_trie, word)
            if flag:
                words[i] = string
        return " ".join(words)


if __name__ == '__main__':
    s = Solution()
    # print(s.replaceWords(dictionary = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"))
    # print(s.replaceWords(dictionary = ["a", "b", "c"], sentence = "aadsfasf absbs bbab cadsfafs"))
    print(s.replaceWords(dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
    print(s.replaceWords(dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))

    """
        Prefix Trie
            - Add words from sentence to the Trie
            - For each word in sorted dictionary, check if this word is already have the startsWith this word in the Trie

    
    """