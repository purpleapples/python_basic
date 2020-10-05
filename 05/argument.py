# 집합관련함수

s4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s5 = {10, 20, 30}
s6 = s4.union(s5)
print(s6)
s7 = s4.intersection(s5)
print(s7)
s8 =s4.difference(s5)
print(s8)
s9 = s4.symmetric_difference(s5)
print(s9)

# packing 은 tuple 만 가능

# unpacking 확장
t2 = (1,2,3,4,5)
a, *b = t2
print(a, b, sep = '  ')


# dict
d1 = dict(one=1,two=2)
print(d1)
d2 = dict([('three', 3),('four', 4)])
print(d2)

# dict : 다양한 type의 key, tuple 도 가능, dict, set, list는 불가
d3 = dict()
d3[True] = False
d3[3] = 4
print(d3)



#
phones = {}
v = phones.setdefault('둘리', '555-5555-55555')
# return value:str
print(v)
v = phones.get('dd')
# return None if phones.get('key') == ''

# clear()
phones.clear()
# delete all context
# select
d7 = {'c': 3, 'a': 1, 'b': 2}

# default : key
for k in d7 :
    print(k, end = ' ')

# enumerate() : Sequential object 의 element에 index를 부여
# zip() : 여러개의 object를 하나로 묶는다. 주로 for  in 문에서 in에 여러개의 인수를 쓰고 싶을때 사용하며
# loop 마다 나오는 것은 unpacked objects 이다. sequential object의 경우 index 기준으로 tuple로 묶는다.

print()
list_even = [ i for i in range(1, 101) if i% 2 ==0 ]
print(list_even)

# 1
something = []
lenth_list = [len(s) for s in something ]
# 2 list comprehension
sam69= [i for i in range(1, 101) ]
# 3 set comprehension
sss = { i for i in range(1,101) }
# dict comprehension
strings = 'asdsadasda'
d= {s: len(s) for s in strings}



