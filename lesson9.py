# f=1234
# if f%10==4:
# 	print(f)
# f='4321'
# res=f[::-1]#4321 sra ognutyamb frcnum sarqumenq 1234
# print(res)
# while True :
# 	test=input('emaail')
# 	shnikitex=0
# 	for i in test:
# 		if i=='@':
# 			break
# 		shnikitex+=1
# 	print(shnikitex)
# 	ketikitex=0
# 	for y in test:
# 		if y=='.':
# 		break
# 	ketikitex+=1
# 	print(ketikitex)
# 	if shnikitex+1 < ketikitex !=0:
# 		print('mail@ chisht ')
# 		break
# 	else:
# 		print('sxal')
#  while True:
#  	test=input('email')
#  	shnikitex=test.index('@')
#  	ketikitex=test.index('.')
#  	if shnikitex<ketikitex and shnikitex!=0:
#  		print("good test")
#  	else: 
#  		break

# c=0
# x=int(input('mutqagreq tiv@ '))
# for i in str(x):
# 	print(i)
# 	c+=1

# pc=12000/180
# print(pc,'metr varkyanum')
# my=12000/198
# print(my, 'metr varkyanum')

x=int(input('num '))
y=int(input('num '))
if x>y:
	start=x
else:
	start=y
end=x*y+1

count=0
for i in range(start,end,start):
	count+=1
	if i % x == 0 and i % y ==0:
		print(i)
		break
print('count',count)

# x=int(input('num 1 '))
# y=int(input('num 2 '))
# if x>