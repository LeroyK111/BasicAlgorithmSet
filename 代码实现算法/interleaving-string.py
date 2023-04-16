#!/usr/bin/python
# -*- coding: utf-8 -*-


class Demo(object):
    def interlace(self, s1: str, s2: str, s3: str) -> bool:
        s12 = s1 + s2
        strCount = {}
        for i in set(s12):
            c = s12.count(i)
            strCount[i] = c

        for key in strCount.keys():
            if s3.count(key) != strCount[key]:
                return False

        return True


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    result = Demo().interlace(s1, s2, s3)
    print(result)
