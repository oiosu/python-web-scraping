distance = 0

while distance < 20:
  print("I'm running:", distance, "km")
  distance = distance + 1

# chapter 06 Python Casino
# user가 이길때까지 반복하는 코드

from random import randint

print("welcome to python casino")
pc_choice = randint(1, 50)

playing = True

# whiledms 조건문 부분(playing) 이 True 일때만 동작한다
while playing:
  user_choice = int(input("choose number:"))
  if user_choice == pc_choice:
    print("you won!")
    # user가 이긴다면 게임은 끝
    playing = False
  elif user_choice > pc_choice:
    print("lower! Computer chose", pc_choice)
  elif user_choice < pc_choice:
    print("higher!")