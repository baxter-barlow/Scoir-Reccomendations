import requests
import re

print("You must enter your Scoir credentials")
email = input("Enter your email: ")
password = input("Enter your password: ")
login_url = "https://app.scoir.com/api/login"
login_info = {
  "UserName": email,
  "Password": password,
}
login = requests.post(login_url, json=login_info)
access_token = login.json()["access_token"]
refresh_token = login.json()["refresh_token"]
user_id = login.json()["UserId"]

url = "https://app.scoir.com/api/user/recommendations"

payload = {}
headers = {
  'authority':
  'app.scoir.com',
  'accept':
  '*/*',
  'accept-language':
  'en-US,en;q=0.9',
  'authentication':
  f'Bearer {access_token}',
  'referer':
  'https://app.scoir.com/student/my-colleges',
  'sec-ch-ua':
  '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile':
  '?0',
  'sec-ch-ua-platform':
  '"macOS"',
  'sec-fetch-dest':
  'empty',
  'sec-fetch-mode':
  'cors',
  'sec-fetch-site':
  'same-origin',
  'user-agent':
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)
json_dump = response.json()['Recommendations']
for rec in json_dump:
  print(rec['StaffFirstName'], rec['StaffLastName'] + ":")
  try:
    body = rec['Text']['Body']
    clean = re.compile('<.*?>')
    print(re.sub(clean, '', body))
  except Exception as e:
    print(e)
