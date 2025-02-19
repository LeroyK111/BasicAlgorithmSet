import sympy as sp

# 定义变量
t, w = sp.symbols("t w")

# 定义一个信号（如矩形波）
f = sp.Piecewise((1, abs(t) < 1), (0, True))  # 矩形脉冲

# 计算傅立叶变换
F_w = sp.fourier_transform(f, t, w)

# 显示结果
sp.pprint(F_w)
