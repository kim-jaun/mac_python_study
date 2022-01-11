import time, threading, requests
class HttpGett(threading.Thread):
    def __init__(self, url): # 매개변수는 생성자를 통하여 받는다
        threading.Thread.__init__(self)
        self.url = url
    def run(self):  # url을 매개변수 받을 수 없기 때문에 생성자를 통하여 받는다
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, resp.text)
print("보고싶은 인터네 주소")
u1 = input()
th = HttpGett(u1)
th.start()