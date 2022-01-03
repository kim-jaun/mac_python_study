year = 2016
month = 1
day = 16
day_of_week = "일"
# "오늘은 2016년 1월 16일 일요일입니다." 출력
print("오늘은 %d년 %d월 %d일 %s요일입니다." %(year,month,day,day_of_week))
print("오늘은 {}년 {}월 {}일 {}요일입니다.".format(year,month,day,day_of_week))
print(f"오늘은 {year}년 {month}월 {day}일 {day_of_week}요일입니다.")
# %%는 %
print("에러가 %d%%입니다" % (80))
# 10s는 10칸을 확보하고 뒤에 부터 글자 hi를 채워라
print("%10s" % ('hi'))
# -10s는 10캄을 확보하고 앞에서 부터 글자 hi를 채워라
print("%-10sjane" % ('hi'))
print("%.2f" % (3.1415923))
# %10.2f 10칸을 확보하고 뒤에 부터 실수 소숫전 2자리까지 출력하라
print("%10.2f" % (3.1415923))