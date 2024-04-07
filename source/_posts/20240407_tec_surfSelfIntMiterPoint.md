---
title: 自交曲面与 miter point
category: 技术博客
mathjax: true
password: 12317003
---

>**参考资料：**
>[1] Park Y, Hong Q Y, Kim M S, et al. Self-intersection computation for freeform surfaces based on a regional representation scheme for miter points[J]. Computer Aided Geometric Design, 2021, 86: 101979.

笔者认为，曲面自交可以分为三类：

1. 具备边界交点的曲面自交；
2. 内部无 miter point 的曲面自交；
3. 内部有 miter point 的曲面自交。

![类型1](images/20240407_surfSelfIntMiterPoint/case1.png)
![类型2](images/20240407_surfSelfIntMiterPoint/case2.png)
![类型3](images/20240407_surfSelfIntMiterPoint/case3.png)

笔者认为，曲面相交只有类型1与类型2，且都可以通过无限细分的方法计算得到初始点。即相比于曲面相交，曲面自交重点围绕着 miter point 展开。

需要考虑的问题有：

1. miter point 的定义与性质；
2. miter point 的计算方法；

# Miter Point 的定义与性质

首先，曲面普通自交点，满足：

$$
S(u,v) = S(s,t), \quad (u,v) \neq (s,t)
$$

而 miter point 附近的两个参数 $(u,v)$ 与 $(s,t)$ 可以任意接近。即可看作 $(u,v) = (s,t)$。

根据参考资料[1]，miter point 还满足如下条件：

$$
\frac{\partial S}{\partial u} \times \frac{\partial S}{\partial v} = 0
$$

在参考资料[1]中说：~~从一个物理直观的角度来看，我们假设在case3参数空间上，沿交线进行逆时针旋转。在蓝色交线上行走时，映射到欧式空间中，我们是沿右手法则行走的（以曲面法向定义）。而在红色交线上行走时，映射到欧式空间中，我们是沿左手法则行走的。~~ 笔者认为这种解释是错误的或者说不够准确。若以曲面法向定义，则都是沿右手法则行走。

# Miter Point 的计算方法

参考资料[1]提出了一种在BVH中检测 miter point 的方法。文章使用 toroidal 曲面片 $T_{ij}(s,t)$ 拟合每个小子面片 $S_{ij}(u,v)$。当小曲面 $S_{ij}(u,v)$ 与 $T_{ij}(s,t)$ 法向方向的偏差大于某个阈值时，认为存在 miter point。

推广到我们的BVH，可以使用局部坐标系的法向方向与曲面法向方向的夹角来判断是否存在miter point。


# **TO BE CONTINUED...**