
from random import randint
# input 함수는 사용자에게 input을 요청하고, 사용자가 키보드로
# 입력한 문자열을 반환할 것이다.
user_choice = int(input("choose number:"))
# pc_choice = 50 을 랜덤 숫자로 만들어주기(function을 module에서 가져오기)
pc_choice = randint(1, 50)

if user_choice == pc_choice:
  print("you won!")
elif user_choice > pc_choice:
  print("lower! Computer chose", pc_choice)
elif user_choice < pc_choice:
  print("higher!")

# 공식문서 참고하기
# random.randint(a, b)
# : 이 function은 random 한 정수 n을 반환한다.
# 첫번째 parameter a은 n 보다 작거나 같고, n은 두번째 parameter b보다
# 작거나 같다.
