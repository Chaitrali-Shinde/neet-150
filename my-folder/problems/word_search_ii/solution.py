class TrieNode:
    def __init__(self):
        self.childern= {}
        self.endOfWord= False
    
    #add word in tries datastructure
    def addWord(self, word: str):
        curr= self
        for c in word:
            if c not in curr.childern:
                curr.childern[c]= TrieNode()
            curr= curr.childern[c]
        curr.endOfWord= True




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root= TrieNode()
        #make trie of all the word in the words list
        for w in words:
            root.addWord(w)
        
        ROWS, COLS= len(board), len(board[0])
        res, visit= set(), set()

        def dfs(r, c, node, word):
            if (r<0 or c<0 or 
            r==ROWS or c==COLS or 
            (r,c) in visit or 
            board[r][c] not in node.childern):
                return
            visit.add((r,c))
            node= node.childern[board[r][c]]
            word+= board[r][c]
            if node.endOfWord:
                res.add(word)
            
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            #as this solution is backtracking DFS so we need to remove r, c from visited
            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)

            

        