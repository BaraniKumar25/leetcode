# Last updated: 8/31/2026, 4:27:06 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        if not digits:
4            return []
5
6        phone_map = {
7            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
8            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
9        }
10        
11        res = []
12        
13        def backtrack(index, path):
14            if index == len(digits):
15                res.append("".join(path))
16                return
17            
18            for letter in phone_map[digits[index]]:
19                path.append(letter)
20                backtrack(index + 1, path)
21                path.pop()
22
23        backtrack(0, [])
24        return res