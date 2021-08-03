Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=5
>>> id(num)
140735254720912
>>> name='sandhya'
>>> id(name)
2199099808048
>>> a-10
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a-10
NameError: name 'a' is not defined
>>> a=10
>>> b=a
>>> a
10
>>> b
10
>>> id(a)
140735254721072
>>> id(b)
140735254721072
>>> id(10)
140735254721072
>>> k=10
>>> id(k)
140735254721072
>>> a=9
>>> id(a)
140735254721040
>>> id(b)
140735254721072
>>> a
9
>>> b
10
>>> k=a
>>> id(k)
140735254721040
>>> b=8
>>> PI=3.14
>>> PI
3.14
>>> PI=3.15
>>> type(PI)
<class 'float'>
>>> 
============== RESTART: C:/Users/DELL/Desktop/mypythonfiles/ty.py ==============
hello
>>> 
============== RESTART: C:/Users/DELL/Desktop/mypythonfiles/ty.py ==============
hello
>>> 
============== RESTART: C:/Users/DELL/Desktop/mypythonfiles/ty.py ==============
hello
10
>>> num=2.5
>>> type(num)
<class 'float'>
>>> num=5
>>> type(num)
<class 'int'>
>>> num=6+9j
>>> type(num)
<class 'complex'>
>>> num
(6+9j)
>>> a=5.6
>>> b=int(a)
>>> type(b)
<class 'int'>
>>> k=float(b)
>>> k
5.0
>>> k=6
>>> c=complex(b,k)
>>> c
(5+6j)
>>> b<k
True
>>> bool=b<k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> b>k
False
>>> int(True)
1
>>> int(False)
0
>>> lst=[25,36,45]
>>> type(lst)
<class 'list'>
>>> s={1,2,3,5,8}
>>> type(s)
<class 'set'>
>>> t=(23,56,45,63)
>>> type(t)
<class 'tuple'>
>>> str="sanju"
>>> type(str)
<class 'str'>
>>> st='a'
>>> type(st)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range(10))
<class 'range'>
>>> list(range(2:10:2))
SyntaxError: invalid syntax
>>> list(range(2,10:2))
SyntaxError: invalid syntax
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> dict={"name":'san','rahul':'Iphone','kiran'='oneplus'}
SyntaxError: invalid syntax
>>> dict={"name":'san','rahul':'Iphone','kiran':'oneplus'}
>>> dict
{'name': 'san', 'rahul': 'Iphone', 'kiran': 'oneplus'}
>>> dict.keys()
dict_keys(['name', 'rahul', 'kiran'])
>>> dict.values()
dict_values(['san', 'Iphone', 'oneplus'])
>>> d['rahul']
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d['rahul']
NameError: name 'd' is not defined
>>> dict['rahul']
'Iphone'
>>> d.get('kiran')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    d.get('kiran')
NameError: name 'd' is not defined
>>> dict.get('kiran')
'oneplus'
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> docs
No Python documentation found for 'docs'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> python docs
No Python documentation found for 'python docs'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
