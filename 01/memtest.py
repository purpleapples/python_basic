
x = 10
y = 20
tmp = x

print('before')
print(id(x))
print(id(tmp))

x += x

print('after')
print(id(x))
print(id(tmp))

print('confirm that numeric valus are immutable?')
print(x)
print(tmp)

# symbolic tables
# 구조 : variable name, reference id, scope
# content return : dict

# 계층
# Global Symbol table : 안에 전역변수 및 class 에 대한 symbol 및 reference id
# class reference id -> class symbol table
# block 단위에서 생성된 객체 -> locals symbol table 생성 : block 끝나면 사라짐

# 내장 함수
# 내장함수의 경우 symbol tale 존재하지 않는다. built-in class의 object는 존재하나 확장 불가

# name space로 접근할 경우와 symbol table로 접근하는 경우는 차이가 있다.






