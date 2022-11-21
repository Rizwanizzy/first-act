set1 = {'rizwan', 'thanseel', 'ubaid', 'azif'}
# print(set1)
# for i in set1:
#     print(i)
# print('nabeel' in set1)
# set1.add('nabeel')
set2 = {'sameer', 'azif', 'prajith'}
# set1.update(set2)
# set1.remove('sameer')
# set1.pop()
# del set1
# print(set1)
# set3=set1.union(set2)
set3 = set1 | set2
# # set3=set1-set2
# print(set3)
print(sorted(set3, reverse=True))
