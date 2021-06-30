Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # create a list lambda fun .....
>>> r = lambda x,y : x*y
>>> print(r(10,6))
60
>>> ##to create fibonacci series to n....
>>> from functools import reduce
>>> fib = lambda n: reduce(lambda x, _:x+[x[-1]+x[-2]],range(n-2),[0,1])
>>> 
>>> print(fib(11))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> #3q
>>> nums = [2,3,6,5]
>>> n = 2
>>> print("original list:",nums)
original list: [2, 3, 6, 5]
>>> print("Given number:",n)
Given number: 2
>>> filtered_numbers=list(map(lambda number:number*n,nums))
>>> print("Result:")
Result:
>>> print(''.join(map(str,filtered_numbers)))
461210
>>> #4q
>>> list1 = [2,3,6,5,45,56,35,52,26,24]
>>> print(list1)
[2, 3, 6, 5, 45, 56, 35, 52, 26, 24]
>>> list2 = list(map(lambda j:j%9==0,list1))
>>> print("Result")
Result
>>> print(''.join(map(str,list2)))
FalseFalseFalseFalseTrueFalseFalseFalseFalseFalse
>>> list2 = list(filter(lambda j:j%9==0,list1))
>>> print("Result")
Result
>>> print(''.join(map(str,list2)))
45
>>> #5q
>>> list1 = [2,3,6,5,4,9,868,23,36,35,34,39,75,65]
>>> print(list1)
[2, 3, 6, 5, 4, 9, 868, 23, 36, 35, 34, 39, 75, 65]
>>> list2 = list(filter(lambda j:j%2==0,list1))
>>> print("Result:")
Result:
>>> print(len(list2))
6
>>> 