# list1=[1,2,3,4,5,6,7,8,9,23]
# c=0
# for i in list1:
# 	c+=i
# print(c)

# c=1
# list1=[1,2,3,4,5,6,7,8,9,23]
# for i in list1:
# 	c*=i
# print(c)


# list1=[8,9,10,11,12]
# list2=[1,2,3,4,5,8]
# list1.extend(list2)
# # print(list1)
# c=0
# for i in list1:
# 	if list1.count(i)>c:
# 		c=i
# print(str(c) +' e')

list1=[8,9,10,11,12]
list2=[1,2,3,4,5,8]
for i in list1:
	if i  in list2:
		print('ka')
	else:
		break