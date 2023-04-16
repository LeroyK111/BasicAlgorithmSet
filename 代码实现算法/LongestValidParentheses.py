class demo(object):

    def findVaild(self, test: str):
        start = test.count("(")
        end = test.count(")")
        if start >= end:
            return start

        return end


if __name__ == '__main__':
    result = demo().findVaild("())")
    print(result)