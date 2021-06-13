Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30 days 30 hours challenge")
30 days 30 hours challenge
>>> hours="thirty"
>>> print(hours)
thirty
>>> days="thirty days"
>>> print(days)
thirty days
>>> print(days[0])
t
>>> print(days[7])
d
>>> print(days[5])
y
>>> challenge=" i will win"
>>> print(challenge[1:10])
i will wi
>>> print(challenge[4:5])
i
>>> print(challenge[0])
 
>>> print(challenge[15])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(challenge[15])
IndexError: string index out of range
>>> print(challenge[1:2])
i
>>> challenge="i will win"
>>> print(challenge.lower())
i will win
>>> a="30 Days"
>>> b="30 hours"
>>> c=a+b
>>> print(c)
30 Days30 hours
>>> a="30 Days"
>>> b="30 hours"
>>> c=a+" "+b
>>> print(c)
30 Days 30 hours
>>> text="thirty days and thirty hours"
>>> x=text.casefold()
>>> print(x)
thirty days and thirty hours
>>> text="thirty days and thirty hours"
>>> x=text.capitalize()
>>> print(x)
Thirty days and thirty hours
>>> text"thirty days and thirty hours"
SyntaxError: invalid syntax
>>> text="thirty days and thirty hours"
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> text="two days and two hours"
>>> x=text.find(days)
>>> print(x)
-1
>>> text ="thirty days and thirty hours"
>>> x=text.isalpha()
>>> print(x)
False
>>> text="thirty days and thirty hours"
>>> x=text.isalnum()
>>> print(x)
False
>>> i will win