class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
                freq1 = {}
                freq2 = {}
                x = sorted(s)
                y = sorted(t)
                for i in x:
                    if i not in freq1:
                        freq1[i] = 1
                    else:
                        freq1[i] +=1
                for i in y:
                    if i not in freq2:
                        freq2[i] = 1
                    else:
                        freq2[i] +=1
                if freq1 == freq2:
                        return True
                return False