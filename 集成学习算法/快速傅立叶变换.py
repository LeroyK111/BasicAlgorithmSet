import numpy as np
import matplotlib.pyplot as plt

# 生成一个包含两个正弦波的信号
fs = 1000  # 采样率
t = np.linspace(0, 1, fs, endpoint=False)  # 时间
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# 计算 FFT
fft_signal = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), 1 / fs)

# 只显示正频率部分
half_N = len(t) // 2
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("时域信号")
plt.xlabel("时间 (s)")
plt.ylabel("振幅")

plt.subplot(2, 1, 2)
plt.plot(frequencies[:half_N], np.abs(fft_signal[:half_N]) / half_N)
plt.title("FFT 变换后的频谱")
plt.xlabel("频率 (Hz)")
plt.ylabel("幅值")

plt.tight_layout()
plt.show()
