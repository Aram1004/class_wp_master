a,b,c = input("입력값을 3개 입력하세요").split()

print(a)
print(b)
print(c)

kor,eng,math,scien = map(int, input("국어, 영어, 수학, 과학 점수를 입력하세요: ").split())
print(int((kor+eng+math+scien)/4))

print(1)
print(2)
print(3, end='')
print(4)

print("Hello",'\n','python',sep='')
