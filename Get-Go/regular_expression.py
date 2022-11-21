import re
# pattern=r"rizwan"
# sentence="hello rizwan , how r u?,how was the day rizwan,hope u feeling gud rizwan"
# new="azif"
# sentence1="rizwan hello  , how r u?"
# # if re.match(pattern,sentence1):
# #     print("found")
# # else:
# #     print("not found")
# # if re.search(pattern,sentence1):
# #     print("found")
# # else:
# #     print("not found")
# # print(re.findall(pattern,sentence))
# print(re.sub(pattern,new,sentence))
pattern=r"[A-Z][a-z][a-z][0-9]"
if re.search(pattern,"Riz9"):
    print("matched")
else:
    print("not matched")