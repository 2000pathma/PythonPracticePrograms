Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=2.
>>> c='a'
>>> d=78
>>> list=[10,2.,'a',78]
>>> friend1='a'
>>> friend2='b'
>>> friemd='c'
>>> print(friend1,friend2,friemd)
a b c
>>> friendlist-['a','b','c]
	    
SyntaxError: EOL while scanning string literal
>>> friendlist=['a','b','c]
	    
SyntaxError: EOL while scanning string literal
>>> friendlist=['a','b','c']
>>> print(friendlist)
['a', 'b', 'c']
>>> #list is mutable
>>> list=[10,2.7,'a']
>>> list[0]
10
>>> list[0]=12
>>> list
[12, 2.7, 'a']
>>> fruitlist=['apple','orange','banana','graphe']
>>> type(fruitlist)
<class 'list'>
>>> fruitlist[1:3]
['orange', 'banana']
>>> fruitlist[:]
['apple', 'orange', 'banana', 'graphe']
>>> fruitlist[1:]
['orange', 'banana', 'graphe']
>>> fruitlist[:3]
['apple', 'orange', 'banana']
>>> student=[]
>>> student.append(12,3,4)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    student.append(12,3,4)
TypeError: list.append() takes exactly one argument (3 given)
>>> student.append(12)
>>> student.append(3)
>>> student.append(4)
>>> print(student)
[12, 3, 4]
>>> apple in fruitlist
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    apple in fruitlist
NameError: name 'apple' is not defined
>>> 'apple' in fruitlist
True
>>> 'jerry' in friendlist
False
>>> print(fruitlist)
['apple', 'orange', 'banana', 'graphe']
>>> fruitlist.sort()
>>> fruitlist
['apple', 'banana', 'graphe', 'orange']
>>> student.insert(0,23,4)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    student.insert(0,23,4)
TypeError: insert expected 2 arguments, got 3
>>> student.insert(23,12)
>>> student
[12, 3, 4, 12]
>>> student.insert(0,2)
>>> student
[2, 12, 3, 4, 12]
>>> list=[0,3,4,1,3,6,7,8,0,7]
>>> listduplicate=[i for i,x in enumerate(list) if list==7]
>>> listduplicate
[]
>>> print(listduplicate)
[]
>>> listduplicate=[i for i,x in enumerate(list) if list==0]
>>> print(listduplicate)
[]
>>> 