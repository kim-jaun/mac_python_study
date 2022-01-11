import time, threading, requests
def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, resp.text)
print("보고싶은 인터네 주소")
u1 = input()
th = threading.Thread(target=getHtml, args=(u1,))
th.start()
print("작업 종료")