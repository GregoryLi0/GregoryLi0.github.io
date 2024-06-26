---
title: 傅里叶级数与变换
category: 技术博客
mathjax: true
date: 2024-03-21
---


>**参考资料：**
>[1] [通俗易懂的理解傅里叶变换（一）](https://zhuanlan.zhihu.com/p/317237264)
>[2] [傅里叶变换](https://zhuanlan.zhihu.com/p/104079068)


傅里叶级数与变换是信号处理中的重要概念，它们可以将信号从时域转换到频域，从而更好地理解信号的特性。傅里叶级数与傅里叶变换不同：

**傅里叶级数**：在时域是一个*周期且连续*的函数，而在频域是一个*非周期离散*的函数。

**傅里叶变换**：在时域是一个*非周期且连续*的函数，转换为频域的一个*非周期连续*的函数。

# 傅里叶级数 Fourier series 

傅里叶级数 Fourier series 直观理解就是任何周期函数都可以分解成无数个正弦函数$Asin(\omega x + \phi)$。进一步可以分解成简单振荡波（正弦波和余弦波）。

其理论基础是三角函数的正交性，即正弦函数和余弦函数在一个周期内的积分为0。可见参考资料[2]。这些基函数的频率是整数倍的基频率，即空间中的基为${1, \sin(x), \cos(x), \sin(2x), \cos(2x), \cdots}$。

而傅里叶级数的公式为：

$$
f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos(n\omega t) + b_n \sin(n\omega t))
$$

其中，$a_0$ 为直流分量，$a_n$ 和 $b_n$ 为交流分量，$\omega$ 为角频率。

![Time and frequency domains](https://gregorygallery.oss-cn-beijing.aliyuncs.com/img/20240321_fourierSerieAndTrans/image.png)

## 时域与频域

时域是指信号随时间变化的情况，频域是指信号随频率变化的情况。傅里叶级数可以将时域的信号转换到频域，即将信号分解成一系列的正弦函数。

# 傅里叶变换 Fourier transform

傅里叶变换是傅里叶级数的推广，它允许我们将一个**非周期**函数转换为频率域表示。这个过程是可逆的，即可以通过逆傅里叶变换从频率域回到时间域。

一个简单的看法就是我们把非周期函数的周期看成无穷大。

具体分析变化参见参考资料[1]。
