
def pratice02_01():
    import re

    s = '/usr/local/bin/python'
    regex =re.findall('\/[1-9a-zA-z]*', s)

    for i in regex:
        print( "'" + i.replace('\/','') +"'", end =' ')
    else: print()

    print("'" +s[:s.rindex('/',1)]+ "'", ' ',"'"+ s[s.rindex('/',1)+1:] +"'")


def practice02_02():
    # re practice
    import re
    string_html= '''<div class="gb_pe">asdsadasdsa<div class="gb_Lc gb_Jc gb_ua"><div class="gb_Uc">asdasdasd<div class="gb_wc"><div class="gb_xc"><a class="gb_Be gb_yc" aria-label="Google" href="/?tab=rr"><span class="gb_va gb_6c" aria-hidden="true"></span></a></div></div></div><div class="gb_Qc"></div></div></div><div class="gb_3d gb_le gb_ce gb_be gb_Dc"><div class="gb_3c gb_ad"><div class="gb_Cc gb_Ja" aria-expanded="false" aria-label="기본 메뉴" role="button" tabindex="0"><svg focusable="false" viewBox="0 0 24 24"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path></svg>'''
    regex = re.findall('\>[a-zA-Z0-9]*\<', string_html)
    regex = set(regex)
    regex.remove('><')
    for i in regex:
        print(i[1:len(i)-2])

def practice02_02_normal():
    string_html = '''<div class="gb_pe">asdsadasdsa<div class="gb_Lc gb_Jc gb_ua"><div class="gb_Uc">asdasdasd<div class="gb_wc"><div class="gb_xc"><a class="gb_Be gb_yc" aria-label="Google" href="/?tab=rr"><span class="gb_va gb_6c" aria-hidden="true"></span></a></div></div></div><div class="gb_Qc"></div></div></div><div class="gb_3d gb_le gb_ce gb_be gb_Dc"><div class="gb_3c gb_ad"><div class="gb_Cc gb_Ja" aria-expanded="false" aria-label="기본 메뉴" role="button" tabindex="0"><svg focusable="false" viewBox="0 0 24 24"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path></svg>'''
    i=0
    start = 0
    list = []
    while True:

        if len(string_html) -1 == i:
            break

        if string_html[i] == '>':
            i += 1
            start = i
            if string_html[i] != '<':
                while string_html[i] != '<':
                    i += 1
                print(string_html[start:i])
        i += 1
def practice02_03():
    import re
    strings = """We encourage everyone to contribute to Pytho. If you still have questions after reviewing the material in this guide, 
    then the Python Mentors group is available to help guide new contributors through the process"""
    results = re.findall('[0-9a-zA-Z]*',strings)
    print(results)

practice02_03()


def practice02_04():
    def sum(*arg):
        sum = 0
        for i in arg :
            for j in i:
                if j not in ['0','1','2','3','4','5','6','7','8','9']:
                    print('정수가 아닙니다.')
                    #sys.exit()
            sum += i
        else : print(sum)

def pratice02_05():
    from random import *
    print('수를 결정하였습니다. 맞추어 보세요')
    number = randint(1,100)
    while True :
        choice = input()
        for i in choice :
            if i  not in ['0','1','2','3','4','5','6','7','8','9']:
                print('정수가 아닙니다.')
                # sys.exit()
        if choice > number :
            print('더 낮게')
        elif choice ==number :
            print('맞았습니다. ')
            continue_yn =input('다시 하시겠습니까(y/n)>>')
            if continue_yn == 'n':
                break
        else :
            print('더 높게')
