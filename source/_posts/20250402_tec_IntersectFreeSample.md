---
title: 样条曲线/曲面无交的网格采样
category: 技术博客
mathjax: true
password: 12317003
---

问题描述：对于输入两个无交的样条曲线/曲面（可能是首尾相接的），如何采样出无交的网格？

如图，两条无交的曲线，由于采样不均匀，可能会出现交叉的情况。
![case2_1](images/20250402_tec_IntersectFreeSample/intersect2D.png)

# 样条曲线采样


## 交点周围采样

先对曲线进行分割得到$C(t)$，使得$C(t)$至$C(0)$的射线与$C$只有一个交点(不包含$C(0)$)。可以通过曲线的每个控制点与第一个控制点的连线，依次为cw/ccw的顺序。

### case1. 曲率方向相反

此情况最简单，两条交线可以随意采样

### case2. 曲率方向相同，切向不同

用t表示在端点处沿曲率最大(most cw/ccw)的曲线的切向，两条曲线的采样点与端点连线的射线落在t的两边。

### case3. 曲率方向相同，切向相同

此情况，先对在端点处曲率最大(most cw/ccw)的曲线进行采样，并得到一条射线。另一条曲线的采样点在该射线与切向之间的夹角范围内。

## 内部采样

在交点周围采样后，从该采样点进行分割，剩余部分为内部采样。

对每条曲线内部算出n个关键采样点参数值Pn。只要采样点包含Pn,就可以保证采样折线无交。

通过BVH、OBB构建包围体，当OBB无交时，进行采样。