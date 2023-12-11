import py3base92

print(py3base92.b92encode("你好".encode()))
# sIb@Vyq8
print(py3base92.b92decode("sIb@Vyq8").decode())
# 你好
print(py3base92.b92encode("hello world".encode()))
# Fc_$aOTdKnsM*k
print(py3base92.b92decode("Fc_$aOTdKnsM*k").decode())
# hello world
