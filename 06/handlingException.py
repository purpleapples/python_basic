def handling_exception():
    lst = []

    try:
        print("예외 가능 코드 블록")
        if len(lst) > 3:  # 방어 코드
            lst[3] = 1
        result = 4 / 0
        int("string")
    except IndexError as e:
        print(e, type(e))
    except ZeroDivisionError as e:
        print(e, type(e))
    except ValueError as e:
        print(e, type(e))
    except IndexError as e:
        print(e, type(e))
    finally:
        print("예외 처리 종료")

    print("End of COde")


def caller():  # 호출하는 함수
    try:
        result = callee(4, 0)
    except ZeroDivisionError as e:
        print(e, type(e))
    else:
        print(result)


def callee(a, b):  # 호출되는 함수
    """
    호출 되는 함수는 내부에서 완벽하게 예외를 처리해 복구하기 힘들다면
    호출한 함수로 예외처리를 위임하는 것이 더 좋다
    raise 예외객체
    """
    if b ==0:
        raise ZeroDivisionError("0으로 나눌 수 없어요")

if __name__ == "__main__":
    #handling_exception()
    caller()