# 리스트는 대괄호, 튜플은 소괄호, 딕셔너리는 중괄호 사용
# 딕셔너리는 키-값 쌍으로 이뤄져 있다

# player라는 딕셔너리를 만들어서 이 안에 name, age, alive 라는
# 속성을 만든 것이다.
player = {'name': 'pubao', 'age': 8, 'alive': True, 'fav_food': ['🍒', '🥕']}

print(player.get('age'))

# 딕셔너라 용도와 리스트의 용도는 아예 다르다
# : 숫자 목록이나 todo 목록, 어떤 목록이 있다면 그건 리스트나 튜플이 될 수 있다.
# 딕셔너리는 많은 속성들을 가지고 있는 데이터를 만들때 사용한다

# 딕셔너리를 생성한 이후 데이터를 추가하는 방법
# : 딕셔너리는 리스트가 변경 가능했던 것처럼 변경이 가능하다

# example_1
print(player)
print(player.pop('age'))
print(player)

# example_2
player['fav_food'].append("🍜")
print(player.get('fav_food'))
print(player['fav_food'])
