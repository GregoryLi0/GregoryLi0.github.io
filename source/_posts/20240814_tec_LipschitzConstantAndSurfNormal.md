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
\|S(u_1,v_1)-S(u_2,v_2)\|\leq L\|(u_1,v_1)-(u_2,v_2)\|.
$$

可推导：

$$
L=\max\left(\frac{\|S(u_1,v_1)-S(u_2,v_2)\|}{\|(u_1,v_1)-(u_2,v_2)\|}\right)= \max\left(\frac{\|S(u_1,v_1)-S(u_2,v_2)\|}{\sqrt{(u_2-u_1)^2+(v_2-v_1)^2}}\right)
$$2
$$
\geq\max\left(\frac{\|S(u_1,v_1)-S(u_2,v_2)\|}{|u_2-u_1|+|v_2-v_1|}\right)
$$

一个冗余的 Lipschitz 常数计算公式为：

$$
L=\sqrt{\max(S_u)^2+\max(S_v)^2}.
$$

只需证明$\sqrt{\max(S_u)^2+\max(S_v)^2}\geq\max\left(\frac{\|S(u_1,v_1)-S(u_2,v_2)\|}{\|(u_1,v_1)-(u_2,v_2)\|}\right)$, 则可将其作为冗余的 Lipshcitz 常数。


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

## Lipschitz 加成下的 Marching Method

相比于传统的 Marching Method，其特点有：

1. 使用BVH对两曲面进行细分，在每个子域上计算Lioschitz常数, 以此辅助计算步长；

2. 该 Marching Method 必须有st uv参数坐标；

# 中值定理推广

存在向量值函数的中值定理不等式：

对于一个连续的向量值函数 $f:[a,b]\to\mathbb{R}^n$，在 $(a,b)$ 上可导，那么存在一个点 $c\in(a,b)$，使得：

$$
\|f(b)-f(a)\|\leq(b-a)\|f'(c)\|
$$

则只看曲面的一个参数分量，固定另一个，以 $u$ 举例，在 $Y\in[u1,u2]$ 上，那么存在一个点 $c\in(u1,u2)$：

$$
\|S(u1,v)-S(u2,v)\|\leq(b-a)\|Y'(c)\|
$$

# 14.12.17更新

最近尝试计算更精确的 Lipschitz 常数，以及计算变化率的下界。

## 基础知识

对一些微分几何的基础知识进行回顾。

### 偏导数

#### 对多元方程：

- **定义**：设函数$z = f(x,y)$在点$(x_0,y_0)$的某一邻域内有定义，当$y$固定在$y_0$而$x$在$x_0$处有增量$\Delta x$时，相应地函数有增量$f(x_0+\Delta x,y_0)-f(x_0,y_0)$，如果极限$\lim\limits_{\Delta x \to 0}\frac{f(x_0+\Delta x,y_0)-f(x_0,y_0)}{\Delta x}$存在，则称此极限为函数$z = f(x,y)$在点$(x_0,y_0)$处对$x$的偏导数，记作$f_{x}(x_0,y_0)$或$\frac{\partial z}{\partial x}\big|_{(x_0,y_0)}$。同理可定义函数$z = f(x,y)$在点$(x_0,y_0)$处对$y$的偏导数$f_{y}(x_0,y_0)$或$\frac{\partial z}{\partial y}\big|_{(x_0,y_0)}$。对于多元函数$u = f(x_1,x_2,\cdots,x_n)$，可类似地定义它对$x_i$的偏导数$\frac{\partial u}{\partial x_i}$。

- **几何意义**：对于二元函数$z = f(x,y)$，$f_x(x_0,y_0)$表示曲面$z = f(x,y)$与平面$y = y_0$的交线在点$(x_0,y_0,f(x_0,y_0))$处的切线对$x$轴的斜率；$f_y(x_0,y_0)$表示曲面$z = f(x,y)$与平面$x = x_0$的交线在点$(x_0,y_0,f(x_0,y_0))$处的切线对$y$轴的斜率。

#### 对多元方程组：

- **定义**：对于由$m$个方程组成的多元方程组$\begin{cases}F_1(x_1,x_2,\cdots,x_n)=0\\F_2(x_1,x_2,\cdots,x_n)=0\\\cdots\\F_m(x_1,x_2,\cdots,x_n)=0\end{cases}$，其中$x_1,x_2,\cdots,x_n$为变量，我们可以对每个方程$F_i$关于每个变量$x_j$求偏导数，记为$\frac{\partial F_i}{\partial x_j}$。

- **作用**：偏导数在研究多元方程组的性质和求解过程中起着重要作用。例如，在判断方程组所确定的隐函数是否存在及可微性时，需要根据偏导数组成的雅可比行列式来进行判断。同时，在使用牛顿迭代法等数值方法求解多元方程组时，也需要计算偏导数来确定迭代的方向和步长。

### 梯度
#### 对多元方程：
- **定义**：设函数$z = f(x,y)$在平面区域$D$内具有一阶连续偏导数，则对于每一点$P(x,y)\in D$，都可定义一个向量$\nabla f(x,y)=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)$，该向量称为函数$z = f(x,y)$在点$P(x,y)$的梯度，记作$\nabla f(x,y)$或$grad f(x,y)$。对于三元函数$u = f(x,y,z)$，其梯度为$\nabla f(x,y,z)=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\right)$。一般地，对于多元函数$u = f(x_1,x_2,\cdots,x_n)$，其梯度是一个$n$维向量$\nabla f(x_1,x_2,\cdots,x_n)=\left(\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2},\cdots,\frac{\partial f}{\partial x_n}\right)$。
- **几何意义**：梯度向量的方向与函数在该点处的等高线（面）垂直，且指向函数值增加最快的方向；梯度的模$\vert\nabla f(x,y)\vert=\sqrt{(\frac{\partial f}{\partial x})^2+(\frac{\partial f}{\partial y})^2}$表示函数在该点处变化率的大小。

#### 对多元方程组：
- **定义**：对于多元方程组中的每个函数$F_i(x_1,x_2,\cdots,x_n)$，都可以定义其梯度$\nabla F_i=\left(\frac{\partial F_i}{\partial x_1},\frac{\partial F_i}{\partial x_2},\cdots,\frac{\partial F_i}{\partial x_n}\right)$。整个方程组可以看作是一个从$\mathbb{R}^n$到$\mathbb{R}^m$的向量值函数$\mathbf{F}=(F_1,F_2,\cdots,F_m)$，那么该向量值函数的雅可比矩阵$J_{\mathbf{F}}$为一个$m\times n$矩阵，其第$i$行第$j$列的元素就是$\frac{\partial F_i}{\partial x_j}$，可以将其看作是一种广义的梯度。
- **作用**：梯度提供了方程组在某点附近的局部线性近似信息，可用于分析方程组所确定的函数的变化趋势和极值情况等。在求解多元方程组时，雅可比矩阵的性质对于迭代方法的收敛性和稳定性有重要影响。例如，当雅可比矩阵非奇异时，通常可以保证牛顿迭代法在局部的收敛性。

### 偏导数与梯度的关系

#### 对多元方程：
- **组成关系**：梯度是由多元函数的各个偏导数组成的向量。例如对于二元函数$z = f(x,y)$，其梯度$\nabla f(x,y)=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)$，就是由对$x$的偏导数和对$y$的偏导数构成的二维向量。
- **方向指示关系**：偏导数只反映了函数沿某个坐标轴方向的变化率，而梯度则综合了函数在各个坐标轴方向的变化率信息，并且指出了函数在某点处变化最快的方向。例如，在某点处函数对$x$的偏导数较大，而对$y$的偏导数较小，那么梯度向量就会在$x$轴方向上的分量较大，从而指向函数值增加更快的大致方向。
- **计算关系**：在计算梯度时，需要先求出函数的各个偏导数，然后将它们组合成向量形式。因此，偏导数的计算是求梯度的基础。

#### 对多元方程组：
- **组成关系**：对于多元方程组所对应的向量值函数，其雅可比矩阵的每一行就是对应方程的梯度向量的转置。即雅可比矩阵是由各个方程的梯度向量组成的矩阵，通过雅可比矩阵可以方便地同时考察多个函数的梯度信息。
- **求解关系**：在求解多元方程组时，常常需要利用偏导数来构造迭代公式，而梯度信息则为确定迭代的方向提供了依据。例如，牛顿迭代法中，需要计算雅可比矩阵的逆与函数值向量的乘积来确定迭代步长和方向，这其中就涉及到了偏导数和梯度的综合运用。
- **几何意义关系**：在几何上，偏导数表示每个方程所确定的超曲面在相应坐标轴方向上的斜率，而梯度则表示该超曲面在某点处的法向量（在隐函数存在定理的条件下）。对于整个多元方程组而言，雅可比矩阵的列向量可以看作是在各个变量方向上的“变化率向量”，它们共同描述了方程组所确定的函数关系在高维空间中的变化情况。