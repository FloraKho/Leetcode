class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # for each char in ransomNote
        # If it is in magazine:
            # Remove it from magazine.
        # Else:
            #Return False
        # Return True
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, '', 1)
                ransomNote = ransomNote.replace(i, '', 1)
            else:
                return False
        return True
        