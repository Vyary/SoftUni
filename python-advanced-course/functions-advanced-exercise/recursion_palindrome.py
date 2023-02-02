def palindrome(word, start_index, end_index=-1):
    if start_index > len(word) / 2:
        return f"{word} is a palindrome"
    if word[start_index] != word[end_index]:
        return f"{word} is not a palindrome"
    return palindrome(word, start_index + 1, end_index - 1)


"""                     Task:
Write a recursive function called palindrome() that will receive a word and an index
(always 0). Implement the function, so it returns "{word} is a palindrome" if the word
is a palindrome and "{word} is not a palindrome" if the word is not a
palindrome using recursion.

Example:
Test Code:
print(palindrome("abcba", 0))
Output:
abcba is a palindrome

Example:
Test Code:
print(palindrome("peter", 0))
Output:
peter is not a palindrome
"""
