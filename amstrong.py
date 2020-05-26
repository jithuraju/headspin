import sys
print(sys.argv)
n=int(sys.argv[1])
print("limit is:",n)
print("amstrng numbers are:")
for i in range(1,n):
	sum=0
	temp=i
	while (temp>0):
		d=temp%10
		sum=sum+(d**3)
		temp =temp//10

	if(i==sum):
		print(i)	