# py3base92

A python library to create base92 encoded strings in python3.

## History Timeline
**Version: 1.0.3-1**  
Thenoviceoof-base92 supports python2 only. Build py3base92 based on base92.  
The current version pack is only a temporary release. It is not in pypi.   
I found that the version was posted to pypi by someone else. [python3base92 1.0.3.post1](https://pypi.org/project/python3base92/)  
**!!!Note: This version(pypi online version) is not maintained and managed by this repository, and there may be potential security problems and bugs. In order to avoid misleading, the instructions for using this version are no longer provided**  


**Version: 1.1.0**  
PyPI Release. Subsequent updates are based on the current version.      
> bytes already supported. And some bugs have been fixed.   

Remove redundant func：  
encode()  
base92_encode()
decode()  
base92_decode()  

**Version: 1.1.1**  
> Some optimization.



## Usage  

Installation  
`pip install py3-base92`  
or  
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



## Tests
Windows Powershell  
`$ENV:PYTHONPATH='src';python .\tests\test_base92.py`  
Linux  
`PYTHONPATH=src python .\tests\test_base92.py`  


## Document
[文档(Document)](https://github.com/Gu-f/py3base92/wiki/%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3(Document))  
