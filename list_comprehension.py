# 리스트 뿐만 아니라 딕셔너리도 가능하다...

# 리스트 컴프리헨션을 사용하지 않는 경우
a = []
for n in range(1, 11):
    if n % 2 == 1:
        a.append(n*2)
print("사용전: ", a)

# 사용한 경우
b = [n*2 for n in range(1, 11) if n % 2 == 1]
print("사용후: ", b)

# 훨씬 코드가 깔끔하다.
