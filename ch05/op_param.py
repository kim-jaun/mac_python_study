# natonality에 값이 넘어오면 그 값으로 , 값이 안오면 한국
# optional parameter
def myself(name, age,natonality="한국"):
    print("이름 :",name)
    print("나이 :",age)
    print("국가 :", natonality)

myself('보검',25,'미국')
myself('로제',23)