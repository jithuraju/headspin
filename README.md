<h3>1.Date check without using inbuilt functions</h3>

<h5>introduction:-</h5>python program to check the validity of a date inserted by the user.

<h5>input:-</h5>Date is inserted by the user in form of string stored in variable "date".

<h5>def:-</h5>Function in the program -"datevalidate()", is used to check whether the given date is valid or not.
Function takes 3 arguements - date,month,year that has been given as input.Every month in the year is divided
into 3 groups depending upon number of days in the month.And there is a special case exist when the year is leapyear.
So year is checked to be leap year or not before its totdays in month made set.




<h3>2.Train seat number check</h3>

<h5>introduction:-</h5>python program to check the sleeper seat number of the train.

<h5>input:-</h5>seat number within 72 is inserted by the user.

<h5>def:-</h5>	program have the function named "seatcheck()" to check the seat number upto 72.
Function takes one arguement which is given as input by the user.Since every side-upper seat is a multiple of 8,
a condition is formed for side-upper with modulus operator(%) which gives remainder result as 0.Similarly condions
are formed for side-lower,lower,middle,upper seats depending upon the remainder formed for the modulus operation with 8.




<h3>3.Amstrong number less than N.N is given as command line arguement.</h3>

<h5>introduction:-</h5>python program to print all the amstrong number less than a limit N.(3 digits)

<h5>input:-</h5>Limit N is made input as command line arguement at the time of execution.

<h4>def:-</h4>	sys module is imported in the program for getting the input given at the time of execution as command line arguement
from the list argv.It is accessed by the command 'sys.argv[1]'.
A for-loop is used to iterate over N numbers to find the amstrong number with in it.
A while-loop is used to find the sum of cube of each individual digits in a number.This calculated sum is compared with the value of i in the iteration.If both are same, number belongs to amstrong number.
