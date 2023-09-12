# py3base92
一个python3实现的base92编码python库  
A python library to create base92 encoded strings in python3.  

正式版本的版本号开始于1.1.0，至于为什么从1.1.0开始，考虑到python2的实现版本为1.0.3，并且已停更，然后之前又发布了一个临时py3的版本1.0.3-1，想区别于py2的版本号又不想从0版本开始，就即兴定下了第一个版本号为1.1.0  

[Readme_EN](https://github.com/Gu-f/py3base92/blob/master/README_EN.md)


## 历史版本时间线
**版本: 1.0.3-1**  
更新到python3之后发现base92模块不能用了，看到原作者thenoviceoof的base92的包最后更新也是7年前了，因此在其基础代码上做base92 python3的兼容版本
包作为临时使用，并未准备用做项目，所以未发到PyPi ，同时构建的setup也未做详细描述和介绍。  
> 该版本只支持可打印字符，不支持bytes  
> 用法：  
> 采用setup.py安装后需要导入py3base92模块  
函数:  
b92encode() / encode() / base92_encode()  等价  
b92decode() / decode() / base92_decode()  等价 
```python
# 当前用法仅为1.0.3-1版本
import py3base92
print(py3base92.encode("test"))
print(py3base92.b92encode("test"))
print(py3base92.base92_encode("test"))
print(py3base92.decode("Jw_@V"))
print(py3base92.b92decode("Jw_@V"))
print(py3base92.base92_decode("Jw_@V"))
```


**版本: 1.1.0**  
第一个正式发布到PyPi的版本，后续仅在该版本基础上更新。    
> 该版本已完善支持bytes  

移除冗余方法：  
encode()  
base92_encode()  



## 用法  

`pip install py3-base92`  
或  
`$ENV:PYTHONPATH='src';python .\src\setup.py install`(Windows Powershell)  
`PYTHONPATH=src python .\src\setup.py install`(Linux)  

```python
import py3base92 as base92

print(base92.b92encode("hello world".encode()))

print(base92.b92decode("Fc_$aOTdKnsM*k").decode())
```



## 测试用例
Windows Powershell  
`$ENV:PYTHONPATH='src';python .\tests\test_base92.py`  
Linux  
`PYTHONPATH=src python .\tests\test_base92.py`  


## 文档
[文档(Document)](https://github.com/Gu-f/py3base92/wiki/%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3(Document))  
