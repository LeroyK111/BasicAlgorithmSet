#!/usr/bin/python
# -*- coding: utf-8 -*-


class Demo(object):
    def __init__(self, words: list, maxWidth: int):
        self.words = words
        self.maxWidth = maxWidth
        self.data = []

    def spacePadding(self):
        result = []

        for ls in self.data:
            ls1 = " ".join(ls)
            count1 = len(ls1)
            ls.insert(1, (self.maxWidth - count1 - 1) * " ")
            result.append(" ".join(ls))
        return result

    def run(self):
        ls = []
        count = 0
        space = 0
        for word in self.words:
            c = len(word)
            if c > self.maxWidth:
                return "Long word?"
            count += c
            if len(ls) != 0:
                space = len(ls) - 1
            if count + space <= self.maxWidth:
                ls.append(word)
            else:
                count = c
                space = 0
                self.data.append(ls)
                ls = [word]
                if self.words[-1] == word:
                    self.data.append(ls)

        result = self.spacePadding()
        # for i in result:
        #     print(len(i))
        return result


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    result = Demo(words, maxWidth).run()
    print(result)
