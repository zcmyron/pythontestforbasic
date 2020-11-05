import re
############################################################################################
# message='Hi there, this is Daniel Zhai, please reply me at 86-18888888888.'
#
# find_phone_number=re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d\d')
# match_object=find_phone_number.search(message)
#
# # print(match_object)
#
# print(match_object.group())

############################################################################################
# message='Hi there, this is Daniel Zhai, please reply me at 86-18888888888, or 86-17777777777.'
#
# find_phone_number=re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d\d')
# match_object=find_phone_number.findall(message)
#
# # print(match_object)
#
# print(match_object)

############################################################################################
# message='Hi there, this is Daniel Zhai, please reply me at 86-18888888888, or 86-17777777777.'
#
# find_phone_number=re.compile(r'(\d\d)-(\d\d\d\d\d\d\d\d\d\d\d)')
# match_object=find_phone_number.search(message)
#
# # print(match_object)
#
# print(match_object.group(2))
############################################################################################
# message='Hi there, this is Daniel Zhai, and my wechat is Daniel Zhang, please reply me at 86-18888888888, or 86-17777777777.'
#
# Daniel_Regex=re.compile(r'Daniel (Zhai|Zhang|test)')
# match_object=Daniel_Regex.findall(message)
# print(match_object)
############################################################################################
