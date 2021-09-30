import os
import requests
import json
from conf import Conf


def get_token(url, username, password):

    try:
        headers = {'content-type': 'application/json'}
        data = {"username": username, "password": password}
        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        token = f"JWT {response.json()['access_token']}"
        return token
    except requests.exceptions.HTTPError as err:
        print(f"Error  ---- {err}")


def save_info(data_dir, init_date):
    cur_dir = (os.path.join(data_dir, init_date))
    os.makedirs(cur_dir, exist_ok=True)
    try:
        response = requests.get(url=url, data=json.dumps({"date": init_date}), headers=header)
        with open(file=os.path.join(cur_dir, f'{init_date}.json'), mode='w') as f:
            json.dump(response.json(), f)
    except requests.exceptions.HTTPError as err:
        print(f"Error ---- {err}")


if __name__ == '__main__':
    conf = Conf(path='./conf.yaml')
    conf_AUTH = conf.get_config("AUTH")
    conf_API = conf.get_config("API")
    token = (get_token(url=conf_API["url"] + conf_AUTH["endpoint"], username=conf_AUTH["payload"]["username"], password=conf_AUTH["payload"]["password"]))
    url = conf_API["url"] + conf_API["endpoint"]
    header = {'content-type': 'application/json', 'Authorization': token}
    data = conf_API["payload"].values()
    print(data)
    data = list(data)[0]
    print(data)
    for date_i in data:
        save_info(data_dir='./info', init_date=date_i)
