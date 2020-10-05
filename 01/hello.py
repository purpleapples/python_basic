numbers = set(range(1,10) )
odds = set(range(1,10,2))

print(numbers, "는", odds, "의 모집합?", numbers.issuperset(odds))
print(odds, "는", numbers, "의 부분집합?", odds.issubset(numbers))

# zip 의 내부 데이터는 출력될때 pop 된다.
x = range(1, 8)
y = range(1, 8)
z = zip(x,y)
print(z)
for i in z:
    print(i)
    break

print(z)


for i in z:
    print(i)