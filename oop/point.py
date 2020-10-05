class Point:
    count_of_instance = 0  # self 없이 클래스 영역에 선언
    # 모든 인스턴스들이 공유하는 객체

    # 생성자 : 객체의 초기화 담당
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        Point.count_of_instance += 1

    # 소멸자
    def __del__(self):
        Point.count_of_instance -= 1

    # 문자열 연결 or 출력시 호출되는 내부 메소드(일반사용자용)
    def __str__(self):
        # 출력 포멧을 return
        return "Point x={}, y={}".format(self.x, self.y)

    # repr의 return 값을 가지고 eval 을 실행하면 원래 객체가 튀어와야 한다. 코드 검증용 문자 출력 역할
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __enter__(self):
         # with 구문이 시작될 때 호출된다.
        return self

    # def __exit__(self, exc_type, exc_val, exc_tb):  # with 구문 종료될 때
    #         pass

    # 연산자 오버로딩
    # 새로운 클래스를 만들었다는 것은 새로운 자료형을 만들었다는 의미
    #   새 자료형에 대한 연산자의 작동 방식을 작성할 필요가 있다.
    def __add__(self, other):
        # Point(x,y) + other
        if isinstance(other, (int, float)):  # other의 type 체크
            return Point(self.x+other, self.y + other)
        elif isinstance(other, Point):  # other가 Point
            return Point(self.x + other.x, self.y + other.y)
        else:
            return self + other

    # 역이행 연산자, 연산자 끝나고 연산자에서 코드 실행이 불가능할 경우 역이행 연산자가 동작된다.
    # other - Point(x, y)
    def __radd__(self, other):
        # Point(x,y) + other
        if isinstance(other, (int, float)):  # other의 type 체크
            return Point(self.x + other, self.y + other)
        elif isinstance(other, Point):  # other가 Point
            return Point(self.x + other.x, self.y + other.y)
        else:
            return self + other

    def __sub__(self, other):
        # Point(x,y) + other
        if isinstance(other, (int, float)):  # other의 type 체크
            return Point(self.x - other, self.y - other)
        elif isinstance(other, Point):  # other가 Point
            return Point(self.x - other.x, self.y - other.y)
        else:
            return self - other

    def __eq__(self, other):
        # Point(x, y) == other
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return self == other

    def set_x(self, x):  # 인스턴스 메서드의 첫번째 인자는 self
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self):
        print("점 ({}, {})  를 그렸습니다.".format(self.x, self.y))

    @classmethod
    def get_count_of_instance(cls):  # cls -> class 객체의 참조 주소
        return cls.count_of_instance

    # class namespace 안쪽에 있을 뿐
    # class 멤버와는 전혀 연관 없는
    @staticmethod
    def static_method():
        print("static method 호출")


# 상속
# 부모로부터 member를 물려받은 이후, 필요한 부분만 추가 구현
# 부모가 가진 method를 재정의한다.
class ColorPoint(Point):  # 부모가 Point인 subclass
    def __init__(self, x=0, y=0, color='black'):
        super().__init__(x, y)  # 부모 생성자 호출
        self.color=color

    def draw(self):
        print("{}색 점({}, {}) 을 그렸습니다.".format(self.color, self.x, self.y))

    def __str__(self):
        return("ColorPoint({}, {}, {})".format(self.x, self.y, self.color))
