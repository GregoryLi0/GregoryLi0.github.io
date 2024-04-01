---
title: 左值右值与智能指针
category: 技术博客
mathjax: true
---

>**参考资料：**
>[1] [microsoft 智能指针（现代 C++）](https://learn.microsoft.com/zh-cn/cpp/cpp/smart-pointers-modern-cpp?view=msvc-170)
>[2] [现代 C++：一文读懂智能指针](https://zhuanlan.zhihu.com/p/150555165)
>[3] [一文读懂C++右值引用和std::move](https://zhuanlan.zhihu.com/p/150555165)


在现代 C++ 编程中，标准库包含智能指针，该指针用于确保程序不存在内存和资源泄漏且是异常安全的。而要理解智能指针中的 `move-only` 的概念，需要先了解左值和右值的概念。

# 左值、右值、左值引用和右值引用

## 左值与右值 lvalue and rvalue

简单来说:

- 可取地址$\rightarrow$左值，不可取地址$\rightarrow$右值。

- 可以被赋值$\rightarrow$左值，不能被赋值$\rightarrow$右值。

- 位于等号左边$\rightarrow$左值，位于等号右边$\rightarrow$**不确定！**

```cpp
int a = 5;  // a是左值，5是右值
int b = a;  // a,b都是左值

// class A{};
A a = A(); // a是左值，A()是右值
```


## 左值引用与右值引用

引用本质是别名，可以通过引用修改变量的值，传参时传引用可以避免拷贝，其实现原理和指针类似。个人认为，引用出现的本意是为了降低C语言指针的使用难度，但现在指针+左右值引用共同存在，反而大大增加了学习和理解成本。

### 左值引用

能指向左值，不能指向右值的就是左值引用。原因是由于右值没有地址，没法被修改，所以左值引用无法指向右值。一个例外是，const左值引用是可以指向右值的：

```cpp
int a = 5;
int &ref_a = a; // 左值引用指向左值，编译通过
int &ref_a = 5; // 左值引用指向了右值，会编译失败
const int &ref_a = 5;  // 编译通过
```

const左值引用不会修改指向值，因此可以指向右值，这也是为什么要使用const &作为函数参数的原因之一，如`std::vector`的`push_back`：
    
```cpp
void push_back(const value_type& val);
```

如果没有const，vec.push_back(5)这样的代码就无法编译通过了。

### 右值引用

右值引用的标志是&&，可以指向右值，不能指向左值。右值引用的用途是可以修改右值，如下：

```cpp
int a = 5;
int &&ref_a_left = a; // 编译不过，右值引用不可以指向左值
ref_a_right = 6; // 右值引用的用途：可以修改右值
```

## 左值右值引用的本质讨论

### 右值引用有办法指向左值吗？

可以的，使用 `std::move`

`std::move` 本质上是一个类型转换函数，将左值转换为右值引用。并不会真正移动数据。它可以实现**移动语义，避免拷贝，从而提升程序性能。**

```cpp
int a = 5; // a是个左值
int &ref_a_left = a; // 左值引用指向左值
int &&ref_a_right = std::move(a); // 通过std::move将左值转化为右值，可以被右值引用指向
cout << a; // 打印结果：5
```

### 左值引用、右值引用本身是左值还是右值？

**被声明出来的左、右值引用都是左值。作为函数返回值的 && 是右值。** 

1. 从性能上讲，左右值引用没有区别，传参使用左右值引用都可以避免拷贝。

2. 右值引用可以直接指向右值，也可以通过std::move指向左值；而左值引用只能指向左值(const左值引用也能指向右值)。

3. 作为函数形参时，右值引用更灵活。虽然const左值引用也可以做到左右值都接受，但它无法修改，有一定局限性。

## 小结

引入右值引用，就是为了移动语义。移动语义就是为了减少拷贝。`std::move` 就是将左值转为右值引用。这样就可以重载到移动构造函数了，移动构造函数将指针赋值一下就好了，不用深拷贝了，提高性能。

## std::forward

`std::forward` 用于完美转发，将左值引用转换为左值引用，右值引用转换为右值引用。

与move相比，forward更强大，move只能转出来右值，forward都可以。

> *`std::forward<T>(u)`* 有两个参数：`T` 与 `u`。
> 1. 当T为左值引用类型时，u将被转换为T类型的左值；
> 2. 否则u将被转换为T类型右值。

# 智能指针 Smart Pointers

C++11 引入了 3 个智能指针类型：

- `std::unique_ptr<T> `：独占资源所有权的指针。
- `std::shared_ptr<T> `：共享资源所有权的指针。
- `std::weak_ptr<T> `：共享资源的观察者，需要和`std::shared_ptr` 一起使用，不影响资源的生命周期。

## std::unique_ptr

`std::unique_ptr` 是一个独占所有权的智能指针，它是一个轻量级的智能指针，不需要额外的开销。`std::unique_ptr` 是 move-only 的。

```cpp
// 传统指针
{
    int* p = new int(100);
    // ...
    delete p;  // 要记得释放内存
}

// 使用 std::unique_ptr
{
    std::unique_ptr<int> p(new int(100));
    // ...
}  // 离开作用域时，自动释放内存
```

`std::unique_ptr` 是 move-only 的，不能被复制，只能通过移动语义来传递所有权。
```cpp
{
    std::unique_ptr<int> uptr = std::make_unique<int>(200);
    std::unique_ptr<int> uptr1 = uptr;  // 编译错误，std::unique_ptr<T> 是 move-only 的

    std::unique_ptr<int> uptr2 = std::move(uptr); // 正确，uptr 的所有权被转移给 uptr2
    assert(uptr == nullptr); // true, uptr 已经被移动
}
```

## std::shared_ptr

`std::shared_ptr` 其实就是对资源做引用计数——当引用计数为 0 的时候，自动释放资源。

```cpp
{
    std::shared_ptr<int> sptr = std::make_shared<int>(200);
    assert(sptr.use_count() == 1);  // 此时引用计数为 1
    {   
        std::shared_ptr<int> sptr1 = sptr;
        assert(sptr.get() == sptr1.get());
        assert(sptr.use_count() == 2);   // sptr 和 sptr1 共享资源，引用计数为 2
    }   
    assert(sptr.use_count() == 1);   // sptr1 已经释放
}
// use_count 为 0 时自动释放内存
```

### 实现原理

`std::shared_ptr` 的实现原理是引用计数。`std::shared_ptr` 需要维护的信息有两部分：

- 指向共享资源的指针
- 引用计数等共享资源的控制信息——实现上是维护一个指向控制信息的指针。

即 `std::shared_ptr` 具有两个指针，一个指向资源，一个指向控制信息。

**创建 `std::shared_ptr`**

```cpp
std::shared_ptr<int> sptr = std::make_shared<int>(200);
// 或者
std::shared_ptr<int> sptr(new int(200));
```

![创建shared_ptr](images/20240327_tec_smartPtr/createSharePtr.png)

**拷贝 `std::shared_ptr`**

```cpp
std::shared_ptr<int> sptr1 = sptr;
```

![拷贝shared_ptr](images/20240327_tec_smartPtr/copySharePtr.png)

其中控制信息也保存了对共享资源的指针，这个指针和 `shared_ptr` 指向的资源指针地址一样，但类型可能不同。

![继承关系的shared_ptr](images/20240327_tec_smartPtr/multiClassPtr.png)

## std::weak_ptr

`std::weak_ptr` 是 `std::shared_ptr` 的观察者，它不会增加引用计数，也不会影响资源的生命周期。

- 如果需要访问 `std::shared_ptr` 指向的资源，可以将 `std::weak_ptr` 转换为 `std::shared_ptr`。
- 当 `std::shared_ptr` 被释放后，`std::weak_ptr` 会自动变为 `nullptr`。

```cpp
{
    std::shared_ptr<int> sptr = std::make_shared<int>(200);
    std::weak_ptr<int> wptr = sptr;
    assert(wptr.use_count() == 1);  // 引用计数为 1
    {
        std::shared_ptr<int> sptr1 = wptr.lock(); // 将 wptr 转换为 shared_ptr sptr1
        assert(sptr1.use_count() == 2);  // 引用计数为 2
    }
    assert(wptr.use_count() == 1);  // sptr1 已经释放
    sptr.reset();  // 释放资源
    assert(wptr.use_count() == 0);  // 引用计数为 0
}
```

![创建weak_ptr](images/20240327_tec_smartPtr/createWeakPtr.png)

当 shared_ptr 析构并释放共享资源的时候，只要 weak_ptr 对象还存在，控制块就会保留，weak_ptr 可以通过控制块观察到对象是否存活。

![删除shared_ptr后的weak_ptr](images/20240327_tec_smartPtr/deleteSharedPtrForWeakPtr.png)

## 小结

- 当资源是被独占时，使用 std::unique_ptr 对资源进行管理。
- 当资源会被共享时，使用 std::shared_ptr 对资源进行管理。
- 使用 std::weak_ptr 作为 std::shared_ptr 管理对象的观察者。

C++是真的麻烦！