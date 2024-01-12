day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
"""
프로그래밍 언어에서 modify(수정하다)는 mutate(변화시키다)는 의미이다
"""

# 리스트와 결합된 메소드
print(day_of_week.count("Wed"))
day_of_week.clear()
day_of_week.reverse()
day_of_week.append("Sat")


# 리스트 장점 : 데이터 가공에 도움을 주는 메소드들을 사용이 가능하다

# 리스트에 있는 특정 아이템에 접근할 수 있는 방법
# : 대괄호안에 내가 접근하고 싶은 아이템의 인덱스를 넣어주면 된다.
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(day_of_week[2])