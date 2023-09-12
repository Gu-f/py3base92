# py3base92

A python library to create base92 encoded strings in python3.

## History Timeline
**Version: 1.0.3-1**  
Thenoviceoof-base92 supports python2 only. Build py3base92 based on base92.  
The current version pack is only a temporary release. It is not in pypi.   
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
> bytes already supported.    

Remove redundant func：  
encode()  
base92_encode()  



## Usage  

`pip install py3base92`  
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
