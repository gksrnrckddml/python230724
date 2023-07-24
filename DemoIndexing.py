# DemoIndexing.py
strA = "python is very powerful"
print(strA[0] )
print(strA[1])
print(strA[0:3])
# 축약된 약식 표현식
print(strA[:3])
#디버깅 하지 않고 바로 샐행 ctrl+F5
print(strA[-3:])
print(strA[-8:])

#리스트 연습
colors = ["red", "blue","green"]
print (colors)
print(len(colors))
print(colors[0])

# 디버깅 할 때 중단점(Break Point)
for item in colors:
    print(item)


# .을 찍으면 auto
colors.append("white")
print (colors)
colors.insert(1,"pink")
print(colors)
print (colors.index("red"))
colors += "red"
print( colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)
print(colors.pop())
print(colors)
colors.extend(["black","red","white","pink"])
print(colors)
colors.remove("black")
#sort는 순서대로 정렬하기(숫자는 작은수부터)
print(colors)
colors.sort()
print(colors)
#reverse는 역순으로 정렬하기
colors.reverse()
print(colors)


print("---dict---")
color = {"apple":"red", "banana":"yellow"}
print(len(color))
print(color["apple"])
color["cherry"] = "red"
print(color)


