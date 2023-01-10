# python_study_code

看漫画学python笔记和代码

## 1、基础

### 1.1、标识符

标识符就是变量、函数、属性、类、模块等可以由程序员指定名称的代码元素

python里的标识符遵循一定的命名规则
1.区分大小写
2.首字母可以是下划线和字母，不能是数字
3.除首字符外的其他字符必须是下划线、字母和数字
4.关键字不能作为标识符
5.不使用Python的内置函数作为自己的标识符

### 1.2、关键字

关键字由语言本身定义好的有特殊含义的代码元素
python中有33个关键字 其中False、True、None首字母大写，其他关键字首字母小写

![image-20230110153913477](images\image-20230110153913477.png)

### 1.3、变量

python和go声明变量的不同在于：
python给变量赋值的同时就声明了该变量，该变量的数据类型就是赋值数据所属的数据类型
python 是动态语言，所以即使一个变量已经赋值过，依然可以接受其他类型的数据

### 1.4、语句

python代码由关键字、标识符、表达式和语句等构成，语句是代码的重要组成部分
python中一行代码表示一条语句，一般语句结束的时候是不加分号的，当然也可以加分号
go语句结束的时候也是不加分号的，当然也可以加，加了在保存代码的时候也会被格式化去掉

### 1.5、注释

python 注释 使用 #
go/java 注释使用 // /**/ 分别代表单行和多行注释
将 #coding=utf-8 放在第一行和第二行可以告诉python解释器该文件的编码集使用的是UTF-8，避免中文等文字乱码

### 1.6、模块

python中一个模块代表一个文件，模块是保存代码的最小单位
模块类似于go的package用来管理代码
一个模块可以导入另一个模块
