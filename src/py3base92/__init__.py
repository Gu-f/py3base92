# -*- coding: utf-8 -*-

"""
>>> from .base92 import Base92
>>> x = Base92.b92encode('hello world')
>>> x
'Fc_$aOTdKnsM*k'
>>> Base92.b92decode(x)
b'hello world'
"""

from .base92 import Base92, __version__
b92encode = Base92.b92encode
b92decode = Base92.b92decode
get_character_set = Base92.get_character_set
