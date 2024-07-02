---
title: Eigen库使用说明
category: 技术博客
date: 2024-03-14
---

# Eigen库简介

Eigen是一个C++模板库，提供了线性代数的基本功能，包括矩阵、向量、矩阵分解、求解线性方程组等。Eigen库的特点是头文件实现，不需要编译，只需要包含头文件即可使用。Eigen库的使用方法和MATLAB、Python中的numpy库类似，可以方便地进行矩阵运算。

Eigen可以使用Intel MKL、OpenBLAS等高性能库进行加速，也可以使用CUDA进行GPU加速。

Eigen遵循MPL2协议，可以免费用于商业用途。

# 在项目中使用Eigen库

## 下载Eigen库

Eigen库的官网是：[http://eigen.tuxfamily.org/](http://eigen.tuxfamily.org/)。目前最新版本是3.4.0。下载对应的zip文件，解压。

## 将Eigen库添加到项目中

遵循Eigen文件中INSTALL文件的说明，将Eigen库的```Eigen/```文件夹添加到项目的```3rdfiles/Eigen```路径中。

{% note  %}
若需要```unsupported/```，也需要将```unsupported/```文件夹拷贝到项目的```3rdfiles/Eigen```目录下。
{% endnote %}

## 在项目中使用Eigen库

在项目的CMakeLists.txt文件中，添加如下代码：

```cmake
#...
include_directories(
    #...
    ${PROJECT_SOURCE_DIR}/3rdfiles/Eigen
    #...
)
#...
```