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
$$
$$
H_{v}=\frac{\partial}{\partial v}b^{m,n}(u,v)=n\sum_{i=0}^{m}\sum_{j=0}^{n-1}(b_{i,j+1}-b_{i,j})B_{i}^{m}(u)B_{j}^{n-1}(v).
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
\begin{aligned}N(u,v)&=H_u\times H_v=\begin{vmatrix}i&j&k\\\\ \partial_ux&\partial_uy&\partial_uz\\\\ \partial_vx&\partial_vy&\partial_vz\end{vmatrix}
\\
&=(\partial_uy\partial_vz-\partial_uz\partial_vy)i+(\partial_uz\partial_vx-\partial_ux\partial_vz)j+(\partial_ux\partial_vy-\partial_uy\partial_vx)k.\end{aligned}
$$

公式推导：

$$
m\sum_{i=0}^{m-1}\sum_{j=0}^{n}(b_{i+1,j}-b_{i,j})B_{i}^{m-1}(u)B_{j}^{n}(v),
$$

$$
n\sum_{i=0}^{m}\sum_{j=0}^{n-1}(b_{i,j+1}-b_{i,j})B_{i}^{m}(u)B_{j}^{n-1}(v).
$$

$$
N(u,v)=H_u \times H_v
\\\\=\left(m\sum_{i=0}^{m-1}\sum_{j=0}^{n}(b_{i+1,j}-b_{i,j})B_{i}^{m-1}(u)B_{j}^{n}(v)\right)\times\left(n\sum_{i=0}^{m}\sum_{j=0}^{n-1}(b_{i,j+1}-b_{i,j})B_{i}^{m}(u)B_{j}^{n-1}(v)\right)
$$

$$
=\begin{vmatrix}i&j&k\\\\ \frac{\partial}{\partial u}b^{m,n}(u,v)&\frac{\partial}{\partial u}b^{m,n}(u,v)&\frac{\partial}{\partial u}b^{m,n}(u,v)\\\\ \frac{\partial}{\partial v}b^{m,n}(u,v)&\frac{\partial}{\partial v}b^{m,n}(u,v)&\frac{\partial}{\partial v}b^{m,n}(u,v)\end{vmatrix}.
$$

$N(u,v)$ 可看做一条Bezier曲线，其控制点 $n_{ij}$ 为：


# HodoGraphs and normals of rational curves and surfaces

## 齐次坐标点之间的方向

定义齐次坐标点为 $P=[X,Y,Z,W]$, 其 Cartesian 坐标为 $\tilde{P}=[\frac{X}{W},\frac{Y}{W},\frac{Z}{W}]$。

定义方向

$$
Dir(P_1,P_2)=(W_1X_2-X_1W_2,W_1Y_2-Y_1W_2,W_1Z_2-Z_1W_2).
$$

注意 $Dir()$ 是对齐次坐标定义下的方向，与 Cartesian 坐标方向有所不同。尤其具有如下性质：

$$
Dir(P_1,P_2)=W_1W_2Dir(\tilde{P}_1,\tilde{P}_2)
$$
$$
Dir(kP_1,P_2)=Dir(P_1,kP_2)=kDir(P_1,P_2).
$$

## 有理 Bezier 曲线的 Hodograph

有理 Bezier 曲线 $P[t]$ 的定义为：

$$
P[t] = (X[t],Y[t],Z[t],W[t]) = \sum_{i=0}^{n}B_i^n(t)P_i.
$$
$$
B_i^n(t) = \binom{n}{i}t^i(1-t)^{n-i}.
$$

其 Hodograph 为：

$$
P'[t] = (X'[t],Y'[t],Z'[t],W'[t]) = \sum_{i=0}^{n-1}B_i^{n-1}(t)(P_{i+1}-P_i).
$$

在 Cartesian 坐标系下，有：

$$
\frac{d}{dt}\tilde{P}[t] = \frac{d}{dt}\left(\frac{X[t]}{W[t]},\frac{Y[t]}{W[t]},\frac{Z[t]}{W[t]}\right)
$$
$$
 = \frac{1}{(W[t])^{2}}(W[t]X^{\prime}[t]-W^{\prime}[t]X[t],W[t]Y^{\prime}[t]-W^{\prime}[t]Y[t],W[t]Z^{\prime}[t]-W^{\prime}[t]Z[t])
$$
$$
= \frac{Dir(P[t],P'[t])}{W[t]^2}.
 $$

 其中 $W[t]^2$ 是一个缩放函数，而 $Dir(P[t],P'[t])$ 给出了 Cartesian 坐标系下的导数方向。

 经过一系列推导（主要依赖其次坐标的分配率，将 Berstein 基展开）得到导数的表达式：

$$
\frac{d}{dt}\tilde{P}[t] = \frac{1}{W[t]^2}\sum_{k=0}^{2n-2}B_k^{2n-2}(t)\tilde{H_k}.
$$
where 

$$
\tilde{H_k}=\frac{1}{\binom{2n-2}k}\sum_{i=\max(0,k-n+1)}^{[k/2]}(k-2i+1)\binom ni \binom n{k-i+1} Dir(P_i,P_{k-i+1}).
$$

若不需要正确的大小，可以将 $W[t]^2$ 省略，得到**导数方向**为：

$$
\alpha\frac{d}{dt}\tilde{P}[t] = Dir(P[t],P'[t]) = \sum_{k=0}^{2n-2}B_k^{2n-2}(t)\tilde{H_k}.
$$

## 导数方向界

在上式 $\tilde{H_k}$ 中，每个 $Dir(P_i,P_{k-i+1})$ 的系数均为正，因此导数方向被一列向量 $Dir(P_a,P_b) (0\leq a < b\leq n)$ 的凸包所界定。即： 

$$
Dir(P_a,P_b) = W_aW_bDir(\tilde{P_a},\tilde{P_b})=W_aW_b\sum_{i=a}^{b-1}(\tilde{P}_{i+1}-\tilde{P}_i).
$$

经过推导，得到**有理 Bezier 曲线导数方向的凸包界定与多项式相同**，为 $\tilde{P}_{i+1}-\tilde{P}_i (i=0,\ldots,n-1)$ 的凸包。

## 导数大小界

我们推出导数的上界。首先定义：

$$
W_{\max} = \max_{0\leq i\leq n}W_i. 
$$
$$
W_{\min} = \min_{0\leq i\leq n}W_i. 
$$
$$
D_{\max} = \max_{0\leq i\leq n-1}||\tilde{P}_{i+1}-\tilde{P}_i||.
$$

显然，有：

$$
W_{\min}\leq W[t]\leq W_{\max},\quad \forall t\in[0,1].
$$

经过推导，得到导数的上界为：

$$
||\frac{d}{dt}\tilde{P}[t]||\leq \frac{nW^2_{\max}D_{\max}}{W^2_{\min}}\sum_{k=0}^{2n-2}B_k^{2n-2}(t)=\frac{nW^2_{\max}D_{\max}}{W^2_{\min}}.
$$

## 有理曲面

其推导过程与有理曲线类似。主要运用如下思想。曲面 $P[s,t]$ 可被表示为：

$$
P[s,t] = \sum_{i=0}^{m}B_i^m[s]Q_i[t]. 
$$
$$
Q_i[t] = \sum_{j=0}^{n}B_j^n[t]P_{ij}.
$$

其中 $P$ 可以看做一条关于 $s$ 的有理 Bezier 曲线，控制点为$Q_i[t]$。$Q$ 可以看做一条关于 $t$ 的有理 Bezier 曲线。

经过一系列推导，得到导数方向的表达式：

$$
\mathrm{Dir}(P[s,t],P_s[s,t])=\sum_{k=0}^{2m-2}\sum_{l=0}^{2n}B_k^{2m-2}[s]B_l^{2n}[t]\tilde{H_{k,l}}
$$

where
$$
\tilde{H_{k,l}}=\sum_{i=\max(0,k-m+1)}^{[k/2]}\sum_{j=\max(0,l-n)}^{\min(l,n)}(k-2i+1)\binom mi\binom m{k-i+1}\binom nj\binom n{l-j}
$$
$$
\times Dir(P_{i,j},P_{k-i+1,l-j})\left/\binom{2m-2}k\binom{2n}l.\right.
$$

### 导数方向界

尽管上式中推导出 hodograph 具有(2m-1)(2n-1)个控制点，但是导数方向的凸包界定可以由 $m(2n+1)$ 个向量的凸包界定。即：

$$
\sum_{j=\max(0,l-n)}^{\min(l,n)}\binom{n}{j}\binom{n}{l-j} Dir(P_{i,j},P_{i+1,l-j})
$$
$$
(i=0,1,\ldots,m-1; l=0,1,\ldots,2n).
$$

其中：$i$ 和 $l$ 为代入的值(见公式第2行，共有 $m(2n+1)$ 次计算) 。 $n$ 为曲面在 $t$ 方向的阶数, $P_{i,j}$ 为曲面的控制点。

### 导数大小界

$$
\left\|\frac{\partial}{\partial s}\tilde{P}[s,t]\right\|= \frac{m}{(W[s,t])^{2}}\Bigg\Vert\sum_{k=0}^{2m-2}(1-t)^{2m-2-k}t^{k} 
$$

$$
\times\sum_{\begin{array}{c}i+j=k+1 \\\\0\leqslant i\leqslant m-1 \\\\1\leqslant j \leqslant m\end{array}}\binom{m-1}i\binom{m-1}{j-1}\operatorname{Dir}(\boldsymbol{Q}_i[t],\boldsymbol{Q}_j[t])
\Bigg\Vert 
$$

$$
\leqslant \frac{mW_{\max}^{2}}{W_{\min}^{2}}\max_{0\leqslant i\leqslant m-1}\|\tilde{Q_{i+1}}[t]-\tilde{Q_{i}}[t]\|
$$

其中
$$
W_{\max}\equiv\max_{\begin{array}{c}0\leqslant i\leqslant m\\\\0\leqslant j\leqslant n\end{array}}W_{i,j},\\
W_{\min}\equiv\min_{\begin{array}{c}0\leqslant i\leqslant m\\\\0\leqslant j\leqslant n\end{array}}W_{i,j},
$$

最后得到上界：

$$
\left\|\frac{\partial}{\partial s}\tilde{P}[s,t]\right\|\leqslant\frac{mW_{\max}^{2}S_{\max}}{W_{\min}^{4}}.
$$

其中 $S_{\max}$ 为以下 $m(2n-1)$ 个向量的凸包的最大长度：

$$
\frac{1}{\binom{2n}{l}}\sum_{j=\max(0,l-n)}^{\min(l,n)}\binom{n}{j}\binom{n}{l-j}Dir(P_{i,j},P_{i+1,l-j})
$$
$$
(i=0,1,\ldots,m-1; l=0,1,\ldots,2n) ,
$$

### 法向方向

单靠导数的叉乘，法向方向的阶数为 $(4m-2)\times(4n-2)$，但是本文证明了法向方向的阶数可以降为 $(3m-2)\times(3n-2)$。

首先定义其次坐标下的法向方向：

$$
Nrm(P_{1},P_{2},P_{3})\equiv\left(\left|\begin{array}{ccc}Y_{1}&Y_{2}&Y_{3}\\\Z_{1}&Z_{2}&Z_{3}\\\W_{1}&W_{2}&W_{3}\end{array}\right|,\left|\begin{array}{ccc}Z_{1}&Z_{2}&Z_{3}\\\X_{1}&X_{2}&X_{3}\\\W_{1}&W_{2}&W_{3}\end{array}\right|,\left|\begin{array}{ccc}X_{1}&X_{2}&X_{3}\\\Y_{1}&Y_{2}&Y_{3}\\\W_{1}&W_{2}&W_{3}\end{array}\right|\right)
$$

其有几个特殊性质：

$$
\operatorname{Nrm}(kP_{1},P_{2},P_{3})=\operatorname{Nrm}(P_{1},kP_{2},P_{3})=\operatorname{Nrm}(P_{1},P_{2},kP_{3})=k\operatorname{Nrm}(P_{1},P_{2},P_{3})\\
$$

$$
\mathsf{Nrm}(P_{1}+P_{2},P_{3},P_{4})=\mathsf{Nrm}(P_{1},P_{3},P_{4})+\mathsf{Nrm}(P_{2},P_{3},P_{4})
$$
$$
\mathsf{Nrm}(P_{1},P_{2}+P_{3},P_{4})=\mathsf{Nrm}(P_{1},P_{2},P_{4})+\mathsf{Nrm}(P_{1},P_{3},P_{4})
$$
$$
Nrm( P_{1}, P_{2}, P_{3}+ P_{4}) =Nrm( P_{1}, P_{2}, P_{3}) +Nrm( P_{1}, P_{2}, P_{4})
$$

而在 $P[s,t]$ 处的法向方向为：

$$
Nrm(P[s,t],P_s[s,t],P_t[s,t])
$$

为方便计算，我们定义 $S_{ij}$ 为：

$$
S_{00}\equiv\sum_{i=0}^{m-1}\sum_{j=0}^{n-1}B_{i}^{n-1}[s]B_{j}^{n-1}[t]P_{i,j},\quad S_{01}\equiv\sum_{i=0}^{m-1}\sum_{j=1}^{n}B_{i}^{m-1}[s]B_{j-1}^{n-1}[t]P_{i,j}
$$
$$
S_{10}\equiv\sum_{i=1}^{m}\sum_{j=0}^{n-1}B_{i-1}^{m-1}[s]B_{j}^{n-1}[t]P_{i,j},\quad S_{11}\equiv\sum_{i=1}^{m}\sum_{j=1}^{n}B_{i-1}^{m-1}[s]B_{j-1}^{n-1}[t]P_{i,j}.
$$

则 $P, P_s, P_t$ 可以使用 $S_{ij}$ 表示：

$$
P[s,t] =(1-s)(1-t) S_{00}+s(1-t) S_{10}+(1-s)t S_{01}+st S_{11}
$$

$$
P_{s}[s,t] =m\sum_{i=0}^{m-1}\sum_{j=0}^nB_i^{m-1}\left[s\right]B_j^n[t]\left(P_{i+1,j}-P_{i,j}\right)
$$

$$
=m[(1-t)S_{10}+tS_{11}-(1-t)S_{00}-tS_{01}],
$$

$$
P_{t}[s,t] =n\sum_{i=0}^m\sum_{j=0}^{n-1}B_i^m[s]B_j^{n-1}[t] (P_{i,j+1}-P_{i,j})
$$

$$
=n[(1-s)S_{01}+sS_{11}-(1-s)S_{00}-sS_{10}]
$$

经过一系列推导，得到法向方向的表达式：

$$
Nrm(P[s,t],P_s[s,t],P_t[s,t])
$$
$$
=mn[(1-s)(1-t)Nrm(S_{00},S_{10},S_{01})+s(1-t)Nrm(S_{00},S_{10},S_{11})
$$
$$
+(1-s)tNrm(S_{00},S_{11},S_{01})+stNrm(S_{10},S_{11},S_{01})].
$$

### 法向方向界

有两种方法计算法向范围：

1. 使用 Sederberg 和 Meyers 的方法，先计算导数的方向锥，然后使用叉乘计算法向锥。需要计算 $m(2n-1)+n(2m-1)$ 个向量。

2. 使用本文的方法，直接计算法向锥的控制点。

作者指出，尽管第二种方法能够给出更紧的界，但是计算量更大。因此，作者建议使用第一种方法。

# Loop detection in surface patch intersections

仅关注论文中有关曲面法向锥的部分。

首先计算曲面 $P[s,t]$ 的方向锥 $\mathscr{T}_{s}$ 和 $\mathscr{T}_{t}$，法向锥的轴为两方向锥的叉乘。法向锥的半角为：

$$
\theta_\perp=\sin^{-1}\left(\frac{\sqrt{\sin^2\theta_s+2\sin\theta_s\sin\theta_t\cos\beta+\sin^2\theta_t}}{\sin\beta}\right)
$$