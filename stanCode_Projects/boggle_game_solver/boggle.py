"""
File: boggle.py
Name: Ryan
----------------------------------------
TODO: Boggle
"""

import time


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                cur.children[ch] = TrieNode()
                cur = cur.children[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
trie = Trie()


def main():
    board = []  # [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]

    for i in range(4):
        arr = input(str(i+1)+' row of letters: ').lower().split(' ')
        if len(arr) != 4:
            print('Illegal input')
            return
        for letter in arr:
            if len(letter) > 1 or not letter.isalpha():
                print('Illegal input')
                return
        board.append(arr)

    read_dictionary()
    start = time.time()
    print("There are", len(find_word(board)), "words in total.")
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open('dictionary.txt') as f:
        for line in f:
            word = line.strip()
            if len(word) > 3:
                trie.insert(word)


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    return trie.startsWith(sub_s)


def find_word(board):
    """
    找單字
    :param board: 使用者輸入
    :return: 回傳字典中之答案(單字長大於3)
    """
    ans = []
    for column in range(4):
        for row in range(4):
            helper(board[row][column], row, column, [[False for _ in range(4)] for _ in range(4)], board, ans)
    return ans


def helper(word, row, column, arr, board, ans):
    """
    Helper
    :param word: 欲尋找單字
    :param row: 目前所在列
    :param column: 目前所在行
    :param arr: 目前使用過的字母
    :param board: boggle
    :param ans: 答案集
    """
    if trie.search(word):
        if word not in ans:
            print(f'Found "{word}"')
            ans.append(word)
    if has_prefix(word):
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if 0 > row + y or row + y > 3 or 0 > column + x or column + x > 3 or x == y == 0 or arr[row + y][column + x]:
                    continue
                else:
                    arr[row][column] = True
                    helper(word+board[row + y][column + x], row + y, column + x, arr, board, ans)
                    arr[row][column] = False


if __name__ == '__main__':
    main()

