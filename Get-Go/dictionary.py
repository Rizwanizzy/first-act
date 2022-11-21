dict1 = {
    1: 'iphone',
    2: 'realme',
    3: 'samsung'
}
dict1[4] = 'honor'
for i in dict1:
    print(dict1[i])
print('===================')
# dict1.popitem()
# del dict1
dict2 = dict1.copy()
for i in dict2:
    print(dict1[i])
print('===============')
dict3 = dict(a='rizwan', b='azif', c='sameer')
for i in dict3.items():
    print(i)
