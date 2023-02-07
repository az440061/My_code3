import time
import asyncio
import requests

URL = "http://192.168.0.106:3000/api/"
getAll = "getAllUsers"
post = "save-user"
puts = "updateUser"
patch = "updateUserStatus"
deleteUser = "deleteUser"


my_list = {

    "id": "",
    "f_name": "",
    "l_name": "",
    "email": "",
    "status": ""
}

async def get_api():
    # get = requests.get(URL + getAll)
    result = requests.get(URL + getAll)
    await asyncio.sleep(3)
    if result.status_code == 200:
        print(result.json())
        return result.json()
    else:
        return { "status" : 400}





async def get_apiList():
    task = asyncio.create_task(get_api())
    await task
    temp = task.result()
    print("status",temp["status"])
    dataList = temp["data"]
    print("global api", dataList)

    islistvailable = False
    for item in dataList:
        if item["user_status"] == "active":
            # item["email"]== "sanrter.mitchel.co.in"):
            my_list["id"] = item["_id"]
            my_list["email"] = item["email"]
            my_list["status"] = item["user_status"]

            print(item["full_name"])
            islistvailable = True
            break

    if islistvailable:
        # post_api()
        # put_api()
        patch_api(my_list)
        # delete_api()
        # patch_api()

    else:
        print("no pending status")


# "john,uttin,jhon@gmail.comm,876667,CEO,HPCL"
def post_api(my):

    my = my_list

    for count in range(0,5):
        new_product = {

            "first_name": "john",
            "last_name": "uutin",
            "email": "john@usv.co.in",
            "mobile": "54300",
            "job_role": "writer",
            "company": "IND"

        }

        requests.post(URL + post, json=new_product)
        # print("new product added ", postreq.json())
        print("new user added ",new_product,my)

        # get_apiList()

def patch_api(my_list):

    list = my_list
    print("patch api called")
    time.sleep(2)
    # islistavailablein = get_apiList()

    if list["status"]== "active":
        dic ={
            "_id": list["id"],
            "user_status" : "active"
        }
        print("my list item for updating",my_list["id"])
        requests.patch(URL + patch ,json=dic)
        print("user status updated",dic)

        # put_api()

    # else:
        # put_api()

def put_api():

    print("put api called")
    time.sleep(2)
    # respons = requests.get(URL + getAll)
    # list_of_data = respons.json()
    # my_dict = list_of_data["data"]
    # print("list of data", my_dict)

    mobile_update = [ {"id": my_list["id"],"mobile":"111"}
                      # {"id": "63df7e5f7e112932fe5b7385","mobile":"222"},
                      # {"id": "63df7e5f7e112932fe5b7388","mobile":"333"},
                      # {"id": "63df7e5f7e112932fe5b738b","mobile":"444"},
                      # {"id": "63df7e5f7e112932fe5b738e","mobile":"555"}
                    ]

    for item in mobile_update :
        # if item["id"]== my_list["id"]:
        #     print(item["id"])

        update_user = {

            "_id" : item["id"],
            # "first_name": "umran",
            # "last_name": "akmal",
            # "email": "jas@bum.co.in",
            "mobile": item["mobile"],
            # "job_role": "cricketer",
            "company": "IND"
        }
        requests.put(URL + puts ,json=update_user)
        break

    # asyncio.run(get_apiList())


def delete_api():
    time.sleep(2)

    param = {
        "_id": my_list["id"],
        "user_status": "delete"
    }

    delete = requests.delete(URL + deleteUser, json=param)
    print("delete user ",delete)

    # get_apiList()
    # post_api()

# get_api()
asyncio.run(get_apiList())
