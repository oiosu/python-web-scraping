# **build-in 함수
age = input("how old are you?")

# type 함수 _ 변수의 type을 알려주는 함수
type(type(age))

# 타입을 변경하고 싶다면 다음과 같이 작성하기
# int는 user가 작성한 string을 받고 int는 그 string을 숫자로 바꿔준다.
your_age = int(input("how old are you?"))

# 음주 나이 계산기 example 1
# 18세 미만이면 술을 마실 수 없다.
if your_age < 18:
  print("you can't drink")
# 그런데 만약 user가 18세 이상이고 and 동시에 35세 미만인 경우
# and 사용은 양쪽(앞,뒤) 모두 true 이어야 한다.
elif your_age >= 18 and your_age <= 35:
  print("you drink beer!")
else:
  print("go ahead!")

# 음주 나이 계산기 example 2
if your_age < 18:
  print("you can't drink")
elif your_age >= 18 and your_age <= 35:
  print("you drink beer!")
# or는 하나의 true만 있어도 된다.
elif your_age == 60 or your_age == 70:
  print("birthday party!")
else:
  print("go ahead!")

# True and True == True
# False and True == False
# True and False == False
# False and False == False

# True or True == True
# True or Fasle == True
# False or True == True
# False or Flase == False