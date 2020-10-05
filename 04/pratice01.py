# 3의 배수 판별
import sys
# keyboard module
#pynut
#keyboard
#PyAutoGUI : kyeboard mouse 제어



# 1 3의 배수
param = input('수를 입력하세요: hello')

if param.isnumeric() :
    if int(param) %3 == 0 :
        print('3의 배수 입니다.')
    else :
        print('3의 배수가 아닙니다.')
else :
    print('정수가 아닙니다.')
    sys.exit()

# 2 짝홀

n2 = input('수를 입력하세요:')

if not n2.isnumeric() or int(n2) == 0:
    sys.exit()

if int(n2) % 2 != 0 :
    print('홀수')
else :
    print('짝수')


# 3 diagonal triangle with double 'for in statement'
for i in range(11) :
    print('*' * i)

# 4 Multiplication table
for i in range (2, 10):
    for j in range(2,10):
        print(f'{i} * {j} = {i * j}', sep='\t ')
    print()

# 5 주어진 리스트 데이털르 잉요하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요
l = [10,12,14,15,17,18,19,20,25,30,32,33,37,40,42,44,46,50]

l_sum = 0
l_count = 0
for i in l :
    if i% 3 ==0 :
        l_sum += i
        l_count +=1
else:
    print(f'주어진 리스트에서 3의 배수의 개수 => {l_count}')
    print(f'주어진 리스트에서 3의 배수의 합 => {l_sum}')


# 6  키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전
# 50원짜리 동전, 10원짜리, 동전, 1원짜리 동전 각 몇 개로 변환되는지 작성하시오



def practice6():
    money = input('금액을 입력하세요')
    divider_count_list = [0, 0, 0, 0, 0, 0, 0, 0];
    divider_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    i = 0
    count = 0
    money = int(money)
    target = money

    while True:

        if target >= divider_list[i]:
            target = target - divider_list[i]
            count += 1
        else:
            divider_count_list[i] = count
            count = 0
            i += 1
        if i == len(divider_list):
            break

    print(f'금액:{money}')
    for i in range(0, len(divider_list)):
        print(f'{divider_list[i]}원: {divider_count_list[i]}개')







# 7 키보드에서 5개의 정수를 입력받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
def find_avg_with_five_integer():
    sum = 0
    five_integer_list = []
    for i in range(0,5):
        s = input('정수를 입력하세요. 아니면 종료합니다.')
        if not s.isnumeric() :
            sys.exit()
        five_integer_list[i] = s
        sum += int(s)
    print(sum/5)


# 8
# 문자열을 입력받아 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요


def practive8():
    def reverse(s):
        tmp = ''
        i = len(s)
        while True :
            if i ==0 :
                break
            i = i -1
            tmp += s[i]
        return tmp
    s = input('문자열 입력')
    reverse()
    print(reverse(s))
# 9
# 주어진 if 문을 dict를 사용해서 수정하세요


def pratice9() :
    menu = input('메뉴:')
    list9 = {'오뎅':300, '순대':400, '만두':500}
    print ('가격:{0}'.format( list9.get(menu) if list9.get(menu) else 0 ))

# price(f'가격:{list9.get(menu)}')

# 10
# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요


def pratice10():
    num10 = input('숫자를 입력하세요')
    sum10 = 0
    i10 = 0
    if not num10.isnumeric():
        sys.exit()
    while i < num10:
        if num10%2 != 0 :
            i10 =2*i10-1
            sum10 += i10
        if num10%2 == 0 :
            i10 =2*i10
            sum10 += i10
    else:
        print(f'결과 값 : {sum10}')