student = {}

student['홍길동'] = '010-1111-1111'
student['이순신'] = '010-1111-2222'
student['강감찬'] = '010-1111-3333'

print('아래 학생들의 전화번호를 조회할 수 있습니다.')

for i in student.keys():
    print(i)
print('전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.')

name = input().strip()

print('{}의 전화번호는 {}입니다.'.format(name, student.get(name)))

# print(student.get('강'))