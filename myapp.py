import requests
import json

URL = 'http://localhost:8000/'

def read():
     r = requests.get(url=URL)
     data = r.json()
     print(data)

# read() #function to get data in json format 

def create():
    data = {
        'name':'raj',
        'service':'beard set',
        'service_man':'nilesh',
        'date': '2022-07-25',
        'check_in': '06:37:30',
        'check_out': '06:37:56',
        'cost':450
    }

    json_data = json.dumps(data)
    r = requests.post(url= URL, data= json_data)
    data = r.json()
    print(data)
# create()  #function to send data to python application into json 

def update():
    data = {
        'id' : 3,
        'name':'rohit',
        'service':'haircut',
        'service_man':'nilesh',
        'date': '2022-07-25',
        'check_in': '06:37:30',
        'check_out': '06:57:56',
        'cost':350
    }

    json_data = json.dumps(data)
    r = requests.put(url= URL, data= json_data)
    data = r.json()
    print(data)
# update()

def delete():
    data = {
        'id' : 1
    }

    json_data = json.dumps(data)
    r = requests.delete(url= URL, data= json_data)
    data = r.json()
    print(data)
# delete()  

