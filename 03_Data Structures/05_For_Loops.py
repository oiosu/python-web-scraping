# for 반복문을 사용할 때 for는 각각의 item이 실행될 때 placeholder를
# 만드는 것을 허락해준다
# placeholder는 꼭 each일 필요가 없다 (이름 마음대로 지정 가능)

websites = ("google.com", "airbnb.com", "twitter.com", "facebook.com")

# python에게 list의 각 item을 활용해서 자동으로 코드를 실행하는 방법
# => for 반복분(loop) 라는 것을 사용

for each in websites:
  # hello 가 4번 출력이 된다
  print("hello")

#  each => 현재 실행중인 item에 접근하는 변수 이름은 마음대로 지정가능
"""
for potato in websites: 
  print("potato is equals to", potato)

# 출력 
potato is equals to google.com
potato is equals to airbnb.com
potato is equals to twitter.com
potato is equals to facebook.com

"""

# 흔한 관습 => 튜플이나 리스트를 만들 때 복수형을 사용한다