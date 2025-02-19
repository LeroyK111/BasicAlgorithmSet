"""
数据压缩算法用于减少数据大小，常用于 存储优化、传输加速。主要分为：

无损压缩（Lossless Compression）：压缩后可完全恢复原始数据，如 ZIP、PNG。
有损压缩（Lossy Compression）：压缩后数据不可完全恢复，但可接受，如 JPEG、MP3。

"""

import heapq
from collections import Counter, namedtuple


# 定义 Huffman 节点
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq  # 让优先队列按照频率排序


# 生成 Huffman 树
def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(char, freq, None, None) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left, right = heapq.heappop(heap), heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, parent)

    return heap[0]


# 生成 Huffman 编码表
def build_huffman_codes(tree, prefix="", codebook={}):
    if tree:
        if tree.char:
            codebook[tree.char] = prefix
        build_huffman_codes(tree.left, prefix + "0", codebook)
        build_huffman_codes(tree.right, prefix + "1", codebook)
    return codebook


# 编码文本
def huffman_encode(text, codebook):
    return "".join(codebook[char] for char in text)


# 解码 Huffman 编码
def huffman_decode(encoded_text, tree):
    decoded_text = []
    node = tree
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char:
            decoded_text.append(node.char)
            node = tree
    return "".join(decoded_text)


# 测试 Huffman 压缩
text = "hello huffman"
tree = build_huffman_tree(text)
codebook = build_huffman_codes(tree)
encoded = huffman_encode(text, codebook)
decoded = huffman_decode(encoded, tree)

print("原始文本:", text)
print("Huffman 编码:", encoded)
print("解码后文本:", decoded)
