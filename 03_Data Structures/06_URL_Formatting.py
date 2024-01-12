# (1)
# 만약 웹사이트 주소가 http로 시작하면 바로 이동하고
# 만약 그렇지 않다면 https를 붙여줘야 한다

websites = ("google.com", "airbnb.com", "https://twitter.com", "facebook.com",
            "https://tiktok.com")

for website in websites:
  print(website)

# websiste 변수는 차례대로 각 사이클에서 리스트 안의 item으로
# 바뀐다는 것을 잊지 말기

for website in websites:
  #  if오직 무언가가 true인지 false인지만 판단한다
  if website.startswith("https://"):
    print("good to go")
  else:
    print("we have to fix it")

# (2) website 가 https:// 로 시작하지 않는 경우에 집중하기
for website in websites:
  if not website.startswith("https://"):
    print("have to fix it")

# (3)  https:// 로 시작할 수 있도록 업데이트 하기
for website in websites:
  if not website.startswith("https://"):
    # string안에 변수를 넣는 방법
    website = f"https://{website}"
  print(website)