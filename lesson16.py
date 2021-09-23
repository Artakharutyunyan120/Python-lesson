# Nver_Adrine={
# 	'taretivy_canotutyan':2021,
# 	'Nveri_hooby':'Table Tennis',
# 	'age':20,
# 	'years':(2000,2002),
# 	'year':{
# 		'Nver':2000,
# 		'Adrine':2002
# 	}
# }

# for i in Nver_Adrine:
# 	print(i,Nver_Adrine[i])

# for i in Nver_Adrine.keys():
# 	print(i,Nver_Adrine[i])

# for i in Nver_Adrine.values():
# 	print(i)

# for i,j in Nver_Adrine.items():
# 	print(i,j)





# Nver_Adrine['age']=19
# Nver_Adrine['Arajin_nvery']='duxi'
# print(Nver_Adrine)

# # print('Nveri age is',Nver_Adrine['age'],
# # 	'taretivy_canotutyan',Nver_Adrine['taretivy_canotutyan'],
# # 	Nver_Adrine['years'],

# # 	'Nver year is',Nver_Adrine['year']['Nver'],
# # 	'Adrine year is',Nver_Adrine['year']['Adrine'])

# # c=Nver_Adrine.popitem()
# # print(c)


# # ####len()
# # thisdict={'name':'Aram','year':1994}
# # print(len(thisdict))

# # thisdict=dict(brand='ford',model='mustang',year=1964)


# # thisdict={'name':'Aram','year':1994}
# # del thisdict['year']
# # print(thisdict)


students={'Artak':9,
		  'Ararat':10,
		  'Arsen':8,
		  'Anna':4,
		  'Jenni':7}
lavaguyn = 0

for i in students.values():
	if i > lavaguyn:
		lavaguyn=i

for i in students:
	if students[i]==lavaguyn:
		print(i,lavaguyn)
