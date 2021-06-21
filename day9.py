Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1
>>> list_1 = [1,2,3,4,5]
>>> l = []
>>> n = len(list_1)
>>> for i in list_1:
	l.append(i+2)
	print(l)

	
[3]
[3, 4]
[3, 4, 5]
[3, 4, 5, 6]
[3, 4, 5, 6, 7]
>>> #2
>>> n = int(5)
>>> a = 0
>>> b = 1
>>> c = 0
>>> sum = 0
>>> count = 1
>>> print("fibonacci series:",end = "")
fibonacci series:
>>> while(count<= n):
	print(sum,end ="")
	count+= 1
	a = b
	b = sum
	sum = a+b
	print("\n")

	
0

1

1

2

3

>>> #3
>>> num_25 = int(154)
>>> sum_25 = 0
>>> temp_1 = num_25
>>> while temp_1>0:
	digit_25 = temp_1%10
	sum_25+=digit_25**3
	temp_1//=10
	if num_25 == sum_25:
		print(num_25,"is amrstrong")
else:
	print(num_25,"is not amrstrong")

	
154 is not amrstrong
>>> #multiplication table opf 9
>>> n_156 = int(9)
>>> mul_21 = 0
>>> print("multiplication table of:9",)
multiplication table of:9
>>> for p in range(1,10+1):
	mul_21 = n_156*p
	print(n_156,"x",p,"=",mul_21)

	
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
>>> # program to knoe  positive or negative
>>> def find(ins_12345):
	year = int(ins_12345/365)
	week = int((ins_12345%365)/day_check)
	days = int((ins_12345%365)%day_check)
	print(year,":years,",week,":weeks,",days,":days")

	
>>> ins_12345 = int(402)
>>> day_check = 7
>>> find(ins_12345)
1 :years, 5 :weeks, 2 :days
>>> #trignometry using math fun
>>> import math
>>> a_b = math.pi/6
>>> print("the value of sine of pi/6 is:",end="")
the value of sine of pi/6 is:
>>> print(math.sin(a_b))
0.49999999999999994
>>> print("the value of cosine of pi/6 is:",end="")
the value of cosine of pi/6 is:
>>> print(math.cos(a_b))
0.8660254037844387
>>> #6
>>> n = int(60)
>>> if n > 0:
	print("number is positive")
elif n <0:
	print("number is negative")
else:
	print("number is neither positive nor negative")

	
number is positive
>>> #calculator
>>> print('calculator')
calculator
>>> print('1.add')
1.add
>>> print('2.subtraction')
2.subtraction
>>> print('3.multiplication')
3.multiplication
>>> print('4.divide')
4.divide
>>> ch = int(input("enter choice(1-4):"))
enter choice(1-4):5
>>> if ch ==1:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a+b
	print("sum=",c)

	
>>> if ch ==1:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a+b
	print("sum=",c)
elif ch ==2:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a-b
	print("difference =",c)
elif ch == 3:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a*b
	print("product =",c)
elif ch == 4:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	print("quotient = ",c)

	
>>> 
>>> 
>>> 
>>> 
>>> if ch ==1:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a+b
	print("sum=",c)
elif ch ==2:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a-b
	print("difference =",c)
elif ch == 3:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a*b
	print("product =",c)
elif ch == 4:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	print("quotient = ",c)

	
>>> 