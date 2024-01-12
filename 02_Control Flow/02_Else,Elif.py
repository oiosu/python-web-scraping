password_correct = True
# password_correct = False

if password_correct:
  print("here is your money")
  # else블럭에는 if의 조건이 fase일때 실행될 코드가 될 것이다.
else:
  print("wrong password")

# example 2
winner = 10

if winner > 10:
  print("winner is greater than 10")
# elif는 코드에 또 다른 대안과 조건을 넣을 수 있도록 해준다.
elif winner < 10:
  print("winner is less than 10")
# else는 조건이 true가 아닐 때, 즉 오직 대안만 제공할 수 있도록 해준다.
# else는 모든 경우가 false일 때 실행된다.
else:
  print("winner is 10")