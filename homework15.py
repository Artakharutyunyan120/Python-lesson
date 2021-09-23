# x=['aplle','lenov','hp','sony']
# if 'hp' in x:
# 	print(True)
# else:
# 	print(False)

# x=[12,21,15,19,8]
# for i in x:
# 	if i%2==0:
# 		print(i,end=',')

x=[12,12,8,21,15,19,8]
for i in x:
# 	#print(i)
# 	if x.count(i)!=1:
# 	remove(i)
res=[i for i in x if x.count(i)==1]
print(res)