class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        translator = str.maketrans('', '', string.punctuation)
        s = s.translate(translator)
        s = s.lower()
        x = s[::-1]
        if x == s:
            return True
        else:
            return False