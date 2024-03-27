---
title: NRUBS Intersect 寻找闭合交线上的初始交点
category: 技术博客
mathjax: true
---

贾宇的公众号 *贾宇的研究手稿* 中发布了 *Initial Point on Closed Intersection Curve* 推文，其中涉及若干公式计算。本文的目标是理解其内容，并与程老师 SIGGRAPH 论文孤立点/小环部分进行对比。

结论：整体思想没有区别。

# Initial Point on Closed Intersection Curve 步骤解析

> 注：贾宇的推文原文见结尾。

**输入：** 两个曲面 $P(u, v)$ 和 $Q(s, t)$

这两个曲面的交点/交线满足: $P(u, v) - Q(s, t) = 0$

Step1: 对上式进行全微分，得到：

$$
P_u du + P_v dv - Q_s ds - Q_t dt = 0
$$

Step2: 两边同时除以 $dt$，得到：

$$
P_u\frac{du}{dt} + P_v\frac{dv}{dt} - Q_s\frac{ds}{dt} = Q_t
$$

Step3: 分别乘以 $P_u$, $P_v$, $Q_s$，得到：

$$
P_u^2\frac{du}{dt} + P_uP_v\frac{dv}{dt} - P_uQ_s\frac{ds}{dt} = Q_tP_u
$$

$$
P_uP_v\frac{du}{dt} + P_v^2\frac{dv}{dt} - P_vQ_s\frac{ds}{dt} = Q_tP_v
$$

$$
P_uQ_s\frac{du}{dt} + P_vQ_s\frac{dv}{dt} - Q_s^2\frac{ds}{dt} = Q_tQ_s
$$

Step4: 求解线性方程组，得:

$$
\frac{ds}{dt}=\frac{\begin{vmatrix}P_u\cdot P_u&P_v\cdot P_u&Q_t\cdot P_u\\\\
P_u\cdot P_v&P_v\cdot P_v&Q_t\cdot P_v\\\\
P_u\cdot Q_s&P_v\cdot Q_s&Q_t\cdot Q_s\end{vmatrix}}
{\begin{vmatrix}P_u\cdot P_u&P_v\cdot P_u&-Q_s\cdot P_u\\\\
P_u\cdot P_v&P_v\cdot P_v&-Q_s\cdot P_v\\\\
P_u\cdot Q_s&P_v\cdot Q_s&-Q_s\cdot Q_s\end{vmatrix}}
$$

Step5: 由于交线是闭合的，因此至少存在一个点满足:

$$\frac{ds}{dt}=0$$

Step6: 需要假设交线处处可导。对于不可导的情况，将他们从不可导的点分开，然后再求解。

Step7: 求解方程组：

$$
\begin{cases}P-Q=\bar0&3\textit{equations}\\\\
\begin{vmatrix}P_u\cdot P_u&P_v\cdot P_u&Q_t\cdot P_u\\\\
P_u\cdot P_v&P_v\cdot P_v&Q_t\cdot P_v\\\\
P_u\cdot Q_s&P_v\cdot Q_s&Q_t\cdot Q_s\end{vmatrix}=0\end{cases}
$$

Step8: 求解方程组，得到交线上的初始点。得到的交点需要判断是否在曲面内，且这个点所在的线也可能是非闭合的。

## 问题：

### 1. 如何求解线性方程组？

使用符号计算可求解。python代码为：
```python
import sympy
x1,x2,x3,a,b,c,A,B,C,D,E,F  = sympy.symbols('x1 x2 x3 a b c A B C D E F')# 声明符号变量
f1=A*x1+B*x2-C*x3-a
f2=B*x1+D*x2-E*x3-b
f3=C*x1+E*x2-F*x3-c
result = sympy.solve([f1, f2, f3],[x1, x2, x3])
print(result)
# result: {x1: (B*E*c - B*F*b - C*D*c + C*E*b + D*F*a - E**2*a)/(A*D*F - A*E**2 - B**2*F + 2*B*C*E - C**2*D), x2: (-A*E*c + A*F*b + B*C*c - B*F*a - C**2*b + C*E*a)/(A*D*F - A*E**2 - B**2*F + 2*B*C*E - C**2*D), x3: (-A*D*c + A*E*b + B**2*c - B*C*b - B*E*a + C*D*a)/(A*D*F - A*E**2 - B**2*F + 2*B*C*E - C**2*D)}
``` 

其中 $x3$ 对应 $\frac{ds}{dt}$。进行符号替换后，与贾宇的推文中的公式一致。

### 2. 为什么一定有一个点满足 $\frac{ds}{dt}=0$？

$\frac{ds}{dt}$ 可以这样理解：

把曲面 $Q(s, t)$ 参数域上的交线看作是一个参数方程，即 $s(t) = 0$。对于一个闭合的交线，$s(t)$ 是一个周期函数。由***微分中值定理***至少存在一个点满足 $\frac{ds}{dt}=0$。

**罗尔定理**：如果一个函数 $f(x)$ 在闭区间\[a, b\]上连续，在开区间(a, b)内可导，并且 $f(a) = f(b)$ ，那么存在一个点$c$在(a, b)内，使得$f'(c) = 0$。

对于周期函数，如果我们考虑一个完整的周期\[a, a+P\]（其中P是周期），则有$f(a) = f(a+P)$。如果这个周期函数在这个周期内连续并且可导，那么根据罗尔定理，至少存在一个点在这个周期内，其导数等于0。


# Topology-driven approximation to rational surface-surface intersection via interval algebraic topology analysis

> 本博客只关注其中对于极小环、孤立点的处理方法，即其中的 *Tangency case* $C_2$ - *Isolated tangent points and closed loops*，与贾宇的方法做对比。

## 基础定义：

对于两个NURBS曲面 $R_1(s, t)$ 和 $R_2(u, v)$，代数表示为：

$$
R_1(s, t)=(\frac{F_1(s, t)}{F_4(s, t)}, \frac{F_2(s, t)}{F_4(s, t)}, \frac{F_3(s, t)}{F_4(s, t)})
$$

$$
R_2(u, v)=(\frac{G_1(u, v)}{G_4(u, v)}, \frac{G_2(u, v)}{G_4(u, v)}, \frac{G_3(u, v)}{G_4(u, v)})
$$

$F_i$和$G_i$是最大公因式为1的多项式。两个曲面的交线表达为：

$$
\Psi(s, t, u, v) = (\frac{F_1(s, t)}{F_4(s, t)} - \frac{G_1(u, v)}{G_4(u, v)}, \frac{F_2(s, t)}{F_4(s, t)} - \frac{G_2(u, v)}{G_4(u, v)}, \frac{F_3(s, t)}{F_4(s, t)} - \frac{G_3(u, v)}{G_4(u, v)})
$$

$\Psi$ 也代表4D空间中的交线。

## Isolated tangent

孤立相切表示两个曲面$R_1$和$R_2$在某个点/线处相切，且这个点/线全部都是相切的。

### 基本思想：奇异点正则化（singularity regulation）

使用正则化方法中的 *deflation* 方法，将奇异点转化为非奇异点。这个方法的基本思想是：将一个系统的孤立多重根转化为另一个可能过定系统的单根。

对于切点而言，其在4D空间中的切线 $T_\psi = 0$。

### 公式说明

对于孤立相切点，其代数表达为：

$$
(\frac{\partial R_1}{\partial s}\times\frac{\partial R_1}{\partial t})_{(\mathrm{s},t)=\pi_1(\mathrm{p})}= 
$$

$$
\lambda(\frac{\partial R_2}{\partial u} \times \frac{\partial R_2}{\partial v})_{(u,v)
 = \pi_2(\mathrm{p})}\neq 0
$$

即四个向量$\frac{\partial R_1}{\partial s}$, $\frac{\partial R_1}{\partial t}$, $\frac{\partial R_2}{\partial u}$, $\frac{\partial R_2}{\partial v}$在某个点$\mathrm{p}$处共面。等价于$T_\psi = 0$。

而对于系统 $\Psi$，其具有四个变量，三个方程。通过再加入一个方程，以保证系统的正定，即为四个方程与四个变量的系统。

添加的方程可以有四个，表示为 $T_\psi^i(s, t, u, v)$。$T_\psi^i$为$T_\psi$在4D空间中的一个分量方程。

从顶向下的$T_\psi$与$T_\psi^i$计算方法可见论文第三章。

### 计算方法

为了方便计算，可以将 $\Psi$ 系统中一个方程替换为 $T_\psi^i$。这样的系统为四个方程三个变量。依然可以通过曲线追踪的方法加速求解。

# 两个方法的对比

两个方法的思路在于，都是对欠定系统添加一个方程，以保证系统的正定。经过推导，两个方法的**做法是一致的**。

即：当 $T_\psi^i = 0$ 时，也代表 $\frac{ds}{dt} = 0$ 或 $\frac{dt}{ds} = 0$。

# 附录

公众号：贾宇的研究手稿 - *Initial Point on Closed Intersection Curve*

![Initial Point on Closed Intersection Curve](/source/_data/pictures/20240327_NURBSIntersectInitalPoint/20240327092015.png)