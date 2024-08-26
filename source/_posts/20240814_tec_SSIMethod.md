---
title: 曲面求交技术 - marhcing method
category: 技术博客
mathjax: true
password: 12317003
---

本博客总结曲面求交技术中的 marching method。

# 寻找初始交点

## 细分法

*Marching along a regular surface/surface intersection with circular steps* 

1. 通过 BVH 方法得到一个可能相交的区域。区域中点为参数的 (u,v), (s,t)，三维空间的 P。

2. 计算曲面 $S(u,v)$ 和 $T(s,t)$ 的与区域中点最近的点。计算方法为：

$$
[u_{i+1}-u_i]=[J^\mathrm{T}J]^{-1}J^\mathrm{T}[P-S_1(u_i,v_i)].
$$

其中 $J$ 为 Jacobian 矩阵。P 为区域三维空间的中点。

**TODO**：记得有一篇优化该点的论文，通过再构建三个平面的交点。

### 寻找 branch point

marching method 的终止条件是：

1. 遇到该分支的起点(闭合交线)；
2. 遇到曲面边界；
3. 遇到另一条交线(分支点)。

分支点往往是两曲面相切的点。切点/分支点可以


# 确定 marching 方向

## osculating circle 近似法

论文 *Marching along a regular surface/surface intersection with circular steps* 使用该方法确定 marching 方向，**但步长是预先给定的**。

![创建shared_ptr](images/20240814_tec_SSIMethod/circular_step.png)

1. circle 中心 C

    中心由三个平面交点给定：Q 与 Q 在曲线上的导数确定一个平面；P 与 P 在曲线上的导数确定一个平面；P，Q 和两者导数叉乘方向确定一个平面。

2. circle 半径

    半径为 C 到 Q 的距离。

3. 计算下一个迭代点

    ***预先给定一个步长 L。***

    a. 使用 $n$ 表示圆平面法向，计算平移矩阵、旋转矩阵，使圆的中心在原点 O，圆平面与 $z=0$ 重合。

    b. 确定 P-Q 为顺时针还是逆时针。

    c. 计算 $A'$。$A'$ 

    d. 应用逆变换，得到 $A$。

    e. 通过牛顿迭代得到更精确的交点。

## 交线切向法

*Marching along a regular surface/surface intersection with circular steps* 

如果两个曲面的切平面是不平行的，则

1. 迭代方向可以由两平面法向的叉乘给定。

2. 改进的方法，减少运算次数。

    $$
    V=S_t-\frac{S_t\cdot n}{S_s\cdot n}S_s
    $$

    其中 $S_s$ 和 $S_t$ 分别是曲面 $S(u,v)$ 对 $s$ 和 $t$ 的偏导数。

# 迭代步长

## 曲率近似法

*Marching along a regular surface/surface intersection with circular steps*

在一个点 P，想要在不计算二阶导数的情况下，得到曲线的曲率半径。先在小距离内取两个点，并将这两个点重新约束到交线上，用 Q 和 R 表示。则曲率半径为：

$$
\rho=\frac{\mid a\mid\mid b\mid\mid a-b\mid}{2\mid a\times b\mid}
$$

步长为：

$$
L=\rho\Delta\theta
$$

其中 $\Delta\theta$ 为给定的角度容差。若步长过大，则使用 CRT 作为步长（Barnhill et al. ‘87 的内容）。

# SISL 曲面求交算法

## 寻找SSI拓扑

*8.3.7 s1859*

输入：两个曲面 $S(u,v)$ 和 $T(s,t)$。

输出：单独交点、交线数目、交线上的一些点。

对曲面进行细分，直到两个BVH节点满足如下条件：

1. 两曲面包围体不相交；

2. 简单情况，满足：

    - 两曲面包围体相交；

    - 两曲面法向锥不重合。

## s1310 理解

epsge: 几何分辨率
maxstep: 最大步长

```cpp
// 作用: 追踪交点
//输入
```
