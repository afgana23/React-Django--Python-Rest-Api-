import requests
import json
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

urls="http://127.0.0.1:8000/funapi/"
def get_data():
    data={}
    json_data=json.dumps(data)
    r=requests.get(url=urls,data=json_data)
    data=r.json()
    print(data)
get_data()

def post_data():
    data={"c_name":"sonam",
    "phone":77889900,}
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=urls,headers=headers,data=json_data)
    data=r.json()
    print(data)
post_data()


