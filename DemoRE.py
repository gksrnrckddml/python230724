# DemoRE.py
# ^는 carrot

import re

#숫자가 0에서 n번 th
result = re.search("[0-9]*th", "  35th")   #앞에 있는 게 찾고 싶은 것 , 35th앞에 빈칸이 있어도 찾을 수 있음
print(result)
print(result.group())

#선택블록: ctrl+/
#result = re.match("[0-9]*th", "  35th")
#print(result)
#print(result.group())

result = re.search("apple", "빅테크에서 apple의 위상")
print(result.group())
result = re.search("\d{4}", "올해는 2023년")
print(result.group())
result = re.search("\d{5}", "우리 동네는 42300")
print(result.group())


print("---대소문자---")
data = ("Apple is big complany and apple is very delicious")
c = re.compile("apple", re.IGNORECASE)
print(c.findall(data))

print("---다중라인검색---")
data2 = """파이썬을
배워서

누구나 사용"""
c = re.compile("^.+", re.MULTILINE)
print(c.findall(data2))
