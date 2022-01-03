# dictionary는 자바의 map과 유사
grade = {'로제':88, '보검':95}
print(grade['로제'], grade['보검'])
print(grade.keys())
print(grade.values())
for k, v in grade.items():
    print(k, '=', v)
# grade.clear()
# print(grade)
for k in grade:
    print(k,'=',grade.get(k))