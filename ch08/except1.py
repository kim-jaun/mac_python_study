print("정수를 입력하세요")
try : 
    num = int(input())
    print(f"10/{num} : {10/num:.2f}")
except ZeroDivisionError as err:
    #print("0으로 나눌수 없습니다")
    print(f"{err}")
except :
    print("에러가 발생했습니다")
else:   # 에러가 없을 때 실행
    print("잘 했어")
finally:    # 에러 여부에 관계없이 무조건 실행
    print("난 무조건이야")