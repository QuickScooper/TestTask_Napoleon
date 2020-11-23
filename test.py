class Solution:
    def romanToInt(self,s: str) -> int:
        if len(s) > 15 or len(s) < 1:
            return '1 <= s.length <= 15'
        else:
            values = {
                "I" : 1, "V": 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000
            }
            high = 0
            result = 0
            for letter in s[::-1]:
                value = values[letter]
                if value >= high:
                    high = value
                    result += value
                else:
                    result -= value
            return result

if __name__ == "__main__":
    sol = Solution()
    s = input('Input: s = ')

    print(f'Output: {sol.romanToInt(s)}')
