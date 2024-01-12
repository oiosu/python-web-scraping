# return value는 function이 어떤 작업을 수행하고 어떤 값을 돌려주는 것 

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  print(response)

  # Response [200] 가 출력된다 _ 이 의미는 웹사이트가 성공적으로 응답했다는 뜻


# internet은 http protocol 에 기반한다고 말 할 수 있다.
# 컴퓨터들이 서로 소통하는 방식은 당연하게도 HTTP request이다.
# 그래서 request가 정상인지 아닌지를 알 수 있는 수단이 있어야 하는데
# request의 결과를 확인하는 방법으로 HTTP 코드를 사용한다

# get function이 request한 response는 다른 것도 가지고 있는데 예를 들면 상태 코드이다.
  
"""
for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  print(response.status_code)

# 200 이 출력된다 

"""

"""
for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    print(f"{website} is OK")
  else: 
    print(f"{website} is not OK")

"""

# ok 또는 fail 같은 응답으로 dictionary를 만들고 싶다면, results라는 dictionary 만들기
# results dictionary 안에 새로운 entry 추가하기
"""
results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    results[website] = "OK"
  else: 
    results[website] = "FAILED"

  print(results)
"""
