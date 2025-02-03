class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available_letters = {}

        for letter in magazine:
            if letter in available_letters:
                available_letters[letter] += 1
            else:
                available_letters[letter] = 1
        
        for letter in ransomNote:
            if letter in available_letters and available_letters[letter] > 0:
                available_letters[letter] -= 1
            else:
                return False
        
        return True