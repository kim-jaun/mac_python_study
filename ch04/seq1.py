#      01234
str = "Korea"
#        -2-1
print(str[0]) #0번째 글자   K
print(str[-2]) #뒤에서 2번째 글자 e
print(str[1:3]) #1번째부터 3번째 글자 앞까지  or
print(str[0:5:2]) #0부터 5번째글자 앞까지 2개씩 건너뛰면서 Kra
print(str[:-1])#가장 마지막 글자를 제외하고
print(str[::-1])#반대로 출력 aeroK
str = "Hello" + "World"
print(str)  # HelloWorld
str = str * 4
print(str)  # HelloWorldHelloWorldHelloWorldHelloWorld