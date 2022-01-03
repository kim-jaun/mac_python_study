print("아이디를 입력하세요")
id = input()
print("암호를 입력하세요")
pass1 = input()
if id=="root" and pass1=="system":
    print("로그인 성공")
elif id=="root" and pass1 != "system":
    print("암호가 다릅니다")
else:
    print("없는 아이디입니다")
