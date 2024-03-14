---
title: 使用ssh连接个人Ubuntu电脑
category: 技术博客
date: 2024-03-13
---

# 内网穿透
{% note  %}
内网穿透参见:[使用SSH优雅连接在家里的主机/](https://xiaoyanfufu.gitee.io/2024/02/25/%E4%BD%BF%E7%94%A8SSH%E4%BC%98%E9%9B%85%E8%BF%9E%E6%8E%A5%E5%9C%A8%E5%AE%B6%E9%87%8C%E7%9A%84%E4%B8%BB%E6%9C%BA/) 
{% endnote %}

因为要在外网连接ubuntu电脑,需要配置内网穿透。使用Natapp的免费隧道进行穿透(选择tcp),下载natapp,更改权限`chmod a+x natapp`,配置config.ini (参见[NATAPP1分钟快速新手图文教程](https://natapp.cn/article/natapp_newbie)) 并运行natapp.得到natappfree的网址和端口.(注意每次打开端口号会变)


# ssh连接
在windows下使用`ssh username@server.natappfree.cc -P portNum`命令，输入密码后可以连接到ubuntu了。同样可以在vscode中使用remote ssh连接。

# 免密登录
此时每次SSH登录都需要输入密码，可以使用免密登录。
1. 在本地生成密钥对`ssh-keygen -t rsa -C `
2. 将公钥复制到服务器上`ssh-copy-id`或者手动复制到`~/.ssh/authorized_keys`文件中

{% note  %}
在windows下没有`ssh-copy-id`命令，可以参考[windows无法使用ssh-copy-id解决办法](https://blog.csdn.net/qq_45624685/article/details/122631083)
{% endnote %}

此时再次使用ssh远程连接时就不需要输入密码了。使用Vscode的remote ssh也可以免密登录。