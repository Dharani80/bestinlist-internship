Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #merge dict
>>> def Merge(dict1,dict2):
	return(dict2.update(dict1))

>>> dict1 = {'a':10,'b':8}
>>> dict2 = {'d':6,'c':4}
>>> print(Merge(dict1,dict2))
None
>>> print(dict2)
{'d': 6, 'c': 4, 'a': 10, 'b': 8}
>>> #remove a key from dictionary
>>> players = ["cricket":"dhoni","badminton":"sindhu","running":"usha"]
SyntaxError: invalid syntax
>>> players = ["cricket":"dhoni","badminton":"sindhu","running":"usha"]
SyntaxError: invalid syntax
>>> players = {"cricket":"dhoni","badminton":"sindhu","running":"usha"}
>>> print(players)
{'cricket': 'dhoni', 'badminton': 'sindhu', 'running': 'usha'}
>>> del players['cricket']
>>> print(players)
{'badminton': 'sindhu', 'running': 'usha'}
>>> #Map two  lists into a dictionary
>>> measurements = ["length","breadth","height"]
>>> values = ["30","30","30"]
>>> myDist = {m:v for m,v in zip(measurements,values)}
>>> print("Dictionary items :",myDict)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print("Dictionary items :",myDict)
NameError: name 'myDict' is not defined
>>> print("Dictionary items :",myDist)
Dictionary items : {'length': '30', 'breadth': '30', 'height': '30'}
>>> #length of the set
>>> A = {1,2,3,4,5}
>>> print(A)
{1, 2, 3, 4, 5}
>>> len(A)
5
>>> #remove the intersection of sets
>>> X = {a,b,c,d,e}
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    X = {a,b,c,d,e}
NameError: name 'a' is not defined
>>> A = {1,2,3,4,}
>>> b ={5,7,11,13}
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> print(A)
{1, 2, 3, 4}
>>> print(b)
{13, 11, 5, 7}
>>> An1 = {1,2,3,4,5}
>>> Bni = {5,7,11,13,17}
>>> print(Bni)
{17, 5, 7, 11, 13}
>>> Xn1 = {1,2,3,5,}
>>> Yn2 = {7,11,13,17}
>>> print(Xn1)
{1, 2, 3, 5}
>>> print(Yn2)
{17, 11, 13, 7}
>>> print("\nRemove the intersection of a 2nd set from the 1st set using difference update():")

Remove the intersection of a 2nd set from the 1st set using difference update():
>>> Xn1.difference update(Yn2)
SyntaxError: invalid syntax
>>> Xn1.difference update (Yn2)
SyntaxError: invalid syntax
>>> print("Xn1:",Xn1)
Xn1: {1, 2, 3, 5}
>>> print("Yn2:",Yn2)
Yn2: {17, 11, 13, 7}
>>> Xn1 = {1,2,3,5}
>>> Yn2 = {7,11,13,17}
>>> print("nRemove the intersection of a 2nd set from the 1st set using -= operator:")
nRemove the intersection of a 2nd set from the 1st set using -= operator:
>>> Xn1-=Yn2
>>> print("Xn1:",Xn1)
Xn1: {1, 2, 3, 5}
>>> print("Yn2:",Yn2)
Yn2: {17, 11, 13, 7}
>>> 
>>> 