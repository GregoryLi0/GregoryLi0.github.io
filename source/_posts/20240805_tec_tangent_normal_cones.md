---
title: NURBS 切向量/法向锥
category: 技术博客
mathjax: true
password: 12317003
---

对论文 *Tangent, normal, and visibility cones on Bezier surfaces - 1995 CAGD* 与论文 *Hodographs and normals of rational curves and surfaces - 1995 CAGD* 的研究。

**符号说明**：

- $b^n(t)$: Bezier 曲线，n 阶的Bezier曲线。

- $b^{m,n}(u,v)$: Bezier 曲面，$m\times n$ 阶的Bezier曲面。

- $\mathscr{T}_{u}$: 曲面 $b^{m,n}(u,v)$ 对 $u$ 方向的切向锥。

- $\mathscr{T}_{v}$: 曲面 $b^{m,n}(u,v)$ 对 $v$ 方向的切向锥。

- $\mathscr{N}_{u}$: 曲面 $b^{m,n}(u,v)$ 对 $u$ 方向的法向锥。

- $H$: Hodograph, 曲线/曲面的切向量。

- $H_t$：曲线的切向量。

- $H_u$：曲面对u方向的切向量。

- $H_v$：曲面对v方向的切向量。

# Hodograph

HodoGraph 是曲线/曲面的切向量。即对曲线而言：

$$
H_t=\frac{\mathrm{d}}{\mathrm{d}t}b^n(t)=n\sum_{i=0}^{n-1}(b_{i+1}-b_i)B_i^{n-1}.
$$

得到的 $H_t$ 是曲线的切向量表达式，他也可看做一条Bezier曲线。此Bezier曲线的控制点 $h_t$ 为：

$$
h_i=n(b_{i+1}-b_i),\quad i=0,\ldots,n-1.
$$

***条件***： 有些特殊情况需要额外考虑：1. 曲线拥有拐点(inflection point)；2. 曲面有尖点(cusp)。需要在这些点处做分割（Kim,1993）。

同理，对曲面而言，有：

$$
H_{u}=\frac{\partial}{\partial u}b^{m,n}(u,v)=m\sum_{i=0}^{m-1}\sum_{j=0}^{n}(b_{i+1,j}-b_{i,j})B_{i}^{m-1}(u)B_{j}^{n}(v),
\\H_{v}=\frac{\partial}{\partial v}b^{m,n}(u,v)=n\sum_{i=0}^{m}\sum_{j=0}^{n-1}(b_{i,j+1}-b_{i,j})B_{i}^{m}(u)B_{j}^{n-1}(v).
$$

$H_u$ 和 $H_v$ 可看做两张Bezier曲面，分别为 $(m-1)\times n$ 和 $m\times(n-1)$ 次的Bezier曲面。$H_u$ 的控制点 $h_{ij}$ 为：

$$
h_{ij}=m(b_{i+1,j}-b_{i,j}),\quad i=0,\ldots,m-1,\quad j=0,\ldots,n.
$$

$H_v$ 的控制点可类似得到。

# 切向锥

定义 $CH(h_{ij})$ 为 $H_u$ 的控制点 $h_{ij}$ 的凸包，$CH(h_{ij}, O)$ 为 $h_{ij}$ 和原点 $O$ 的凸包。则 Beizer 曲面的凸包性可以描述为：

$$
b^{m,n}(u,v)\subseteq\mathrm{CH}(b_{ij}).
$$

其中 $b^{m,n}(u,v)$ 为原曲面方程，$b_{ij}$ 为原曲面的控制点。

该理论可推广至 $H_u$。

$$
H_u\subseteq\mathrm{CH}(h_{ij})\subseteq\mathrm{CH}(h_{ij},O).
$$

# 法向锥

曲面的法向 $N(u,v)$ 定义为：

$$
\begin{aligned}N(u,v)&=H_u\times H_v=\begin{vmatrix}i&j&k\\\partial_ux&\partial_uy&\partial_uz\\\partial_vx&\partial_vy&\partial_vz\end{vmatrix}\\&=(\partial_uy\partial_vz-\partial_uz\partial_vy)i+(\partial_uz\partial_vx-\partial_ux\partial_vz)j+(\partial_ux\partial_vy-\partial_uy\partial_vx)k.\end{aligned}
$$

公式推导：

$$
m\sum_{i=0}^{m-1}\sum_{j=0}^{n}(b_{i+1,j}-b_{i,j})B_{i}^{m-1}(u)B_{j}^{n}(v),
\\

n\sum_{i=0}^{m}\sum_{j=0}^{n-1}(b_{i,j+1}-b_{i,j})B_{i}^{m}(u)B_{j}^{n-1}(v).
$$

$$
\begin{aligned}N(u,v)&=H_u\times H_v
 


\\&=\left(m\sum_{i=0}^{m-1}\sum_{j=0}^{n}(b_{i+1,j}-b_{i,j})B_{i}^{m-1}(u)B_{j}^{n}(v)\right)\times\left(n\sum_{i=0}^{m}\sum_{j=0}^{n-1}(b_{i,j+1}-b_{i,j})B_{i}^{m}(u)B_{j}^{n-1}(v)\right)

\\&=\begin{vmatrix}i&j&k\\\frac{\partial}{\partial u}b^{m,n}(u,v)&\frac{\partial}{\partial u}b^{m,n}(u,v)&\frac{\partial}{\partial u}b^{m,n}(u,v)
\\\frac{\partial}{\partial v}b^{m,n}(u,v)&\frac{\partial}{\partial v}b^{m,n}(u,v)&\frac{\partial}{\partial v}b^{m,n}(u,v)\end{vmatrix}.\end{aligned}
$$

$N(u,v)$ 可看做一条Bezier曲面，其控制点 $n_{ij}$ 为：