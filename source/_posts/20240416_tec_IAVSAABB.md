---
title: NURBS 区间计算（IA & AA） 与控制点AABB的区间范围差别。
category: 技术博客
mathjax: true
password: 12317003
---

# 问题

在之前 Affine Arithmetic 的文章中，提到了区间计算 (IA) 与仿射计算 (AA)，方便起见都叫做 AA。而样条曲面使用控制点插入 + 计算 AABB 的方法，同样是输入一段参数区间，输出一个区间范围。因此本文将对比 AA 与控制点 AABB 的区间范围差别。

# 解题

由于曲面是张量积的形式，只需要对比曲线即可。而 B 样条曲线可以看作是 Bezier 曲线拼接而成，我们先对比最简单的 Bezier 曲线；Beizer 曲线 $x,y,z$ 坐标计算方法相同，仅需对比 $x$ 轴即可。

## Bezier 曲线上的对比

### 1 次 Bezier 曲线

当考虑 1 次Bezier 曲线时，其控制点为 $P_0, P_1$，参数为 $t \in [0, 1]$。容易证明节点插入的控制点 AABB 与区间计算的范围相同。

### 2 次 Bezier 曲线

当考虑 2 次 Bezier 曲线时，其控制点为 $P_0, P_1, P_2$，参数为 $t \in [0, 1]$。其表达式为

$$
B(t) = (1-t)^2 P_0 + 2(1-t)t P_1 + t^2 P_2
$$


首先考虑**特殊情况**：

t取 $[0, 1]$。则上述式子的 $t$ 与 $(1-t)$ 都在 $[0, 1]$ 区间内，因此即使 $P_0, P_1, P_2$ 不包括 0， $B(t)$ 的区间范围必定包括0。

而对于节点插入与控制点计算的 AABB，如果 $P_0, P_1, P_2$ 的 AABB 区间范围不包括 0，那么 $B(t)$ 的区间范围也不包括 0。

**即两者的区间范围不同，且某些情况下，AA 的区间范围更大，但不能确定是否存在某些情况下，AA 的区间范围更小。**

接下来对二次 Bezier 曲线的区间计算与控制点 AABB 的区间范围进行对比。

### AA

对于输入区间 $\hat{t} = [a, b]$，区间计算的最大值为：

$$
B_{max}(\hat{t}) = max[(1-t)^2 P_0] + 2max[(1-t)t P_1] + max[t^2 P_2]
$$

假设 $P_0, P_1, P_2 \geq 0$，则对于区间 $[0, 1]$，有：

$$
B \in [0, P_0 + 2P_1 + P_2]
$$

明显大于控制点的 AABB 区间范围。

对于输入区间 $t = [a, b]$，其区间计算的最大值为：

$$
B_{max}(\hat{t}) = max[(1-t)^2 P_0] + 2max[(1-t)t P_1] + max[t^2 P_2] \\ \\
B_{max}(\hat{t}) = (1-a)^2 P_0 + 2(1-a)b P_1 + b^2 P_2
$$



### AABB

在不进行节点插入的情况下，控制点的 AABB 区间范围为：

$$
AABB = [min(P_0, P_1, P_2), max(P_0, P_1, P_2)]
$$


而在节点插入后，对区间 $t = [a, b]$，其控制点为 $Q_0, Q_1, Q_2$，有：

$$
Q_0 = (1-a)P_0 + aP_1, \\
Q_1 = (1-a)(1-b)P_0 + (a+b-2ab)P_1 + abP_2, \\
Q_2 = (1-a)(1-b)P_1 + (a+b-ab)P_2
$$

分别对三个控制点的系数进行讨论：

$P_0$:  $0 < (1-a)(1-b) < (1-a)^2 < (1-a)$


$P_1$:  仅能保证 $2(1-a)b < a+b-2ab$，其他无法比较

$P_2$:  $ab < b^2 < a+b-ab$

即在区间 $t = [a, b]$ 的情况下，无法进行比较。

区间计算缺点：

1. 平移改变：改变控制点的位置，可能会导致区间长度的改变。

2. 不等参：例如对于 $ [\frac{1}{5}, \frac{2}{5}] \in [0, 1]$，区间计算的结果与 $ [2, 3] \in [1, 6]$ 的结果不同。而对于控制点 AABB，其结果相同。这在处理 B 样条曲线时，可能会导致问题。

3. 区间范围可能更大。

区间计算测试代码：
    
```python
class IntervalNumber:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  
  def __str__(self):
    return '[{0},{1}]'.format(self.a,self.b)

  def __add__(self,other):
    return _add(self,other)

  def __sub__(self,other):
    return _sub(self,other)

  def __mul__(self,other):
    return _mul(self,other)

  def __truediv__(self,other):
    return _truediv(self,other)

def _add(I,J):
  result = IntervalNumber(I.a+J.a,I.b+J.b)
  return result

def _sub(I,J):
  result = IntervalNumber(I.a - J.b, I.b-J.a)
  return result

def _mul(I,J):
  result = IntervalNumber(I.a*J.a,I.b*J.b)
  return result

def _truediv(I,J):
  result = IntervalNumber(I.a/J.b, I.b/J.a)
  return result

t = IntervalNumber(0, 1)
t_0 = IntervalNumber((t.a+t.b)/2, (t.a+t.b)/2)
t_1 = IntervalNumber((t.b-t.a)/2, (t.b-t.a)/2)
ep = IntervalNumber(-1, 1)

x = 1
y = 2
z = 3

P_0 = IntervalNumber(x, x)
P_1 = IntervalNumber(y, y)
P_2 = IntervalNumber(z, z)
N_1 = IntervalNumber(1, 1)
N_2 = IntervalNumber(2, 2)
B = (N_1-t)*(N_1-t)*P_0+N_2*(N_1-t)*t*P_1+t*t*P_2
print('B(t) =', B)

B = (N_1-(t_0+ep*t_1))*(N_1-(t_0+ep*t_1)) * \
    P_0+N_2*(N_1-(t_0+ep*t_1))*(t_0+ep*t_1)*P_1+(t_0+ep*t_1)*(t_0+ep*t_1)*P_2


print('B(t) =', B)
```