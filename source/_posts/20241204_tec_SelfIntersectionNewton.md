---
title: 曲面自交技术 - 牛顿迭代
category: 技术博客
mathjax: true
password: 12317003
---

本文试图使用牛顿迭代法解决曲面自交问题。

重点考虑：

1. 曲面自交为$R(s, t) = R(u, v)$，且要求 $(s, t) \neq (u, v)$；

## 算法思路

样条曲面本身给定了三个方程，几何曲面自交定义可以写出方程组：

$$
\begin{cases}
R_1(s, t) = R_1(u, v)\\
R_2(s, t) = R_2(u, v)\\
R_3(s, t) = R_3(u, v)
\end{cases}
\quad \quad (s, t) \neq (u, v)
$$

其中 $R_i$ 为曲面的三个方程。

如果仅仅考虑这三个方程，还未添加$(s, t) \neq (u, v)$的约束。因此，我们需要添加一个约束方程$L$，使得$L(s, t, u, v) = \infty$。例如：

$$
L(s, t, u, v) = (s - u)^2 + (t - v)^2 \\
L(s, t, u, v) = -log((s - u)^2 + (t - v)^2)
$$

此时，算法目标改为一个优化问题：

$$
\min_{s, t, u, v} \left\{ \begin{aligned}
& R_1(s, t) - R_1(u, v) \\
& R_2(s, t) - R_2(u, v) \\
& R_3(s, t) - R_3(u, v) \\
& L(s, t, u, v)
\end{aligned} \right.
$$

$$
\min_{s, t, u, v} \left\{ (R_1(s, t) - R_1(u, v))^2 + (R_2(s, t) - R_2(u, v))^2 + (R_3(s, t) - R_3(u, v))^2 + L(s, t, u, v) \right\}
$$

其导数为：

$$
\begin{cases}
\frac{\partial f}{\partial s} = 2(R_1(s, t) - R_1(u, v)) \cdot \frac{\partial R_1}{\partial s} + 2(R_2(s, t) - R_2(u, v)) \cdot \frac{\partial R_2}{\partial s} + 2(R_3(s, t) - R_3(u, v)) \cdot \frac{\partial R_3}{\partial s} + 2(s - u) \\
\frac{\partial f}{\partial t} = 2(R_1(s, t) - R_1(u, v)) \cdot \frac{\partial R_1}{\partial t} + 2(R_2(s, t) - R_2(u, v)) \cdot \frac{\partial R_2}{\partial t} + 2(R_3(s, t) - R_3(u, v)) \cdot \frac{\partial R_3}{\partial t} + 2(t - v) \\
\frac{\partial f}{\partial u} = -2(R_1(s, t) - R_1(u, v)) \cdot \frac{\partial R_1}{\partial u} - 2(R_2(s, t) - R_2(u, v)) \cdot \frac{\partial R_2}{\partial u} - 2(R_3(s, t) - R_3(u, v)) \cdot \frac{\partial R_3}{\partial u} - 2(s - u) \\
\frac{\partial f}{\partial v} = -2(R_1(s, t) - R_1(u, v)) \cdot \frac{\partial R_1}{\partial v} - 2(R_2(s, t) - R_2(u, v)) \cdot \frac{\partial R_2}{\partial v} - 2(R_3(s, t) - R_3(u, v)) \cdot \frac{\partial R_3}{\partial v} - 2(t - v)
\end{cases}
$$