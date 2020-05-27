n=int(input("enter the seat number to be checked"))
def seatcheck(n):
	if(n%8==0):
		print("your seat ",n," is in SU-Side Upper")
	if(n%8==7):
		print("your seat ",n," is in SL-Side Lower")
	if(n%8==1 or n%8==4):
		print("your seat ",n,"is in L-Lower")
	if(n%8==2 or n%8==5):
		print("your seat ",n," is in M-Middle")
	if(n%8==3 or n%8==6):
		print("your seat ",n," is in U-Upper")	
	if(n>72):
		print("invalid seat number")				
seatcheck(n)