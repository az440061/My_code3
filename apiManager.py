import requests

URL = "http://192.168.0.105:3000/api/"
getAll = "/getAllUsers"
post = "save-user"
puts = "updateUser"
delete = ""

def get_api():

    get = requests.get(URL + getAll)
    if get.status_code == 200:
        source = get.json()
        print("source",source)
        print(get.elapsed)

    else:
        print("no data found ")

    # get_api_limit()

    post_api()

def post_api():

    print("Post new product")

    new_product = {

        "first_name": "nicholas ",
        "last_name": "cage",
        "email": "nicho@cage.co.in",
        "mobile": "unavalaible",
        "job_role": "actor",
        "company": "hollywood"

    }

    post =requests.post(URL+"save-user",json=new_product)
    print("new product added ",post.json())

    put_api()

def put_api():


    update = {

        "first_name": "nicholas ",
        "last_name": "cage-lincon",
        "email": "nicho@cage.co.in",
        "mobile": "unavalaible",
        "job_role": "actor",
        "company": "hollywood"

    }

    put = requests.put(URL + puts,params={"id":"63da6380d27d7d797e606c00"},json={update})
    print(put.json())

get_api()
