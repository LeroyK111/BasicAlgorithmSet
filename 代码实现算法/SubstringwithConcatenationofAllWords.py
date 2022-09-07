#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(s: str, word: list) -> list:
    result = []
    words = []
    count = len(word)

    # 将words全排列
    def sortWord(clipData: list = [],
                 word: list = [],
                 words: list = [],
                 count: int = 1):
        if len(clipData) == 0:
            # 必须截取字符串
            x = []
            for s in range(1, 1 + count):
                x.append(word[-s])
            words.append("".join(x))
            return

        for i in clipData:
            word.append(i)
            newData = list(filter(lambda x: x != i, clipData))
            sortWord(newData, word, words, count)

    sortWord(clipData=word, words=words, count=count)
    for i in words:
        result.append(s.find(i))
        s = s.replace(i, "", 1)

    return list(filter(lambda x: x != -1, result))


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar", "22"]
    result = demo(s, words)
    print(result)
