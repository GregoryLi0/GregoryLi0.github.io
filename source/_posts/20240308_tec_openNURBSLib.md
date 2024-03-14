---
title: cmake使用openNURBS
category: 技术博客
date: 2024-03-08
---

想要在cmake中使用openNURBS库。OpenNURBS教程中没有给明确的安装方法，甚至在源代码中还包含sln文件。所有找方法导入到自己的项目中。

Copy了openNURBS源码到项目中，使用add_subdirectory添加了openNURBS的CMakeLists.txt，但是在Windows下只能链接到openNURBS的静态库，能够正常生成动态库文件，如果手动复制dll文件到项目的bin目录下，程序可以正常运行，但是无法在cmake中指定动态库位置。在Linux下只能链接到openNURBS的动态库（带有Threads::Threads库防止报错），而不能链接到openNURBS的静态库。

目前通过在cmake中判断操作系统，使用不同的链接方式解决了这个问题。

```cmake
#... 

add_subdirectory("3rdfiles/opennurbs-8")

include_directories(
    #...
    ${PROJECT_SOURCE_DIR}/3rdfiles/opennurbs-8
    #...
)

#... 

if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
    message(STATUS "current system: Linux")
    target_link_libraries(test3rdlib OpenNURBS Threads::Threads)
elseif(CMAKE_SYSTEM_NAME MATCHES "Windows")
target_link_libraries(test3rdlib opennurbsStatic)
    message(STATUS "current system: Windows")
else()
    message(STATUS "current system: ${CMAKE_SYSTEM_NAME}")
endif()
```