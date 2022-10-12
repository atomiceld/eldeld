#ifelse.py
score = int(input("점수를 입력하시오-->"))
if 90 <= score <= 100:
    grade ="AAA"
elif 80 <= score <= 90:
    grade ="BBB"
elif 70 <= score <= 80:
    grade ="CCC"
else :
    grade ="바보 낙제"

print("등급은",grade,"입니다.")
