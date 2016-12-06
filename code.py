#!/usr/bin/python

Please check out: http://continuum.io/thanks and https://anaconda.org
>>> bin(ord('H'))
'0b1001000'
>>> bin(ord('H'))[2:]
'1001000'
>>> bin(137)[2:]
'10001001'
>>> bin(141)[2:]
'10001101'
>>> def pad(message):
...     missing = 8 - len(message)
...     return ('0' * missing) + message
...
>>> pad('01')
'00000001'
>>> b = ''
>>> for char in 'Hello': b += pad(bin(char)[2:])
...
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an index
>>> for char in 'Hello': b += pad(bin(char)[2:])
...
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an index
>>> bin('H')
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an index
>>> for char in 'Hello': b += pad(bin(ord(char))[2:])
...
>>> b
'0100100001100101011011000110110001101111'
>>> len(b)
40
>>>