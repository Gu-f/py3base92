# py3base92

A python library to create base92 encoded strings in python3.

## History Timeline
**Version: 1.0.3-1**  
Thenoviceoof-base92 supports python2 only. Build py3base92 based on base92.  
The current version pack is only a temporary release. It is not in pypi.   
I found that the version was posted to pypi by someone else. [python3base92 1.0.3.post1](https://pypi.org/project/python3base92/)  
Installation command `pip install python3base92`  
> Only printable characters supported, not bytes.  
> Usage：  
> Import the py3base92 module after installed by setup.py   
func:  
b92encode() / encode() / base92_encode()  equal  
b92decode() / decode() / base92_decode()  equal  
```python
# Only version 1.0.3-1 is supported  
import py3base92
print(py3base92.encode("test"))
print(py3base92.b92encode("test"))
print(py3base92.base92_encode("test"))
print(py3base92.decode("Jw_@V"))
print(py3base92.b92decode("Jw_@V"))
print(py3base92.base92_decode("Jw_@V"))
```


**Version: 1.1.0**  
PyPI Release. Subsequent updates are based on the current version.      
> bytes already supported. And some bugs have been fixed.   

Remove redundant func：  
encode()  
base92_encode()
decode()  
base92_decode()  



## Usage  
Since the py3base92 package name is determined by pypi to be similar to the previous python3base92 package name, it cannot be used, so the new version uses py3-base92.  
There are some bugs in the old version, it is recommended to use the latest version.  

Installation  
`pip install py3-base92`(Old version use `pip install python3base92`)  
or  
`$ENV:PYTHONPATH='src';python .\src\setup.py install`(Windows Powershell)  
`PYTHONPATH=src python .\src\setup.py install`(Linux)  

```python
import py3base92 as base92

print(base92.b92encode("hello world".encode()))

print(base92.b92decode("Fc_$aOTdKnsM*k").decode())
```



## Tests
Windows Powershell  
`$ENV:PYTHONPATH='src';python .\tests\test_base92.py`  
Linux  
`PYTHONPATH=src python .\tests\test_base92.py`  


## Document
[文档(Document)](https://github.com/Gu-f/py3base92/wiki/%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3(Document))  
