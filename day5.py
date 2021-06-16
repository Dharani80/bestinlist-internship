Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=4
>>> M=[855,5,2,74,33,]
>>> M=M*n
>>> print(M)
[855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33]
>>> print('updated M list:',M)
updated M list: [855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33]
>>> # add an item in list
>>> M.append(6)
>>> print(M)
[855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 6]
>>> print('updated M list:',M)
updated M list: [855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 6]
>>> #Delete an item in list
>>> M.remove(855)
>>> print(M)
[5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 6]
>>> # Storing the largest number from the list
>>> P=max(M)
>>> print(P)
855
>>> #storing the smallest number from the list
>>> Q=min(M)
>>> print(M)
[5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 855, 5, 2, 74, 33, 6]
>>> print(Q)
2
>>> #creating a tuple and reverse of the created tuple
>>> X=('d','h','a','r','a','n','i', '84','hello','world')
>>> print(X)
('d', 'h', 'a', 'r', 'a', 'n', 'i', '84', 'hello', 'world')
>>> Z=reversed(X)
>>> print(tuple(Z))
('world', 'hello', '84', 'i', 'n', 'a', 'r', 'a', 'h', 'd')
>>> #Tuple to convert into list
>>> R=( 582,'am','abc',5,2)
>>> S=list(R)
>>> print"list elements:",S
SyntaxError: invalid syntax
>>> print"list elements :",S
SyntaxError: invalid syntax
>>> type(R)
<class 'tuple'>
>>> S=list(R)
>>> type(S)
<class 'list'>
>>> print(S)
[582, 'am', 'abc', 5, 2]
>>> print(R)
(582, 'am', 'abc', 5, 2)
>>> R=(582,'am','abc',5,2)
>>> type(R)
<class 'tuple'>
>>> R=list(R)
>>> type(R)
<class 'list'>
>>> print(R)
[582, 'am', 'abc', 5, 2]
>>> 