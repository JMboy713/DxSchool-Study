# 고객의 니즈가 변경
# 업무 로직과는 관계가 없는 로깅을 출력하는 코드를 추가하기를 원함.
# 유지보수 과정이나 업무로직과 관련이 없는 코드를 추가하거나 삭제하는 경우 업무 로직을 직접 수정하는것은 예상치 못한 결과를 만들어 낼 수 있다.
# 이러한 경우엔 업무 로직은 손을 대지 않고 가능하도록 만드느것이 좋다.

# def decorator(func):
#     func()
#     print("로깅")

# @decorator
# def businessLogic():
#     print("업무로직")

# businessLogic

# 함수를 호출할 때 마다 실행에 걸린 시간,인수,매개변수,리턴 값을 출력하는 decorator 생성
import time
import functools


def function1(func):
    # decorator가 적용된 함수가 호출되면 수행될 실제 함수.
    def clock(*args):
        start = time.time()
        # 업무 로직 함수를 호출
        result = func(*args)

        end = time.time()
        print(end - start)
        # 매개변수 확인
        print("매개변수:", args)
        # 결과값 확인
        # print(result)
        return result

    return clock


@functools.lru_cache
@function1
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(50))
