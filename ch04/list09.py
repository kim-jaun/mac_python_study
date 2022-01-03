data = ['Morning','Afternoon','evening','Night']
# assii 값 A 65, a 97 즉 소문자가 크다
data1 = sorted(data)
print(data1)
data.sort(reverse=True)
print(data)
# 대소문자 구별하지 않고 큰순
data.sort(key=str.lower,reverse=True)
print(data)
# def 함수, 메서드
def strlen(s):
   return len(s)
print(strlen('대박사건'))
data.sort(key=strlen)  # 글자수가 작은 것부터 정열
print(data)