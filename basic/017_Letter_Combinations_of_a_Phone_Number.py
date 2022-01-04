class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # define the hash table that maps phone number to letters
        mapping = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # recursion
        if len(digits) == 0:
            return ''
        elif len(digits) == 1:
            return list(mapping[digits[0]])
        else:
            prev = digits[:-1]
            last = mapping[digits[-1]]
            return [i + j for i in self.letterCombinations(prev) for j in last]