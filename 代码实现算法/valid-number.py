#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
"""


class Demo(object):
    def __init__(self, number: str) -> None:
        self.number = number

    def check1(self, data: list) -> bool:
        s = ["+", "-"]
        s1 = data.count(s[0])
        s2 = data.count(s[1])

        if s1 == 0 and s2 == 0:
            return True

        if (s1 == 1 and s2 == 0) or (s1 == 0 and s2 == 1):
            if data.index(s[0]) == 0 or data.index(s[1]) == 0:
                return True

        return False

    def check2(self, data: list) -> bool:
        s = "e"
        s1 = data.count(s)
        if s1 == 0:
            return True

        if s1 == 1:
            index = data.index(s)
            s2 = data[(index + 1) :]
            if len(s2) != 0:
                try:
                    r = int("".join(s2))
                except Exception:
                    pass
                else:
                    if r != 0:
                        return True

        return False

    def check3(self, data: list) -> bool:
        s = "."
        s1 = data.count(s)

        if s1 == 0:
            return True

        if s1 == 1:
            index = data.index("e")
            s2 = data[:index]
            try:
                r = float("".join(s2))
            except Exception:
                pass
            else:
                if r:
                    return True
            
            

        return False

    def check(self) -> bool:
        data = list(self.number)
        # 正负号验证
        if not self.check1(data):
            return False

        # e验证
        if not self.check2(data):
            return False

        # 点验证
        if not self.check3(data):
            return False

        return True


if __name__ == "__main__":
    number = "+1.1e11"
    res = Demo(number).check()
    print(res)
