# Last updated: 9/3/2026, 2:12:32 PM
1class Solution:
2    def multiply(self, num1: str, num2: str) -> str:
3        if num1 == "0" or num2 == "0":
4            return "0"
5
6        res = [0] * (len(num1) + len(num2))
7
8        for i in range(len(num1) - 1, -1, -1):
9            for j in range(len(num2) - 1, -1, -1):
10                mul = int(num1[i]) * int(num2[j])
11                p1, p2 = i + j, i + j + 1
12                
13                total = mul + res[p2]
14                res[p2] = total % 10
15                res[p1] += total // 10
16
17        # Skip leading zeros
18        start = 0
19        while start < len(res) and res[start] == 0:
20            start += 1
21
22        return "".join(map(str, res[start:]))