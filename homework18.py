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
#     if students[i]>9:
#         print(i,students[i])

# gnahatakaneri_qanak = 0
# erkarutyun = 0
# for i in students:
#     erkarutyun+=1
#     gnahatakaneri_qanak+=students[i]
# res=gnahatakaneri_qanak/erkarutyun
# print(res)


# for i in students:
#         if students[i] <10:
#                 res=10-students[i]
#                 print(i,res)

# for i in students:
#         if students[i]>=10:
#                 print(i,students[i])


# for i in students:
#         if students[i]>=5:
#                 print(i,students[i])


# for i in students:
#          if students[i]<=5:
#                  print(i,students[i])

# x=input('name: ')
# if x in students:
#         print(x,students[x])


# s = 'a,2,b,5,c,8,a,4,e,11'.split(',')
# res={}
# for i in range(0,len(s),2):
#         if s[i] in res:
#                 res[s[i]]=res[s[i]]+int(s[i+1])
#         else:
#                 res[s[i]]=int(s[i+1])
# print(res)


# word = 'exercises'
# res={}
# for i in word:
#         res[i]=word.count(i)
# print(res)

# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# nwe_list=[]
# for i in old_list:
#         if i not in nwe_list:
#                 nwe_list.append(i)
# print(nwe_list)



# x=['1', '2', '3', '4', '5', '6', '7', '8']
# y=[]
# for i in range(0,len(x),2):
#         res=x[i]+x[i+1]
#         y.append(res)
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
        #print(i)
        print(questions[i]['q'][0])
        # ans==(int(input('ans:'))
        # if ans==questions([i]['q'][0]['c']):
        #         print('laver')