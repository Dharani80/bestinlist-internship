Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #getting two  inputs from user
>>> A = int(input("Enter an integer:"))
Enter an integer:4
>>> B = int(input("Enter an integer:"))
Enter an integer:2
>>> #addition of two numbers
>>> print("sum of A and B:"A+B)
SyntaxError: invalid syntax
>>> print("sum of A and B:",A+B)
sum of A and B: 6
>>> #sub of two numbers
>>> print("difference of A and B:",A-B)
difference of A and B: 2
>>> #Multiplication of two numbers
>>> print("multiplication of A and B:",A*B)
multiplication of A and B: 8
>>> print("division of A and B:",A%B)
division of A and B: 0
>>> #Create a function covid()
>>> def covid(patientname,bodytemperature):
	if bodytemperature<str(0):
		default = str(98)
		print("patientname is",patientname,"bodytemperature is",default)
	else:
		print("patientname is",patientname,"bodytemperature is",bodytemperature)
		covid("dharani","")
		covid("dharani","99")

		
>>> 
>>> patientname is dharani bodytemperature is 98
SyntaxError: invalid syntax
>>> patientname is dharani bodytemperature is 99
SyntaxError: invalid syntax
>>> 
>>> 