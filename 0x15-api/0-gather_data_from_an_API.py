#!/usr/bin/python3
import requests as r
import sys

if _name_ == '_main_':
    url = 'https://jsonplaceholder.typicode.com/'
    usr_id = r.get(url + 'user/{}'.format(sys.argv[1])).json()
    to_do = r.get(url + 'todos', params={'userID': sys.argv[1]}).json()
    completed = [title.get("title") for title in to_do if
                 title.get('completed') is True]
    print(completed)
    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                          len(completed),
                                                          len(to_do)))
    [print("\t {}".format(title)) for title in completed]
