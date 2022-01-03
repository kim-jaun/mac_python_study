class Cnt:
    count = 0
    def __init__(self):
        Cnt.count += 1
    @classmethod  # 클래스 변수 사용 가능
    def pr(cls): # cls를 사용하여 클래스변수 사용 가능
        print('클래스 메서드',cls.count)
    @staticmethod
    def prs():
        print("정적 메서드")

cn1 = Cnt()
cn1.pr()
cn1.prs()