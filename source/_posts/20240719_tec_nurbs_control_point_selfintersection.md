---
title: NURBS 自交曲面的控制点的充分条件
category: 技术博客
mathjax: true
password: 12317003
---

朱老师的文章给出了可变权重下的 NURBS 自交曲面的控制点的充分必要条件。这篇博客先研读分析朱老师的文章，然后给出快速的充分条件。

# Injectivity conditions of rational Bézier surfaces

## Preknowledge

### degree elevation

升阶算法会插入新的节点和控制点，且不断进行升阶，控制点的极限是曲面本身。

***定义***

$A_(m,n)={(i,j), i=0,1,...m; j=0,1,...n}$ 其中 $m,n$ 是正整数，$A_(m,n)$ 是整数点矩阵。 $\Delta_{A_{m,n}}$ 是 $A_{m,n}$ 的AABB，具有四个顶点和四条边。


# Well-posed 算法逻辑

```
算法：判断控制点是否Well-posed
输入：控制点矩阵P
输出：bool值

1. 对所有任意四个控制点：
2.   判断控制点连线是否与其他控制点连线相交。若相交，返回 false。
3.   对所有其他i，j满足条件1的控制点Pi,j：
4.     计算控制点Pi,j的重心坐标。
5.     判断Pi,j的重心坐标是否在Pi,j的凸包内。若在，返回 false。
6. 返回 true。
```