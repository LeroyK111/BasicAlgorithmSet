import numpy as np

# 定义信号
N = 8  # 信号长度
n = np.arange(N)
signal = np.sin(2 * np.pi * n / N)  # 正弦信号


# 计算 DFT
def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X


dft_signal = dft(signal)

# 输出 DFT 结果
print("DFT 结果:", np.round(dft_signal, 2))
