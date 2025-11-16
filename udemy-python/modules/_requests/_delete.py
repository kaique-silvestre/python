import requests

link = "https://python-api-a70a6-default-rtdb.firebaseio.com/-OTnPhDnV0EFfXr3EXoA/-OTnRzl0C-JHmv87a5nG/.json"

response = requests.delete(link)
print(response)