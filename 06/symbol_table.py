# global, local symbol table
g_a =1
g_s = '둘리'

def local_symbol():
    l_s = '마이콜'
    print(locals())

# object symbol Table
local_symbol.n = 'hello'
print(local_symbol.__dict__)

# class

class Myclass():
    __x__ = 0
    def __init__(self):
        self.__x__ = 10
        print(id(self), '생성됩니다.')
    x = 10
    y = 10
    def __del__(self):
        print(id(self),'소멸합니다.')

#instance_Myclass =Myclass()
#print(instance_Myclass.x)


#3.내장함수
# 심벌테이블 x -> 확장 x

# 4. 내장 클래스
# symboltable 0 -> 확장 x
#5. 확장 클래스
# symbol table 

class Father():
    __word__ = 'father'
    def __init__(self):
        self.__word__ = 'father'
        print(self.__word__, id(self), '생성됩니다.')
    x = 10
    y = 10
    def __del__(self):
        self.__word__ = 'daddy'
        print(self.__word__, id(self), '소멸합니다..')

class Mother():
    __word__ = 'mother'
    def __init__(self):
        self.__word__ = 'mother'
        print(self.__word__, id(self), '생성됩니다.')
    x = 10
    y = 10
    def __del__(self):
        self.__word__ = 'mommy'
        print(self.__word__, id(self), '소멸합니다..')

# 상속시 생성자에서 발현되는 부모의 생성자는 명시적이지 않으면 먼저 적은 것만 작동된다.
class Child(Father, Mother):
    __word__ = 'child'

    def __init__(self):
        Father()
        Mother()
        self.__word__ = 'child'
        print(self.__word__, id(self), '생성됩니다.')

    x = 10
    y = 10

    def __del__(self):

        self.__word__ = 'yongman'
        print(self.__word__, id(self), '소멸합니다..')


#Child()

class Z:
    def __init__(self):
        print("Z 클래스의 생성자 호출!")


class A:
    def __init__(self):
        print("A 클래스의 생성자 호출!")


class B(A, Z):
    def __init__(self):
        print("B 클래스의 생성자 호출!")
        super().__init__()


class C(A, Z):
    def __init__(self):
        print("C 클래스의 생성자 호출!")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D 클래스의 생성자 호출!")
        super().__init__()

D()


