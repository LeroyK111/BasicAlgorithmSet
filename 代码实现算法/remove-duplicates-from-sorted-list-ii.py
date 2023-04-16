class Solution:
    def demo(self, data: list) -> list:
        result = []
        for i in set(data):
            if data.count(i) == 1:
                result.append(i)

        return result


if __name__ == "__main__":
    head = [1, 2, 3, 3, 4, 4, 5]
    result = Solution().demo(head)
    print(result)
