# DemoStr.py
# print( dir(str) )

strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.count("p"))
print(strB.count("p", 7))
print(strB.startswith("python"))
print(strB.endswith("ful"))
result = strB.upper()
print(result)
result2 = result.lower()
print(result2)
data = "  spam and ham  "
result = data.strip()   #strip은 앞에 있는 쓸데없는 띄어쓰기 없애줌
print(data)
print(result)
