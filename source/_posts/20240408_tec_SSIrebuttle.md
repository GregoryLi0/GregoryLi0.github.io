---
title: A Robust and Fast Surface-Surface Intersection Algorithm for NURBS Rebuttal 分析
category: 技术博客
mathjax: true
password: 12317003
date: 2024-04-08
---

# Reviews

## Reviewer 1

创新点不够明显，仅添加 BVH，其他理论与 SIGGRAPH 2023 论文相同。且论文许多算法细节丢失，无法重现。例如：

1. 说明控制点的作用
2. 如何结合代数系统与基函数？
3. 如何进行 C-S 计算？
4. 如何计算小环与孤立点？

## Reviewer 2

1. 是否可以边计算 BVH 边判断？以减少计算时间。

2. SIGGRAPH 2023 论文的技术可以在任意 BVH level 使用。level 深度与效率有什么关系？有什么停止条件？

3. C-S 如何计算？4D 边界与 edge 混用表述不清楚。

4. 如何算 Lipschitz 系数？

使用方法：

    - 细分法， OBB 对角线距离小于 Lipschitz 约束 $\epsilon$，则停止细分。

    - 追踪法，步长小于 $\epsilon$

5. 一些表述单词错误。**rebuttle 原文给出了详细清单**


## Reviewer 3

1. 把所有测试用例图转成一个表格。

2. 一些说明问题，**rebuttle 原文给出了详细清单**

3. Quad-Tree 与 4-way BVHs or BVH4 表述问题。

## Reviewer 4

1. 一些未参考文献

2. introduction 中说当 degree 提升，速度变慢。但代数系统同样效率变慢。如何证明方法好？

3. 4D、3D、2D 的转换太乱

4. C-S、小环、孤立点计算不清楚

5. 与其他方法的对比不可控变量太多。统一标准

## Reviewer 5

1. 创新点不够

# 提升内容

1. 详细说明每一步技术细节

2. 实现使用 Lipschitz 约束

3. 实现 RMS 误差计算

4. 修改表述错误等

5. 减少 SIGGRAPH 2023 论文的影响

6. 详细表述 4D、3D、2D 等