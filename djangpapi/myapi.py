import requests
import json
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

urls="http://127.0.0.1:8000/crudapi/"
def get_data(id=None):
    data={'id':id}
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.get(url=urls,headers=headers ,data=json_data)
    data=r.json()
    print(data)
#get_data()

def post_data():
    data={
     
        "c_name": "mohan",
        "phone": 787890,
        "age": 66,
        "gender": "M",
        "address": "faridabad"
    }
    
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=urls,headers=headers,data=json_data)
    data=r.json()
    print(data)
#post_data()


def update_data():
    data={
         "id": 8,
        "c_name": "jack ryan",
        "phone": 34587890,
        "age": 39,
        "gender": "M",
        "address": "california"
    }
    
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url=urls,headers=headers,data=json_data)
    data=r.json()
    print(data)
#update_data()

def delete_data():
    data={
         "id": 5,
        
    }
    
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.delete(url=urls,headers=headers,data=json_data)
    data=r.json()
    print(data)
delete_data()




