Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=[1,2,3,4,5]
>>> s.insert(3,5)
>>> s
[1, 2, 3, 5, 4, 5]
>>> s.pop()
5
>>> s.pop(3)
5
>>> s
[1, 2, 3, 4]
>>> 
>>> s.remove(4)
>>> s
[1, 2, 3]
>>> s.reverse()
>>> s
[3, 2, 1]
>>> s2=[9,3,5,1,7,5]
>>> s.sort()
>>> s
[1, 2, 3]
>>> s2.sort()
>>> s2
[1, 3, 5, 5, 7, 9]
>>> a=(3,2,1,5,6,7,8)
>>> type(a)
<class 'tuple'>
>>> a[0]=9
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a[0]=9
TypeError: 'tuple' object does not support item assignment
>>> a=a+(10,)
>>> a
(3, 2, 1, 5, 6, 7, 8, 10)
>>> a[2]
1
>>> a[2:]
(1, 5, 6, 7, 8, 10)
>>> a[:2]
(3, 2)
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b=()
>>> for i in b:
	print(i)

	
>>> b
()
>>> b=(2,3,4,5,6)
>>> for i in b:
	print(i)

	
2
3
4
5
6
>>> len(b)
5
>>> max(b)
6
>>> min(b)
2
>>> b.count(5)
1
>>> b=b+(2,)
>>> b
(2, 3, 4, 5, 6, 2)
>>> b.count(2)
2
>>> b.index(3)
1
>>> c=(6,7,8)
>>> b+c
(2, 3, 4, 5, 6, 2, 6, 7, 8)
>>> c*5
(6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8)
>>> d=((1,2),(3,4),(5,6))
>>> d
((1, 2), (3, 4), (5, 6))
>>> d[1]
(3, 4)
>>> d[1]10]
SyntaxError: invalid syntax
>>> d[1][0]
3
>>> e='priya'
>>> f=tuple(e)
>>> f
('p', 'r', 'i', 'y', 'a')
>>> type(e)
<class 'str'>
>>> type(f)
<class 'tuple'>
>>> tuple=()
>>> for i in range():
	tuple.append(i)

	
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    for i in range():
TypeError: range expected at least 1 argument, got 0
>>> for i in range(6):
	tuple.append(i)

	
Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    tuple.append(i)
AttributeError: 'tuple' object has no attribute 'append'
>>> f.count(3)
0
>>> f.count(a)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    f.count(a)
NameError: name 'a' is not defined
>>> f.count('a')
1
>>> f.extend(d)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    f.extend(d)
AttributeError: 'tuple' object has no attribute 'extend'
>>> f.insert(3,4)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    f.insert(3,4)
AttributeError: 'tuple' object has no attribute 'insert'
>>> f.pop()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    f.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> f.pop(3)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    f.pop(3)
AttributeError: 'tuple' object has no attribute 'pop'
>>> f
('p', 'r', 'i', 'y', 'a')
>>> f.remove('a')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    f.remove('a')
AttributeError: 'tuple' object has no attribute 'remove'
>>> f.reverse()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    f.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> f.sort()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    f.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> a=[1,0,9,8]
>>> a
[1, 0, 9, 8]
>>> b=tuple(a)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    b=tuple(a)
TypeError: 'tuple' object is not callable
>>> a=tuple(a)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a=tuple(a)
TypeError: 'tuple' object is not callable
>>> a=(9,8,7)
>>> b=list(a)
>>> b
[9, 8, 7]
>>> c=[9,3,4]
>>> d=tuple(c)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    d=tuple(c)
TypeError: 'tuple' object is not callable
>>> c=tuple(c)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    c=tuple(c)
TypeError: 'tuple' object is not callable
>>> 