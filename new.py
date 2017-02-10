import requests
import re
a = str(input().strip())
b = str(input().strip())
res = requests.get(""+a)
urls = []
result = "No"
allLinks = re.findall(r"href=\".+\"", res.text)
for link in allLinks:
        checkres=requests.get(link[6:-1])
        if b in checkres.text:
            result = "Yes"
print (result)