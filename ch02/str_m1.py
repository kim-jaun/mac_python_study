#     01234
a1 = "Hello"
print(a1.startswith("H"))  # startswith 시작하는 문자
print(a1.startswith("K"))

print(a1.endswith("lo"))  # endswith 끝나는 문자
print(a1.endswith("Ko"))

print(a1.find("l"))  # l이있는 index
print(a1.find("k"))  # 찾는 값이 없으면 -1

print(a1.rfind("l")) # rfind 뒤부터 찾아서 첫번째 발견된 index
print(a1.count("l")) # 해당하는 문자의 갯수

print("   대박".lstrip()) # 왼쪽의 공란을 지워라
print("대박   ".rstrip()) # 오른쪽의 공란을 지워라
print("   대박   ".strip()) # 좌우의 공란을 지워라