# fruits = {'apple', 'orange', 'banana', 'grapes'}
# # print(fruits)
# # # fruits[2]='pineapple'
# # # print(fruits)
# # # print('pineapple' in fruits)
# # print(len(fruits))
# # fruits.insert(1,'pineapple')
# # print(fruits)
# # print(len(fruits))
# # print(fruits.index('grapes'))
# # for i in fruits:
# #     print(i)
# fruits[1] = 'mango'
# print(fruits)
dict = {
    'name:': 'rizwan',
    'age:': 25,
    'location:': 'kochi',
}
for i, j in dict.items():
    print(i, j)
print('==================')
dict['num:'] = 9037
for i, j in dict.items():
    print(i, j)
print('==================')
del dict['age:']
for i, j in dict.items():
    print(i, j)
