Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Dict={'tamilnadu':'chennai','kerala':'tiruvananthapuram'}
>>> type(Dict)
<class 'dict'>
>>> Dict['tamilnadu']
'chennai'
>>> chennai in Dict
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    chennai in Dict
NameError: name 'chennai' is not defined
>>> 'chennai' in Dict
False
>>> 'tamilnadu' in Dict
True
>>> Dict2={'goa':'banama','gujarat':'gandhinagar'}
>>> Dict.update(Dict2)
>>> Dict
{'tamilnadu': 'chennai', 'kerala': 'tiruvananthapuram', 'goa': 'banama', 'gujarat': 'gandhinagar'}
>>> del Dict['goa']
>>> Dict
{'tamilnadu': 'chennai', 'kerala': 'tiruvananthapuram', 'gujarat': 'gandhinagar'}
>>> for key in Dict:
	print(key)

	
tamilnadu
kerala
gujarat
>>> for key in Dict:
	print(key,Dict(key))

	
Traceback (most recent call last):
  File "<pyshell#16>", line 2, in <module>
    print(key,Dict(key))
TypeError: 'dict' object is not callable
>>> for key in Dict:
	print(key,Dict[key])

	
tamilnadu chennai
kerala tiruvananthapuram
gujarat gandhinagar
>>> 