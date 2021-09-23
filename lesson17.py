students={'Artak':10,
		  'Arsen':15,
	      'Arman':7,
	      'Karen':8,
	      'Narek':12,
	      'Ando':5,
	      'Ararat':4,
	      'Arus':3,
	      'Anna':2,
 	      'Ashot':1
}
# for i in students:
# 	if students[i] >9:
# 		print(i,students[i])
# count_raiting=0
# lenght=0
# for i in students:
# 	lenght+=1
# 	count_raiting+=students[i]
# res=count_raiting/lenght
# print(res)

# shem=10
# gnahatakan=0
# for i in students:
# 	if students[i]<10:
# 		res=10-students[i]
# 		print(i,res)


# students={'Artak':10,
# 		  'Arsen':15,
# 	      'Arman':7,
# 	      'Karen':8,
# 	      'Narek':12,
# 	      'Ando':5,
# 	      'Ararat':4,
# 	      'Arus':3,
# 	      'Anna':2,
#  	      'Ashot':1
# }

# x=input('mutqagreq anun@: ')

# if x in students:
# 	print('ayo',x,students[x])
# else:
# 	print('no')


s='a,2,b,5,c,8,a,4,e,11'.split(',')
res={}
for i in range(0,len(s),2):
	if s[i] in res:
		res[s[i]]+=int(s[i+1])
	else:
		res[s[i]]=int(s[i+1])
print(res)

# word='exercises'
# res={}
# for i in word:
# 	res[i]=word.count(i)
# print(res)

old_list=[{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# new_list=[]
# for i in old_list:
# 	if i not in new_list:
# 		new_list.append(i)
# print(new_list)
c=0
for i in range(len(old_list)):
	if old_list.count(old_list[c])>1:
		old_list.remove(old_list[c])
	else:
		c+=1
print(old_list)

# x=['1','2','3','4','5','6','7','8']
# y=[]
# for i in range(0,len(x),2):
# 	res=x[i]+x[i+1]
# 	y.append(res)
# print(y)


questions={
	'question 1':{
		'q':['When was the battle of Avarayr\na)160 b)400 c)451 d)452','c'],
	},
	'question 2':{
		'q':['what is hight of Everest \na)8000 b)8400) c)5451) d)8849','d'],
		}
}
for i in questions:
	print(i)
	print(questions[i]['q'][0])
	ans==(int(input('ans:'))
	if ans==questions([i]['q'][0]['c']):
		print('laver')

		


	




