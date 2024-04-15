---
title: Injectivity conditions of rational Bézier surfaces 阅读
category: 论文阅读
mathjax: true
---

>发表期刊：Computers & Graphics \
>团队：大工数学院朱春钢老师

重点：有理 Bézier 曲面在权重可变情况下的单射性（自交）条件。

# Preknowledge

## degree elevation algorithm

- 有理 Bézier 曲面的 degree elevation 算法是通过增加节点数来增加曲面的次数，从而提高曲面的精度。

$m\times n$ 次有理 Bézier 曲面可以表示为：

$$
\mathbf{R}(u,v)=\frac{\sum_{i\operatorname{=}0}^m\sum_{j\operatorname{=}0}^n\omega_{i,j}\mathbf{P}_{i,j}B_i^m(u)B_j^n(v)}{\sum_{i\operatorname{=}0}^m\sum_{j\operatorname{=}0}^n\omega_{i,j}B_i^m(u)B_j^n(v)}
$$

通过 degree elevation 算法，可以得到 $(m+1)\times (n+1)$ 次有理 Bézier 曲面：

$$
\mathbf{R}^*(u,v)=\frac{\sum_{i\operatorname{=}0}^{m+1}\sum_{j\operatorname{=}0}^{n+1}\omega^*_{i,j}\mathbf{P}^*_{i,j}B_i^{m+1}(u)B_j^{n+1}(v)}{\sum_{i\operatorname{=}0}^{m+1}\sum_{j\operatorname{=}0}^{n+1}\omega^*_{i,j}B_i^{m+1}(u)B_j^{n+1}(v)}
$$

其中：

$$
\begin{aligned}\omega_{i,j}^{*}&=\alpha_{i}\beta_{j}\omega_{i-1,j-1}+\alpha_{i}(1-\beta_{j})\omega_{i-1,j}\\&+(1-\alpha_{i})\beta_{j}\omega_{i,j-1}+(1-\alpha_{i})(1-\beta_{j})\omega_{i,j}\end{aligned}
$$

$$
\begin{aligned}\mathbf{P}_{i,j}^{*}&=(\alpha_{i}\beta_{j}\mathbf{P}_{i-1,j-1}+\alpha_{i}(1-\beta_{j})\mathbf{P}_{i-1,j}\\&+(1-\alpha_{i})\beta_{j}\mathbf{P}_{i,j-1}+(1-\alpha_{i})(1-\beta_{j})\mathbf{P}_{i,j})/\omega_{i,j}^{*}\end{aligned}
$$

$$
\begin{aligned}\alpha_{i}&=\frac{i}{m+1}, \quad \beta_{j}=\frac{j}{n+1}\end{aligned}

当不断通过 degree elevation 算法提高曲面次数时，得到的曲面会逼近原曲面。