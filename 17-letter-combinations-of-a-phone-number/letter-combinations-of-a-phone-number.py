class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {"2":"abc", "3":"def","4":"ghi",
        "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        result = []

        def backtrack(index,current_combination):
            if len(digits) == len(current_combination):
                result.append(current_combination)
                return

            curr_letters = letters[digits[index]]

            for letter in curr_letters:
                backtrack(index+1,current_combination+letter)

        backtrack(0, "")
        return result