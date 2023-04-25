# range() 함수를 사용하는 이유

a = [n for n in range(1000)]
b = range(1000)

# len(a) == len(b)

import sys


# range를 사용한 쪽이 메모리 사용율이 월등히 적은것을 알 수 있다.
print(sys.getsizeof(a))
print(sys.getsizeof(b))

