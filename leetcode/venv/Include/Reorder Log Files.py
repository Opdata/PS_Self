text = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

class Solution:
    def reorderLogFiles(self, logs) -> list:
        digit_arr, letter_arr = [], []
        for i in logs:
            if i.split()[1].isalpha():
                letter_arr.append(i)
            else:
                digit_arr.append(i)
        letter_arr.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_arr + digit_arr

f = Solution()
f.reorderLogFiles(text)