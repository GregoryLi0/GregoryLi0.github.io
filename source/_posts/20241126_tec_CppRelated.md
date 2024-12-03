---
title: Cpp相关技巧
category: 技术博客
mathjax: true
---

本文列举一些工程项目中学到的C++相关技巧。

# 1. Cmake 设置测试目录

例如有如下项目结构：

```
project/
│   CMakeLists.txt
│   tests/
│   └── CMakeLists.txt
│   └── test1.cpp
│   data/
│   └── data1.txt
```

则可以在`project/CMakeLists.txt`中设置测试目录：

```cmake
# ...
set(DATA_DIR ${CMAKE_SOURCE_DIR}/data)

add_subdirectory(tests)
# ...
```

在`tests/test1.cpp`中可以使用`DATA_DIR`：

```c
std::string dataFolder = TEST_DATA_DIR;
```

# 2. Log打印

可以使用Cpp的类库log4cplus，在本项目中定义自己的log打印类。详见：`NLib/3rdfiles/log4cplus`与`NLib/Tools/include/my_log.h`。注意，例如在`tests/test1`中使用，则要在`tests/CMakeLists.txt`中添加：

```cmake
# 若要使用log4cplus或my_log，需要添加以下链接库
add_custom_command (TARGET test1 POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
    $<TARGET_FILE:log4cplus::log4cplus> $<TARGET_FILE_DIR:test1>
)

add_custom_command (TARGET test1 POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
    ${PROJECT_SOURCE_DIR}/tools/src/iss_log.conf $<TARGET_FILE_DIR:test1>
)
```

@TODO: 避免这种拷贝方式，寻找更轻量化的方式。

# 3. 函数运行时间

可以在Visual Studio中使用**调试-性能探查器**查看函数运行时间。注意，若函数运行时间较短，可能无法显示，可以通过循环调用函数来增加函数运行时间。

# 4. Kit, Toolchain 设置

Kit: 一个Kit包含一个编译器、一个CMake生成器、一个目标体系结构和一个调试器。

Toolchain: 一个Toolchain包含一个编译器、一个目标体系结构和一个调试器。

在Windows下，若使用vcpkg安装的库，在运行CMake时，需要添加参数`-DCMAKE_TOOLCHAIN_FILE`，例如：`cmake -DCMAKE_TOOLCHAIN_FILE="C:/vcpkg/scripts/buildsystems/vcpkg.cmake" ..` 或者在`CMakeLists.txt`中设置该变量。

但该处的Toolchain并不是指vcpkg是一个Toolchain。vcpkg只是一个包管理器。

若在VSCode中设置Kit为`Visual Studio xx`，则不会使用vcpkg安装的库。因此，我目前的做法是设置Kit为[Unspecified]，然后在`settings.json`中设置
```json
"cmake.configureSettings": 
{"CMAKE_TOOLCHAIN_FILE": "C:/vcpkg/scripts/buildsystems/vcpkg.cmake"}
```
同理，linux下也设置为[Unspecified], 否则用的库不同。

## settings.json

另有一个问题，我在Windows下设置了`settings.json`使用vcpkg。但链接至WSL时，会出现找不到库的问题。