print("점수를 입력하세요")
score = int(input())
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)
message = "success" if score >= 60 else "failure"
print(message)