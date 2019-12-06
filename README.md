# py3base92
更新到python3之后发现base92模块不能用了，看到原作者的base92的包最后更新也是7年前了，因此在其基础代码上做base92 python3的兼容版本

[原作者项目地址](https://github.com/thenoviceoof/base92)

## 已知问题  
部分不可见字符及中文不支持
>>因可满足常规的使用，暂不准备做更多，请支持原作者更新更完善内容  

包作为临时使用，并未准备用做项目，所以未发到PyPi ，同时构建的setup也未做详细描述和介绍


# 用法  
采用setup.py安装后需要导入py3base92模块

函数:  
b92encode() / encode() / base92_encode()  等价  
b92decode() / decode() / base92_decode()  等价  

```python
import py3base92
print(py3base92.encode("test"))
print(py3base92.b92encode("test"))
print(py3base92.base92_encode("test"))
print(py3base92.decode("Jw_@V"))
print(py3base92.b92decode("Jw_@V"))
print(py3base92.base92_decode("Jw_@V"))
```
