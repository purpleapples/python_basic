a=23
a = 20 +3

print(a, type(a))
print(isinstance(a, int))

# 2진수, 10진수, 8진수, 16진수
b = 0b1101
c = 0o23
d = 0x23

print(b,c,d,sep='  ')

#is_integer :float object가 저장한 value의 decimal 존재여부 판별
b = 2.0
print(type(b))
print(b.is_integer())

c=3e3
print(c)
d=0.2e-4
print(d)

# complex :  real number + imaginary number
a= 4 + 5j
print(a, type(a))

b = 7 -2j
print(a + b )

# divmod()

t = divmod(2, 3)
print(t,type(t))

# indentity, homogeneity
# identity
a = 2
b = 2
print(a == b)
# homogeneity
print(a is b)
print(id(a), id(b) ,sep=' ')
# 이 결과는 mutable 과 imutable을 확인하기 위한 수단이다.

l1 = [10,20,30]
l2 = [10,20,30]
print(l1 == l2)
print(l1 is l2)
print(id(l1), id(l2) , sep=' ')
# 결국은 id 값에 대한 비교이다.