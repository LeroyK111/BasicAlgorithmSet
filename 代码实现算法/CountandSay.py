def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    if n == 2:
        return "11"

    output = ["1", "1"]

    while n > 2:
        prev = int(output.pop(0))
        count = 1
        for i in range(len(output)):
            num = int(output.pop(0))
            if num == prev:
                count += 1
                continue
            else:
                output.append(str(count))
                output.append(str(prev))
                prev = num
                count = 1
        output.append(str(count))
        output.append(str(prev))
        n -= 1

    return "".join(output)


if __name__ == '__main__':
    data = 4
    result = countAndSay(data)
    print(result)