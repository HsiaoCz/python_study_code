## python web 框架 django

### 1、web

Web 服务（Web service）是一种面向服务的架构的技术，通过标准的 Web 协议提供服务，目的是保证不同平台的应用服务可以互操作。

简单的说就是，可以让我们通过网络访问目标服务器上的文件

例如我通过网络访问百度，腾讯，淘宝，其本质就是访问到了目标机器上的文件

### 2、Django

Django 安装：`pip install Django`

生成环境

```bash
python3 -m venv hello

cd hello

# 安装django
source venv/bin/activate
# 这里有个问题，上面这一套适用于bash和zsh，但是fish就寄
# 这里需要把activate替换成activate.fish

# 安装django
pip install django -i https://pypi.douban.com/simple

# 使用django命令创建一个项目
django-admin startproject helloworld

# cd helloworld
helloworld
manage.py  # 项目的入口

# 将虚拟环境挪到项目下
mv hello/ helloworld/
```
