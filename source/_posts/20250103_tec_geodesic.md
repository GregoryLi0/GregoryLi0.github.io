---
title: 曲面测地距离
category: 技术博客
mathjax: true
password: 12317003
---

参数曲面上的测地线是曲面上的一条曲线，其长度是曲面上的最短路径。

## 测地线

当且仅当曲面上的曲线满足如下条件时，称其为测地线：

***在曲线上的任意一点，曲线的法向与曲面的法向平行***

也可以描述为测地线是一条测地曲率为0的曲线。

曲线的法向可以通过曲线的切向和曲率来计算。


## 现有方法

大致分为两类：解析和数值。

## 算法原理

$C$ : curve on parametric space of $S$

$Q_0$ : start point on $C$ in $R^3$

$T_0$ : tangent vector at $Q_0$

$C'$ : curve on $S$ in $R^3$

$L_0$ : pull $T_0$ to paramter space

$q_1$ : a point in the neighborhood of $q_0$ on $C'$, which can be approximated by:

$(u_1,v_1) = (u_0 + u'(q_0)\Delta s, v_0 + v'(q_0)\Delta s)$

where $\Delta s$ is arch length increment.

the unit tangent vector at $Q_1=r(u_1,v_1)$ can be approximated by:

$T_1 = T_0 + k_0 \beta_0 \Delta s$

where $T_1$ is the unit tangent vector of $C$ at $Q_1$, $k_0$ is the curvature of $C$ at $Q_0$, $\beta_0$ is the principal normal of $C$ at $Q_0$.

## 算法流程

输入：曲面$S$，起始点$Q_0$，切向量$T_0$

1. 将$T_0$投影到参数空间，得到参数空间上$C'$在$q_0$的行进方向$L_0$

2. 进行行进，得到$q_1$

3. 计算曲面$S$在$Q_0$和$Q_1$的单位法向量$n_0$和$n_1$

4. 使用一些公式计算在$Q_1$的切向量$T_1$

5. 使用$q_1$和$T_1$作为新的起始点和切向量，重复1-4步

