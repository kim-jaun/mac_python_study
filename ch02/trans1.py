in1  = 'abcdef'
out1 = '123456'
trans = ''.maketrans(in1, out1)
str = "hello world korea"
# str의 문자를 trans기준으로 변경하라
print(str.translate(trans))