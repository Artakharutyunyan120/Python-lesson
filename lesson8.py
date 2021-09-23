# x=range(10)
# for i in x:
# 	print(i)

# x=range(10)
# for i in x:
# 	 print(i,end='')#(end='')print aracner@ outputm irar koxqic tpi

# for j in 'Ani':
# 	print(j)

# x=range(100)
# for i in x:
# 	if i == 5:
# 		break
# 	print(i,end='')

# x='Aram'
# for i in 'Aram':
# 	if i =='a':
# 		continue
# 	print(i)

x=range(50)
for i in x:
	if i%2==0:
		continue
	print(i,end='')

# x=range(1,50,2)
# for i in x:
# 	print(i,end='')

# for i in x:
# 	pass #pass vor grumes kod@ stugeluc error chi talis,aranc passi kodi el mnacac hatvac@ chi ashxati


# Nested loops
# color= 'red'
# fruits= 'apple'
# for x in color:
# 	for y in fruits:
# 		print(x,y)

# x=1
# while True:
# 	x+=1
# 	print(x)
# 	if x == 18:
# 		break

# x = 1
# while x<17:
# 	x+=1
# 	print(x)

# i = 1
# while i<6:
# 	print(i)
# 	i+=1

# x=0
# while True:
# 	x+=1
# 	if x%10==0:
# 		continue
# 	print(x)

# name = 'Visual'
# for i in name:
# 	if i == 's':
# 		continue
# 	elif i =='s':
# 		break
# 	else:
# 		print(i,end='')
# 		

# import time
# import os
# while True:
# 	localtime =time.localtime()
# 	result=time.strftime('%I:%M:%S %p',localtime)
# 	os.system("clear")
# 	print(result)
# 	time.sleep(1)

# while True:
# 	age =input('Age ')
# 	if age.isdigit():
# 		age=int(age)
# 		print('Good',age,type(age))
# 		break
# 	print('enter a number')

# while True:
# 	name=input('name')
# 	if name.isalnum():
# 		name='name'
# 		print('Goode',name,type(name))
# 		break
# 	print ('enter a name')

# while True:
# 	name=input('name')
# 	for i in name:
# 		if i in '!@#$$%^&**(()_+':
# 			print('enter a name')
# 			break
# 	else:
# 		print('good',name,type(name))
# 		break