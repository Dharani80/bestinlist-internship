Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1
>>> #NAME ERROR
>>> list = 12
>>> print(list1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(list1)
NameError: name 'list1' is not defined
>>> #TYPE ERROR
>>> a = 35
>>> a+=45
>>> a
80
>>> x=45
>>> x+='123'
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x+='123'
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
>>> #SYNTAX ERROR
>>> print(hey google)
SyntaxError: invalid syntax
>>> #INDEX ERROR
>>> l = [1,2,3,4,5]
>>> x = l[5]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x = l[5]
IndexError: list index out of range
>>> #MODULE NOT FOUND ERROR
>>> import my module
SyntaxError: invalid syntax
>>> import mymodule
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    import mymodule
ModuleNotFoundError: No module named 'mymodule'
>>> #KEY ERROR
>>> dict={1:90,2:80,3:76}
>>> print(dict[5])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(dict[5])
KeyError: 5
>>> #IMPORT ERROR
>>> from pandas import abc
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    from pandas import abc
ModuleNotFoundError: No module named 'pandas'
>>> #VALUE ERROR
>>> float('dharani')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    float('dharani')
ValueError: could not convert string to float: 'dharani'
>>> #ZERO DIVISION ERROR
>>> 100/0
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    100/0
ZeroDivisionError: division by zero
>>> """Desing a simple calculator app with try and except for all use cases"""
'Desing a simple calculator app with try and except for all use cases'
>>> def calculator():
	try:
		print('+')
		print('-')
		print('*')
		print('%')
		print('**')
		operation = input("select an operator\n")
		print("Enter two numbers")
		num_1 = int(input())
		num_2 = int(input())
		if operation =='+':   #to add numbers
			print(num_1 + num_2)
		elif operation =='-':
			print(num_1 - num_2)
		elif operation =='*':
			print(num_1 * num_2)
		elif operation =='%':
			print(num_1 % num_2)
		elif operation =='/':
			print(num_1 / num_2)
		elif opeation =='**':
			print(num_1 ** num_2)
		else:
			print("invalid input")
		except Exception as e:
			
SyntaxError: invalid syntax
>>> except Exception as e:
	
SyntaxError: invalid syntax
>>> """Design a simple calculator app with try and except for all use cases"""
'Design a simple calculator app with try and except for all use cases'
>>> def clculatror():
	try:
		print('+')
		print('-')
		print('*')
		print('%')
		print('**')
		operation = input("select an operator\n")
		print("Enter two numbers")
		num_1 = int(input())
		num_2 = int(input())
		if operation =='+':  #to add numbers
			print(num_1 + num_2)
		elif operation =='-':
			print(num_1 - num_2)
		elif operation =='*':
			print(num_1 * num_2)
		elif operation =='%':
			print(num_1 % num_2)
		elif operation =='/':
			print(num_1 / num_2)
		elif operation =='**':
			print(num_1 ** num_2)
		else:
			print("invalid input")
			except Exception as e:
				
SyntaxError: invalid syntax
>>> print(calculate)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print(calculate)
NameError: name 'calculate' is not defined
>>> >>> """Design a simple calculator app with try and except for all use cases"""
SyntaxError: invalid syntax
>>> def clculatror():
	try:
		print('+')
		print('-')
		print('*')
		print('%')
		print('**')
		operation = input("select an operator\n")
		print("Enter two numbers")
		num_1 = int(input())
		num_2 = int(input())
		if operation =='+':  #to add numbers
			print(num_1 + num_2)
		elif operation =='-':
			print(num_1 - num_2)
		elif operation =='*':
			print(num_1 * num_2)
		elif operation =='%':
			print(num_1 % num_2)
		elif operation =='/':
			print(num_1 / num_2)
		elif operation =='**':
			print(num_1 ** num_2)
		else:
			print("invalid input")
			except Exception as e:
				
SyntaxError: invalid syntax
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> def calculator():
	try:
		print('+')
		print('-')
		print('*')
		print('%')
		print('/')
		print('**')
		operation = input("select an operator\n")
		print("Enter two numbers")
		num_1 = int(input())
		num_2 = int(input())
		if operator =='+':
			print(num_1 + num_2)
		elif opertion =='-':
			print(num_1 - num_2)
		elif operation =='*':
			print(num_1 * num_2)
		elif operation =='%':
			print(num_1 % num_2)
		elif operation =='/':
			print(num_1 / num_2)
		elif operation =='**':
			print(num_1 ** num_2)
		else:
			print("invalid input")
except Exception as e:
	
SyntaxError: unexpected unindent
>>> 