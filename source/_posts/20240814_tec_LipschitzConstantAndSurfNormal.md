---
title: NURBS 曲面上 Lipschitz 常数与法向
category: 技术博客
mathjax: true
password: 12317003
---

最近阅读了些论文，可以计算多项式/有理 Bezier 曲面的导数、法向的方向锥与大小。那么，这篇博客就来推导一下 NURBS 曲面上的 Lipschitz 常数与这些值的关系。

# Lipschitz 常数

直观地理解，Lipschitz 常数是一个函数的变化速率的上限。Lipschitz 连续性是一种强的连续性，它保证了函数的变化速率是有界的。

## Lipschitz 定义

设 $f$ 是定义在 $D$ 上的函数，$D$ 是 $\mathbb{R}^n$ 的子集。如果存在一个常数 $L$，使得对于 $D$ 中任意两点 $x_1$ 和 $x_2$，有：

$$
\|f(x_1)-f(x_2)\|\leq L\|x_1-x_2\|,
$$

则称 $f$ 在 $D$ 上是 Lipschitz 连续的，常数 $L$ 称为 Lipschitz 常数。

如果 $f(x)$ 在定义域 $D$ 上可导，则 $L$ 可以表示为：

$$
L=\max_{x\in D}\|f'(x)\|.
$$

# 参数曲面的 Lipschitz 常数

## 参数曲面上，Lipschitz 常数的作用

如果我们给出参数域到空间映射的 Lipschitz 常数，它有什么用呢？假设我们在参数域 $D_1$ 上计算得到其 Lipschitz 常数为 $L_1$。则若要在三维域达到精度 $\varepsilon$，我们可以通过以下公式计算在参数域上的步长 $h$：

$$
h=\frac{\varepsilon}{L_1}.
$$

当在参数域上取步长 $h$ 时，我们可以保证在三维空间上迭代前后两点 $p_1, p_2$的误差不超过 $\varepsilon$。

**TODO** 是否能得到 $p_1, p_2$ 之间的点距离同样不超过 $\varepsilon$？

## 参数曲面的 Lipschitz 常数计算

我们考虑三维空间中的参数曲面 $S(u,v)$，其中 $u,v\in[a,b]$。我们可以将 $S(u,v)$ 看做一个从 $[a,b]\times[a,b]$ 到 $\mathbb{R}^3$ 的映射。那么， $S(u,v)$ 的 Lipschitz 常数定义为：

$$
\|S(u_1,v_1)-S(u_2,v_2)\|\leq L\|(u_1,v_1)-(u_2,v_2)\|_2.
$$

一个冗余的 Lipschitz 常数计算公式为：

$$
L=\sqrt{\max(S_u)^2+\max(S_v)^2}.
$$

其中 $S_u$ 和 $S_v$ 分别是 $S(u,v)$ 对 $u$ 和 $v$ 的偏导数。

但是，这个公式是不准确的。因为 $S_u$ 和 $S_v$ 的最大值不一定同时出现在同一个点。

$$
\sqrt{(Xp_2-Xp_1)^2}+\sqrt{(Yp_2-Yp_1)^2}+\sqrt{(Zp_2-Zp_1)^2}\leq L(p2-p1).
$$

$$
L\geq \frac{\sqrt{(Xp_2-Xp_1)^2}}{p2-p1}+\frac{\sqrt{(Yp_2-Yp_1)^2}}{p2-p1}+\frac{\sqrt{(Zp_2-Zp_1)^2}}{p2-p1}.
$$

即

$$
L\geq \frac{\partial X}{\partial p} + \frac{\partial Y}{\partial p} + \frac{\partial Z}{\partial p}.
$$

而我们已知 $S_u$ 和 $S_v$ 的方向范围和最大模长。$S_u$ 的最大模长，即为:

$$
\max(S_u)=\max_{(u,v)\in[a,b]\times[a,b]}\sqrt{(\frac{\partial X}{\partial u})^2+(\frac{\partial Y}{\partial u})^2+(\frac{\partial Z}{\partial u})^2}.
$$

$S_v$ 的最大模长，即为:

$$
\max(S_v)=\max_{(u,v)\in[a,b]\times[a,b]}\sqrt{(\frac{\partial X}{\partial v})^2+(\frac{\partial Y}{\partial v})^2+(\frac{\partial Z}{\partial v})^2}.
$$

法向为:

$$
N=S_u\times S_v.
$$

问题：Lipschitz 常数和这者有何关系？


********
***以下推导由AI帮手完成***

我们考虑三维空间中的参数曲面 $S(u,v)$，其中 $u,v\in[a,b]$。我们可以将 $S(u,v)$ 看做一个从 $[a,b]\times[a,b]$ 到 $\mathbb{R}^3$ 的映射。那么，我们可以定义 $S(u,v)$ 的 Lipschitz 常数为：

$$
L=\max_{(u,v)\in[a,b]\times[a,b]}\|S_u(u,v)\times S_v(u,v)\|.
$$

其中 $S_u(u,v)$ 和 $S_v(u,v)$ 分别是 $S(u,v)$ 对 $u$ 和 $v$ 的偏导数。

********
***推导结束***
