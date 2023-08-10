# 이름과 점수를 갖는 객체를 여러개 사용해야 하는 경우
class Student:
    # 접근자 메서드
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def getScore(self):
        return self.score
    def setScore(self,score):
        self.score=score
        
s=Student()
s.setName("아담")
s.setScore(97)
# getter를 이용한 속성 사용
print(s.getName())
# 최근에 등장한 IDE는 대부분 getter와 setter만드는 유틸을 제공함 