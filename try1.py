#try1.py
def divide(a,b):
    return a/b

# result=devide(5,0)


try:
    result = divide(5,"aaa")
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("형식이 숫자여야 합니다.")
else:
    print("결과:{0}".format(result))
finally:
    print("무조건 실행")
print("전체 코드 종료")