# x=5
# y=5
# print(id(x))
# print(id(y))

# print(x is y)

# my_list=[1,2]
# my_list2=[1,2]

# print(id(my_list))
# print(id(my_list2))
# print(my_list is my_list2)

# my_list='helo world'
# my_list=my_list.split()
# my_list=my_list.split(',')
# print(my_list)

# fruits=['banana','apple','cherry','kiwi']
# print(fruits[1:3])
# print(fruits[:3])
# print(fruits[1:])
# print(fruits[-3:-1])

# fruits['banana','apple','chery']
# fruits[1]='kiwi'
# print(fruits)

# fruits=['banana','apple','chery']
# fruits.append('orange')
# print(fruits)

# fruits=['banana','apple','chery']
# fruits.insert(1,'orange')#avelacnuma nor andam@ dzer uzac texum
# print(fruits)

# fruits=['banana','apple','chery']
# fruits.remove('apple')
# print(fruits)

# fruits=['banana','apple','chery']
# if 'apple' in fruits:
# 	fruits.remove('apple')
# print(fruits)	

# fruits=['banana','apple','chery']
# # fruits.pop()
# x=fruits.pop()
# print(fruits)

# fruits=['banana','apple','chery']
# del fruits[2]
# print(fruits)
# del fruits#   jnjuma @ndhanur list@ anveradardz
# print(fruits)

# fruits=['banana','apple','chery']
# numbers = [34,56,-457,7.89,-2.23]
# fruits.extend(numbers)#lister@ miavorum e irar
# print(fruits)

# numbers = [34,56,-457,7.89,-2.23]
# numbers.sort()###dasavorume poqric michev mec,is tareri depqum dasavorum @st aybenakan kargi
# print(numbers)

# numbers = [34,56,-457,7.89,-2.23]
# numbers.reverse()
# print(numbers)

# c = [1,2,3,4,5,6,7,8]
# z = []
# for i in c:
# 	if i %2==0:
# 		z.append(i)
# print(z)		


# my_list=[i for i in range(10)]
# print(my_list)

# my_list=[i**2 for i in range(100)if i%2==0]
# print(my_list)

my_list=[1,3,4,5,1,2,3,1]
z=0
for i in my_list:
	if my_list.count(i)>z:
		z=i
print(z)
# c = set([i for i in my_list if my_list.count(i)==z])
# print(c)



# my_list=[1,3,4,5,1,2,3,1]
# print(max(my_list))

# c=my_list[0]
# for i in my_list:
# 	if i>c:
# 		c>i
# print(c)

# print(min(my_list))
# for i in my_list:
# 	if c>i:
# 	   c=1
# print(c)

# print(sum(my_list))
# c=0
# for j in my_list:
# 	c+=j
# print(c)