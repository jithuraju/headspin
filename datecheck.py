date=str(input("enter the date to be validated in dd/mm/yyyy:"))
#print(len(date))
dd=int(date[:2])
mm=int(date[3:5])
yyyy=int(date[6:])
print("date is:",dd)
print("month is:",mm)
print("year is:",yyyy)

def datevalidate(dd,mm,yyyy):
	month1=[1,3,5,7,8,10,12]
	month2=[4,6,9,11]
	month3=[2]

	if mm in month1:
		totdays=31
	elif mm in month2:
		totdays=30
	elif mm in month3 and (yyyy%4==0 and yyyy%100!=0) or (yyyy%400==0):
		totdays=29
	else:
		totdays=28

	if(yyyy>=2020 and mm>=5 and dd>24):
		print("it is a future date....")	
	elif(mm<1 or mm>12):
		print("invalid date..")
	elif(dd<1 or dd>totdays):
		print("invalid date...")	
	else:
		print("valid date...")	


datevalidate(dd,mm,yyyy)						