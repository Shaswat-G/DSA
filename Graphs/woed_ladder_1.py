"""
Word Ladder Problem

Problem Statement:
Given two distinct words `startWord` and `targetWord`, and a list `wordList` of unique words of equal lengths, find the length of the shortest transformation sequence from `startWord` to `targetWord`.

Conditions:
- A word can only consist of lowercase characters.
- Only one letter can be changed in each transformation.
- Each transformed word must exist in the `wordList` including the `targetWord`.
- `startWord` may or may not be part of the `wordList`.

Note: If there’s no possible way to transform the sequence from `startWord` to `targetWord`, return 0.

Input:
- wordList: Set[str] - A set of unique words of equal lengths.
- startWord: str - The starting word.
- targetWord: str - The target word.

Output:
- int - The length of the shortest transformation sequence, or 0 if no transformation is possible.

Example 1:
Input:
wordList = {"des","der","dfr","dgt","dfs"}
startWord = "der", targetWord = "dfs"
Output: 3

Explanation:
The length of the smallest transformation sequence from "der" to "dfs" is 3 i.e. "der" -> (replace ‘e’ by ‘f’) -> "dfr" -> (replace ‘r’ by ‘s’) -> "dfs". So, it takes 3 different strings for us to reach the `targetWord`. Each of these strings are present in the `wordList`.

Example 2:
Input:
wordList = {"geek", "gefk"}
startWord = "gedk", targetWord= "geek"
Output: 2

Explanation:
The length of the smallest transformation sequence from "gedk" to "geek" is 2 i.e. "gedk" -> (replace ‘d’ by ‘e’) -> "geek". So, it takes 2 different strings for us to reach the `targetWord`. Each of these strings are present in the `wordList`.
"""

from typing import Set
from collections import deque


def word_ladder_length(startWord: str, targetWord: str, wordList: Set[str]) -> int:
    """
    Find the length of the shortest transformation sequence from startWord to targetWord.

    :param startWord: str - The starting word.
    :param targetWord: str - The target word.
    :param wordList: Set[str] - The set of unique words of equal lengths.
    :return: int - The length of the shortest transformation sequence, or 0 if no transformation is possible.
    """
    q = deque([(startWord, 0)])

    visited = {allowed_word: False for allowed_word in wordList}

    while q:
        cur_word, cur_t = q.popleft()

        for possible_word in generate_possible_words(cur_word):
            if possible_word in wordList:
                if not visited[possible_word]:
                    q.append((possible_word, cur_t + 1))
                    visited[possible_word] = True
                    if possible_word == targetWord:
                        return cur_t + 1 + 1

    return 0


def generate_possible_words(word):

    possible_words = []
    alphabets = "abcdefghijklmnopqrtsuvwxyz"
    assert len(alphabets) == 26
    for idx, character in enumerate(word):
        for alphabet in alphabets:
            if character != alphabet:
                new_word = word[:idx] + alphabet + word[idx + 1 :]
                possible_words.append(new_word)

    return possible_words


# Example test cases
if __name__ == "__main__":
    # Test case 1
    wordList1 = {"des", "der", "dfr", "dgt", "dfs"}
    startWord1 = "der"
    targetWord1 = "dfs"
    print(
        "Test Case 1 - Expected: 3, Got:",
        word_ladder_length(startWord1, targetWord1, wordList1),
    )

    # Test case 2
    wordList2 = {"geek", "gefk"}
    startWord2 = "gedk"
    targetWord2 = "geek"
    print(
        "Test Case 2 - Expected: 2, Got:",
        word_ladder_length(startWord2, targetWord2, wordList2),
    )

    # Test case 3: No possible transformation
    wordList3 = {"abc", "def", "ghi"}
    startWord3 = "xyz"
    targetWord3 = "abc"
    print(
        "Test Case 3 - Expected: 0, Got:",
        word_ladder_length(startWord3, targetWord3, wordList3),
    )

    # Test case 4: Empty word list
    wordList4 = set()
    startWord4 = "abc"
    targetWord4 = "def"
    print(
        "Test Case 4 - Expected: 0, Got:",
        word_ladder_length(startWord4, targetWord4, wordList4),
    )
