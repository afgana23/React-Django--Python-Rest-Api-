import requests
import json
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

URl="http://127.0.0.1:8000/addapi"
def post_data():
    data={
   
    "c_name":"sonam",
    "phone":77889900,
    "age":30,
    "gender":"female",
    "address":"toronto",

}
    json_data=json.dumps(data)
    r=requests.post(url=URl,data=json_data,headers=headers)
    data=r.json()
    print(data)
post_data()

