# py3base92
一个python3实现的base92编码python库  
A python library to create base92 encoded strings in python3.  

正式版本的版本号开始于1.1.0，至于为什么从1.1.0开始，考虑到python2的实现版本为1.0.3，并且已停更，然后之前又发布了一个临时py3的版本1.0.3-1，想区别于py2的版本号又不想从0版本开始，就即兴定下了第一个版本号为1.1.0  

[Readme_EN](https://github.com/Gu-f/py3base92/blob/master/README_EN.md)


## 历史版本时间线
**版本: 1.0.3-1**  
更新到python3之后发现base92模块不能用了，看到原作者thenoviceoof的base92的包最后更新也是7年前了，因此在其基础代码上做base92 python3的兼容版本
包作为临时使用，并未准备用做项目，所以未发到PyPi ，同时构建的setup也未做详细描述和介绍。  
pypi中搜索了下，我没有发布，但是发现其他人把这个版本发布上去了，[python3base92 1.0.3.post1](https://pypi.org/project/python3base92/)  
**!!!注意: 该版本(pypi上的这个版本)不受该仓库维护和管理，可能存在潜在安全问题及Bug，为防止误导，不再提供该版本使用说明**  


**版本: 1.1.0**  
第一个正式发布到PyPi的版本，后续仅在该版本基础上更新。    
> 该版本已完善支持bytes，并修复了上个版本中遗留的一些bug  

移除冗余方法：  
encode()  
base92_encode()  
decode()  
base92_decode()  

**版本: 1.1.1** 
> 一些优化



## 用法
安装  
`pip install py3-base92`  
或  
`$ENV:PYTHONPATH='src';python .\src\setup.py install`(Windows Powershell)  
`PYTHONPATH=src python .\src\setup.py install`(Linux)  

```python
import py3base92

print(py3base92.b92encode("你好".encode()))
# sIb@Vyq8
print(py3base92.b92decode("sIb@Vyq8").decode())
# 你好
print(py3base92.b92encode("hello world".encode()))
# Fc_$aOTdKnsM*k
print(py3base92.b92decode("Fc_$aOTdKnsM*k").decode())
# hello world
```



## 测试用例
Windows Powershell  
`$ENV:PYTHONPATH='src';python .\tests\test_base92.py`  
Linux  
`PYTHONPATH=src python .\tests\test_base92.py`  


## 文档
[文档(Document)](https://github.com/Gu-f/py3base92/wiki/%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3(Document))  
