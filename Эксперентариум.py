# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         BeforMiddle = [s[0]]
#         PostMiddle = list(s[-1:0:-1])
#         b = ''
#         MaxPalin = str[s[0]]
#         while len(PostMiddle) > 0:
#             palinC = b

#             for i in range(0,min(len(BeforMiddle),len(PostMiddle))):
#                 PalinUp = BeforMiddle[-1 - i]
#                 if BeforMiddle[-1 - i] == PostMiddle[-1 - i]:
#                     palinC = PalinUp + palinC + PalinUp
#                 else:
#                     break
            
#             if b != '':
#                 BeforMiddle.append(b)
#                 b = ''
#             else:
#                 b = PostMiddle.pop()
            
#             if len(MaxPalin) < len(palinC):
#                 MaxPalin = palinC
#         return MaxPalin
    
# s = Solution()
# print(s.longestPalindrome("a"))

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        Zig = numRows - 2
        AllRows = [[]]*numRows
        Start = 0
        print(AllRows[0])
        while Start + 1 <= numRows:
            NowStars = Start
            while NowStars <= len(s) - 1:
                AllRows[Start].append(s[NowStars])
                NowStars += numRows - Start + Zig
s = Solution()
print(s.convert("PAYPALISHIRING", 3))