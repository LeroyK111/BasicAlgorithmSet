def demo(longStr, sonStr):

    return longStr.find(sonStr)


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    startIndex = demo(haystack, needle)
    print(startIndex)