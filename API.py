import time

import requests

URL = "http://192.168.0.106:3000/api/"
getAll = "getAllUsers"
post = "save-user"
puts = "updateUser"
patch = "updateUserStatus"
deleteUser = "deleteUser"
globalAPI = requests.get(URL + getAll).json()
my_dic = globalAPI["data"]

my_list = {

    "id": "",
    "f_name": "",
    "l_name": "",
    "email": "",
    "status": ""
}

def get_api():

    get = requests.get(URL + getAll)
    if get.status_code == 200:
        print(get.json())

    else:
        print("Error in API")

def get_apiList():

    # isAPIavailable = get_api()

    get = requests.get(URL + getAll)
    # if isAPIavailable:
    #     print("my dic",my_dic)
    islistvailable = False
    for item in get.json()["data"]:
        if item["user_status"] == "pending":
            print(len(item))
            my_list["id"] = item["_id"]
            my_list["email"] = item["email"]
            my_list["status"] = item["user_status"]

            print(item["_id"])
            islistvailable = True
            break

    if islistvailable :
        # post_api()
        # put_api()
        patch_api()
        # delete_api()
        # patch_api()


    else:
        print("no pending status ")


def post_api():

    for count in range(0,5) :
        new_product = {

            "first_name": "umran",
            "last_name": "akmal",
            "email": "jas@bum.co.in",
            "mobile": "945024059",
            "job_role": "cricketer",
            "company": "IND"

        }

        requests.post(URL + post, json=new_product)
        # print("new product added ", postreq.json())
        print("new user added ",new_product)

        get_apiList()

def patch_api():
    time.sleep(2)
    # islistavailablein = get_apiList()

    if my_list["status"]== "pending":
        dic ={
            "_id": my_list["id"],
            "user_status" : "active"
        }
        print("my list item for updating",my_list["id"])
        requests.patch(URL + patch ,json=dic)
        print("user status updated",dic)

        put_api()

    else:
        put_api()

def put_api():
    time.sleep(2)
    # respons = requests.get(URL + getAll)
    # list_of_data = respons.json()
    # my_dict = list_of_data["data"]
    # print("list of data", my_dict)

    mobile_update = [ {"id": "63df7e5f7e112932fe5b7382","mobile":"111"},
                      {"id": "63df7e5f7e112932fe5b7385","mobile":"222"},
                      {"id": "63df7e5f7e112932fe5b7388","mobile":"333"},
                      {"id": "63df7e5f7e112932fe5b738b","mobile":"444"},
                      {"id": "63df7e5f7e112932fe5b738e","mobile":"555"}
                    ]

    for item in mobile_update :
        if item["id"]== my_list["id"]:
            print(item["id"])

            update_user = {

                "_id" : my_list["id"],
                # "first_name": "umran",
                # "last_name": "akmal",
                # "email": "jas@bum.co.in",
                "mobile": item["mobile"],
                # "job_role": "cricketer",
                "company": "IND"
            }
            requests.put(URL + puts ,json=update_user)

    get_apiList()


def delete_api():
    time.sleep(2)

    param = {
        "_id": my_list["id"],
        "user_status" : "delete"
    }

    delete = requests.delete(URL + deleteUser, json=param)
    print("delete user ",delete)

    get_apiList()
    # post_api()

# get_api()
get_apiList()
